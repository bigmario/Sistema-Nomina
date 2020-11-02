#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Generacion de Reportes
## Ultima Revisión: 06-06-2012 2:50p.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 18 de Mayo de 2012
#
# +-------------------------------------------------+#
###########################################################################

import os
import sys
import tempfile
from modelo import ModeloBD
import diasLaborales
from datetime import datetime, date
import time
from dateutil import relativedelta
from dateutil import rrule
import calendar

#Obtenemos de platypus las clases Paragraph, para escribir párrafos Image, para insertar imágenes y SimpleDocTemplate para definir el DocTemplate.
#Además importamos Spacer, para incluir espacios  e Image para agregar El logo en la cabecera.
from reportlab.platypus import Paragraph
from reportlab.platypus import Image
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate
from reportlab.platypus import Spacer
from reportlab.platypus import Table
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
#Se carga el módulo apropiado para las tablas:
from reportlab.platypus import Table
#Importamos clase de hoja de estilo de ejemplo.
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
#Se importa el tamaño de la hoja.
from reportlab.lib.pagesizes import letter
#Y los colores.
from reportlab.lib import colors


class Reportes:

    def __init__(self):
        self.BD=ModeloBD()

    def sumarHoras(self, m, t):
        #sumarHoras(f[9], f[10])

        total=0
        totalM=0
        hM, mM, sM = map(int, m.split(":"))
        totalM = 3600*hM + 60*mM + sM

        totalT = 0
        hT, mT, sT = map(int, t.split(":"))
        totalT = 3600*hT + 60*mT + sT

        total=totalM+totalT
        totalMT="%02d:%02d:%02d" % (total / 3600, total / 60 % 60, total % 60)
        return totalMT

    def calcularPorcentajeAsistencia(self):
        pass

    def crearProyeccion(self, profesor, fecha_inicio, fecha_fin):
        datosNucleo=self.BD.obtenerDatosNucleo()
        datosProfesor=self.BD.obtenerDatosProf(profesor)
        self.profeID=datosProfesor[0]
        horas=self.BD.calcularPromedioHoras(self.profeID, fecha_inicio, fecha_fin)
        hLaborales=self.BD.obtenerHorasLaborales(self.profeID)
        catedrasDictadas=self.BD.buscarNomCatedraDictada(self.profeID, rep=True)

        lines=[]

        #calculo el pomedio de horas asistidas y el porcentaje de asistencia
        if not horas==[]:
            for hora in horas:
                lines.append(hora[0])
            total = 0
            for line in lines:
                h, m, s = map(int, line.split(":"))
                total += 3600*h + 60*m + s

            inicio2 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            fin2= datetime.strptime(fecha_fin, "%Y-%m-%d")

            inicio3=inicio2.date()
            fin3=fin2.date()

            meses=relativedelta.relativedelta(fin3, inicio3) #calcula el tiempo entre las dos fechas (RELATIVEDELTA)

            dias_laborales=self.BD.obtenerDiasLaborales(self.profeID)

            print diasLaborales.diasLaborales(inicio3, fin3, 10)

            dias_feriados=[]

            dia=[]
            for d in dias_laborales:
                if d[0]=='Domingo':
                    dia.append(rrule.SU)
                elif d[0]=='Lunes':
                    dia.append(rrule.MO)
                elif d[0]=='Martes':
                    dia.append(rrule.TU)
                elif d[0]=='Miercoles':
                    dia.append(rrule.WE)
                elif d[0]=='Jueves':
                    dia.append(rrule.TH)
                elif d[0]=='Viernes':
                    dia.append(rrule.FR)
                elif d[0]=='Sabado':
                    dia.append(rrule.SA)

            dia2=tuple(dia)

            semanas= rrule.rrule(rrule.WEEKLY, dtstart=inicio3, until=fin3, wkst=rrule.MO, byweekday=dia2) #calcula la fechas de catedra en cada semana en el lapso
            #semanas2=semanas.between(inicio2, fin2, inc=True)

            numero_semanas=semanas.count()/len(dia2)

            #numero_semanas2=len(semanas2)/len(dia2)

            semanas3=list(semanas)

            semanaInicio=semanas3[:1][0]
            semanaFin=semanas3[-1:][0]

            #calculo la cantidad de horas laborales en el lapso
            hlab, mlab, slab = map(int, hLaborales[0].split(":"))
            lab = (3600*hlab + 60*mlab + slab)*numero_semanas

            #lab2=lab*meses.months
            lab2=lab

            carga_laboral="%02d:%02d:%02d" % (lab2 / 3600, lab2 / 60 % 60, lab2 % 60)

            total2=total/len(lines)

            promedio= "%02d:%02d:%02d" % (total2 / 3600, total2 / 60 % 60, total2 % 60)

            print "Tiempo entre %s y %s: %s meses y %s dias"%(fecha_inicio, fecha_fin, meses.months, meses.days)
            print "Numero de Semanas entre %s y %s: %s"%(fecha_inicio, fecha_fin, numero_semanas)
            print "Semana Inicial_1: %s"%semanaInicio.strftime("%d-%m-%Y")
            print "Semana Final_1: %s"%semanaFin.strftime("%d-%m-%Y")
            print "Carga horaria mensual %02d:%02d:%02d" % (lab / 3600, lab / 60 % 60, lab % 60)
            print "carga horaria lapso %02d:%02d:%02d" % (lab2 / 3600, lab2 / 60 % 60, lab2 % 60)
            print "horas totales %02d:%02d:%02d"%(total / 3600, total / 60 % 60, total % 60)
            print "horas promediadas %02d:%02d:%02d"%(total2 / 3600, total2 / 60 % 60, total2 % 60)
            print "Dias de asistencia %s"%(len(lines))
            print "\n"

            #calculo el porcentaje de asistencia
            porcentaje=(float(total)) * 100 / float(lab2)
        else:
            lab2=0
            promedio="00:00:00"
            carga_laboral="00:00:00"
            total=0

        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='TotalHorasPromediadas', alignment=TA_CENTER, fontSize=11, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='TotalHorasHorario', alignment=TA_CENTER, fontSize=11, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='Datos', alignment=TA_LEFT, fontSize=10,))
        estiloHoja.add(ParagraphStyle(name='Catedras', alignment=TA_LEFT, fontSize=9, bulletIndent = 18))


        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        tHorasP=estiloHoja['TotalHorasPromediadas']
        tHorasH=estiloHoja['TotalHorasHorario']
        datos=estiloHoja['Datos']
        catedras=estiloHoja['Catedras']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen), width=200,height=50)
        imagen_logo.hAlign = 'LEFT'
        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"<b>Proyección de Asistencia de Profesor - Núcleo %s</b>" % (unicode(datosNucleo[0][3],))
        cadena5=u"<u>Lapso Calculado: del %s-%s-%s al %s-%s-%s</u>" % (fecha_inicio[8:], fecha_inicio[5:7], fecha_inicio[:4], fecha_fin[8:], fecha_fin[5:7], fecha_fin[:4])

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo = Paragraph(cadena, subtitulo)
        parrafo12 = Paragraph(cadena5, subtitulo)

        #Y lo incluimos en el story.
        story.append(parrafo)
        story.append(parrafo12)

        #Dejamos espacio.
        story.append(Spacer(0,20))

        nombre= u"<b>Nombre del Profesor</b>: %s, %s" % (datosProfesor[2], datosProfesor[1])
        cedula=u"<b>Cédula de Identidad</b>: %s" % (datosProfesor[3],)
        telefono=u"<b>Telefono</b>: %s" % (datosProfesor[4],)

        if datosProfesor[5]=='Si':
            activo=u"<b>Estado</b>: PROFESOR ACTIVO"
        elif datosProfesor[5]=='No':
            activo=u"<b>Estado</b>: PROFESOR INACTIVO"

        if datosProfesor[6]==0:
            tipo=u"<b>Categoría del Profesor</b>: Profesor por Hora"
        elif datosProfesor[6]==1:
            tipo=u"<b>Categoría del Profesor</b>: Profesor En Comisión de Servicio"
        elif datosProfesor[6]==2:
            tipo=u"<b>Categoría del Profesor</b>: Profesor Fijo"

        cadena4="<b>Cátedras Dictadas</b>:"

        parrafo2 = Paragraph(nombre, datos)
        parrafo3 = Paragraph(cedula, datos)
        parrafo4 = Paragraph(telefono, datos)
        parrafo5 = Paragraph(tipo, datos)
        parrafo6 = Paragraph(activo, datos)
        parrafo10 = Paragraph(cadena4, datos)

        story.append(parrafo2)
        story.append(Spacer(20,2))
        story.append(parrafo3)
        story.append(Spacer(20,2))
        story.append(parrafo4)
        story.append(Spacer(20,2))
        story.append(parrafo5)
        story.append(Spacer(20,2))
        story.append(parrafo6)
        story.append(Spacer(20,2))
        story.append(parrafo10)

        for i in range(len(catedrasDictadas)):
            listaCatedras=unicode('%s'%catedrasDictadas[i][0])
            parrafo11 = Paragraph(listaCatedras, catedras, bulletText='\xe2\x80\xa2')
            story.append(Spacer(20,2))
            story.append(parrafo11)

        story.append(Spacer(0,20))
        cadena2=u"Horas Diarias Promediadas de Asistencia en este Lapso: %s" % (promedio)
        cadena3=u"Carga Horaria para este Lapso: %s" % (carga_laboral)
        horascumplidas=u"Horas Totales de Asistencia en este Lapso: %02d:%02d:%02d"%(total / 3600, total / 60 % 60, total % 60)

        # string to time tuple PROMEDIADAS
        if not promedio == "00:00:00":
            hayAsistencia=True
        else:
            hayAsistencia=False

        if hayAsistencia:
            cadena4=u"Porcentaje de Asistencia en este Lapso: <b>%s %%</b>"%(round(porcentaje))
        else:
            cadena4=u"No hay Asistencia para este Profesor en el lapso seleccionado, no pudo calcularse el Promedio de Asistencia"


        parrafo7 = Paragraph(cadena2, tHorasP)
        story.append(parrafo7)
        story.append(Spacer(0,5))
        parrafo8 = Paragraph(cadena3, tHorasP)
        story.append(parrafo8)
        story.append(Spacer(0,5))
        parrafo12 = Paragraph(horascumplidas, tHorasP)
        story.append(parrafo12)
        story.append(Spacer(0,5))
        parrafo9 = Paragraph(cadena4, tHorasP)
        story.append(parrafo9)

        #Dejamos espacio.
        story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        name = "Proyeccion-%s-%s" % (date_str, os.getpid())
        temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
        temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.build(story)

        self.open_report(temp.name)


    def CrearFichaProfesor(self, prof):

        datosNucleo=self.BD.obtenerDatosNucleo()
        datosProfesor=self.BD.obtenerDatosProf(prof)
        self.profeID=datosProfesor[0]
        ficha=self.BD.fichaProfesor(datosProfesor[0])
        #dias=self.BD.buscar_dia_Prof(self.profeID)


        ##############################################################################
        ##############################################################################


        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='TotalHoras', alignment=TA_CENTER, fontSize=7, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='TotalHorasGenerales', alignment=TA_CENTER, fontSize=11, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='Datos', alignment=TA_LEFT, fontSize=10,))
        estiloHoja.add(ParagraphStyle(name='SinAsistencia', alignment=TA_CENTER, fontSize=7, textColor=colors.red, ))


        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        tHoras=estiloHoja['TotalHoras']
        tHorasGenerales=estiloHoja['TotalHorasGenerales']
        datos=estiloHoja['Datos']
        sinAsistencia=estiloHoja['SinAsistencia']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen), width=200,height=50)
        imagen_logo.hAlign = 'LEFT'
        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"Ficha de Profesor - Núcleo %s" % (unicode(datosNucleo[0][3],))

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        story.append(Spacer(0,20))

        #################################################################

        filasContenido=[]
        fila1 = [u'Día',u'Cátedra',u'E. Mañana', u'S. Mañana', u'E. Tarde', u'S. Tarde', 'Horas', 'Observaciones']
        filasContenido.append(fila1)

        nombre= u"Nombre del Profesor: %s, %s" % (datosProfesor[2], datosProfesor[1])
        cedula=u"Cédula de Identidad: %s" % (datosProfesor[3],)
        telefono=u"Telefono: %s" % (datosProfesor[4],)

        if datosProfesor[5]=='Si':
            activo=u"Estado: PROFESOR ACTIVO"
        elif datosProfesor[5]=='No':
            activo=u"Estado: PROFESOR INACTIVO"

        if datosProfesor[6]==0:
            tipo=u"Categoría del Profesor: Profesor por Hora"
        elif datosProfesor[6]==1:
            tipo=u"Categoría del Profesor: Profesor En Comisión de Servicio"
        elif datosProfesor[6]==2:
            tipo=u"Categoría del Profesor: Profesor Fijo"

        parrafo3 = Paragraph(nombre, datos)
        parrafo4 = Paragraph(cedula, datos)
        parrafo5 = Paragraph(telefono, datos)
        parrafo6 = Paragraph(tipo, datos)
        parrafo7 = Paragraph(activo, datos)

        story.append(parrafo3)
        story.append(parrafo4)
        story.append(parrafo5)
        story.append(parrafo6)
        story.append(parrafo7)

        story.append(Spacer(0,20))
        story.append(Spacer(0,20))

        if not ficha==[]:
            for f in ficha:
                if f[3]=='00:00:00' and f[4]=='00:00:00':
                    filasContenido.append([f[2],f[14],'','',f[5], f[6], f[8], f[10]])
                elif f[5]=='00:00:00' and f[6]=='00:00:00':
                    filasContenido.append([f[2], f[14], f[3],f[4],'','', f[7], f[10]])
                else:
                    filasContenido.append([f[2], f[14], f[3],f[4], f[5],f[6], self.sumarHoras(f[7], f[8]), f[10]])

            #Definimos la tabla.
            tabla = Table(filasContenido)

            #Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos a poner de color azul Mañana,Tarde y Noche y en color rojo los días de la semana.
            tabla.setStyle([('TEXTCOLOR',(0,0),(7,0),colors.blue),('TEXTCOLOR',(1,1),(0,-1),colors.blue), ('FONTSIZE',(0,0),(-1,-1),8)])
            #Damos color de fondo a las cabeceras.
            tabla.setStyle([('BACKGROUND',(0,0),(7,0),colors.gray),('VALIGN',(0,1),(-1,-1),'TOP')])
            #Creamos una caja alrededor de las celdas.
            tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
            #Y ponemos una malla (rejilla) a la tabla.
            tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
            #Y la asignamos al platypus story.
            story.append(tabla)
            story.append(Spacer(0,20))
            self.BD.conectar()
            self.BD.cursor.execute("""SELECT distinct horaslaborales FROM dias WHERE profesor_idprofesor=?""", (datosProfesor[0],))
            horasDictadas=self.BD.cursor.fetchone()
            self.BD.desconectar()
            horasTrabajadas=Paragraph(u'Carga Horaria Semanal :%s'%horasDictadas, tHoras)
            story.append(horasTrabajadas)
            story.append(Spacer(0,20))
        else:
            parrafo5=Paragraph(u'No hay asistencia para esta Cátedra, en este Corte', sinAsistencia)
            story.append(parrafo5)
            story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        name = "FichaProf-%s-%s" % (date_str, os.getpid())
        temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
        temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.build(story)

        self.open_report(temp.name)

    def CrearReporteCatedra(self, ca,fecha_Inicio,fecha_Fin, comision):

        datosNucleo=self.BD.obtenerDatosNucleo()

        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='FechaCorte', alignment=TA_RIGHT, fontSize=7, ))
        estiloHoja.add(ParagraphStyle(name='SinAsistencia', alignment=TA_CENTER, fontSize=7, textColor=colors.red, ))
        estiloHoja.add(ParagraphStyle(name='TotalHoras', alignment=TA_CENTER, fontSize=7, textColor=colors.red,))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        fechaCorte=estiloHoja['FechaCorte']
        sinAsistencia=estiloHoja['SinAsistencia']
        tHoras=estiloHoja['TotalHoras']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #parrafo = Paragraph("Conservatorio de Música Simón Bolívar - Extensión Carabobo ",cabecera)

        #Lo incluimos en el Platypus story.

        #story.append(parrafo)

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen), width=200,height=50)
        imagen_logo.hAlign = 'LEFT'
        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u" Reporte Cátedras Núcleo "+unicode(datosNucleo[0][3])

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)

        #Dejamos espacio.

        story.append(Spacer(0,20))

        parrafo3=Paragraph('FECHA DE CORTE: del %s al %s'%(fecha_Inicio, fecha_Fin), fechaCorte)
        story.append(parrafo3)

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        story.append(Spacer(0,20))

        if comision:
            parrafo7=Paragraph(U'PROFESORES EN COMISIÓN DE SERVIIO', subtitulo)
        else:
            parrafo7=Paragraph('PROFESORES POR HORA Y FIJOS', subtitulo)

        story.append(parrafo7)
        story.append(Spacer(0,20))

        seleccion=self.BD.obtenerNombreCatedraX(ca)
        parrafo4=Paragraph(u'Cátedra: '+seleccion[0], subtitulo)
        story.append(parrafo4)
        story.append(Spacer(0,20))

        nomProfe=self.BD.listarNomProfesoresCatedras(ca, comision)

        for nombre in nomProfe:
            filasContenido=[]
            fila1 = ['Nº','Dia', 'Fecha','Entrada', 'Salida', 'Horas', 'Observaciones']
            filasContenido.append(fila1)
            parrafo5=Paragraph('Profesor: '+nombre[0]+', '+nombre[1], subtitulo)
            story.append(parrafo5)
            story.append(Spacer(0,20))
            catedra=self.BD.reporteCatedras(ca, nombre[2],fecha_Inicio,fecha_Fin, comision)
            horasDictadas=self.BD.sumarHorasDictadas(nombre[3], fecha_Inicio,fecha_Fin, ca)
            if not catedra==[]:
                for cat in catedra:
                    filasContenido.append([cat[10], cat[2], "%s-%s-%s"%(cat[1][8:], cat[1][5:7], cat[1][:4]), cat[3],cat[4], cat[0], cat[5]])
                #Definimos la tabla.
                tabla = Table(filasContenido)

                #Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos a poner de color azul Mañana,Tarde y Noche y en color rojo los días de la semana.
                tabla.setStyle([('TEXTCOLOR',(0,0),(6,0),colors.blue),('TEXTCOLOR',(1,1),(0,-1),colors.blue), ('FONTSIZE',(0,0),(-1,-1),8)])
                #Damos color de fondo a las cabeceras.
                tabla.setStyle([('BACKGROUND',(0,0),(6,0),colors.gray),('VALIGN',(0,1),(-1,-1),'TOP')])
                #Creamos una caja alrededor de las celdas.
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #Y ponemos una malla (rejilla) a la tabla.
                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                #Y la asignamos al platypus story.
                story.append(tabla)
                horasTrabajadas=Paragraph(u'Horas Totales: '+horasDictadas, tHoras)
                story.append(horasTrabajadas)
                story.append(Spacer(0,20))
            else:
                parrafo5=Paragraph(u'No hay asistencia para este Profesor, en este Corte', sinAsistencia)
                story.append(parrafo5)
                story.append(Spacer(0,20))

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        if comision:
            name = "ReporteCat_ComServ-%s-%s" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()
        else:
            name = "ReporteCat_HorasyFijos-%s-%s" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.build(story)

        self.open_report(temp.name)

    def CrearReporteProf(self, prof,fecha_Inicio,fecha_Fin, comision):
        #instanciamos el controlador de la BD

        datosNucleo=self.BD.obtenerDatosNucleo()

        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=15, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='FechaCorte', alignment=TA_RIGHT, fontSize=7, ))
        estiloHoja.add(ParagraphStyle(name='SinAsistencia', alignment=TA_CENTER, fontSize=7, textColor=colors.red, ))
        estiloHoja.add(ParagraphStyle(name='TotalHoras', alignment=TA_CENTER, fontSize=7, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='TotalHorasGenerales', alignment=TA_CENTER, fontSize=11, textColor=colors.red,))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        fechaCorte=estiloHoja['FechaCorte']
        sinAsistencia=estiloHoja['SinAsistencia']
        tHoras=estiloHoja['TotalHoras']
        tHorasGenerales=estiloHoja['TotalHorasGenerales']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #parrafo = Paragraph("Conservatorio de Música Simón Bolívar - Extensión Carabobo ",cabecera)

        #Lo incluimos en el Platypus story.

        #story.append(parrafo)
        #story.append(Spacer(0,10))

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen), width=200,height=50)
        imagen_logo.hAlign = 'LEFT'
        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = u"Reporte de Profesor Núcleo "+unicode(datosNucleo[0][3])

        #Damos un estilo al segundo párrafo, que será el texto a escribir.
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)

        #Dejamos espacio.

        story.append(Spacer(0,20))

        parrafo3=Paragraph('FECHA DE CORTE: del %s al %s'%(fecha_Inicio, fecha_Fin), fechaCorte)
        story.append(parrafo3)

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        story.append(Spacer(0,20))

        if comision:
            parrafo7=Paragraph(U'PROFESORES EN COMISIÓN DE SERVIIO', subtitulo)
        else:
            parrafo7=Paragraph('PROFESORES POR HORA Y FIJOS', subtitulo)

        story.append(parrafo7)
        story.append(Spacer(0,20))

        seleccionProf=self.BD.obtenerDatosProf(prof)

        horasGenerales=self.BD.sumarHorasDictadas(seleccionProf[0],fecha_Inicio, fecha_Fin)

        parrafo4=Paragraph(u'Profesor: '+seleccionProf[2]+', '+seleccionProf[1], subtitulo)
        story.append(parrafo4)
        story.append(Spacer(0,20))

        catedrasDictadas=self.BD.listarCatedrasConAsistencia(seleccionProf[0], comision)
        horasTotales=[]
        for catedra in catedrasDictadas:
            filasContenido=[]
            fila1 = ['Nº','Dia', 'Fecha','Entrada', 'Salida', 'Horas', 'Observaciones']
            filasContenido.append(fila1)
            parrafo5=Paragraph('Catedra: '+catedra[0], subtitulo)
            story.append(parrafo5)
            catedraTabla=self.BD.reporteProfesor(catedra[1], seleccionProf[0], fecha_Inicio,fecha_Fin,comision)
            horasDictadasPorCatedra=self.BD.sumarHorasDictadas(seleccionProf[0], fecha_Inicio, fecha_Fin, catedra[1])

            if not catedraTabla==[]:
                for cat in catedraTabla:
                    filasContenido.append([cat[7], cat[2], "%s-%s-%s"%(cat[1][8:], cat[1][5:7], cat[1][:4]), cat[3],cat[4], cat[0], cat[5]])
                #Definimos la tabla.
                tabla = Table(filasContenido)

                #Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos a poner de color azul Mañana,Tarde y Noche y en color rojo los días de la semana.
                tabla.setStyle([('TEXTCOLOR',(0,0),(6,0),colors.blue),('TEXTCOLOR',(1,1),(0,-1),colors.blue), ('FONTSIZE',(0,0),(-1,-1),8)])
                #Damos color de fondo a las cabeceras.
                tabla.setStyle([('BACKGROUND',(0,0),(6,0),colors.gray),('VALIGN',(0,1),(-1,-1),'TOP')])
                #Creamos una caja alrededor de las celdas.
                tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])
                #Y ponemos una malla (rejilla) a la tabla.
                tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black)])
                #Y la asignamos al platypus story.
                story.append(tabla)
                horasTrabajadas=Paragraph(u'Horas Totales para esta Cátedra: '+horasDictadasPorCatedra, tHoras)
                story.append(horasTrabajadas)
                story.append(Spacer(0,20))
            else:
                parrafo5=Paragraph(u'No hay asistencia para esta Cátedra, en este Corte', sinAsistencia)
                story.append(parrafo5)
                story.append(Spacer(0,20))

        horasTrabajadasGeneral=Paragraph(u'Horas Totales del Profesor: '+horasGenerales, tHorasGenerales)
        story.append(horasTrabajadasGeneral)

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        if comision:
            name = "ReporteProf_ComServ-%s-%s" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()
        else:
            name = "ReporteProf_HorasyFijos-%s-%s" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.build(story)

        self.open_report(temp.name)

    def CrearFormaUnica(self,fecha_Inicio,fecha_Fin, comision):
        #instanciamos el controlador de la BD

        datosProf=self.BD.formaUnicaProfesores(fecha_Inicio, fecha_Fin, comision)
        datosNucleo=list(self.BD.obtenerDatosNucleo())

        #Creamos un PageTemplate de ejemplo.

        estiloHoja = getSampleStyleSheet()
        estiloHoja.add(ParagraphStyle(name='Cabecera', alignment=TA_CENTER, fontSize=12, ))
        estiloHoja.add(ParagraphStyle(name='SubTitulo', alignment=TA_CENTER, fontSize=11, ))
        estiloHoja.add(ParagraphStyle(name='Nucleo', alignment=TA_LEFT, fontSize=10, textColor=colors.red,))
        estiloHoja.add(ParagraphStyle(name='EntFederal', alignment=TA_LEFT, fontSize=9, ))
        estiloHoja.add(ParagraphStyle(name='Municipio', alignment=TA_RIGHT, fontSize=8, ))
        estiloHoja.add(ParagraphStyle(name='FechaCorte', alignment=TA_RIGHT, fontSize=7, ))
        estiloHoja.add(ParagraphStyle(name='Tabla', alignment=TA_CENTER, fontSize=11, ))

        #Inicializamos la lista Platypus Story.

        story = []

        #Definimos cómo queremos que sea el estilo de la PageTemplate.

        cabecera = estiloHoja['Cabecera']
        subtitulo=estiloHoja['SubTitulo']
        nucleo=estiloHoja['Nucleo']
        EntidadFederal=estiloHoja['EntFederal']
        municipio=estiloHoja['Municipio']
        fechaCorte=estiloHoja['FechaCorte']
        tituloTabla=estiloHoja['Tabla']

        #No se hará un salto de página después de escribir la cabecera (valor 1 en caso contrario).

        cabecera.pageBreakBefore=0

        #Se quiere que se empiece en la primera página a escribir. Si es distinto de 0 deja la primera hoja en blanco.

        cabecera.keepWithNext=0

        #Color de la cabecera.

        cabecera.backColor=colors.cyan

        #Incluimos un Flowable, que en este caso es un párrafo.

        #parrafo = Paragraph("FUNDACION DEL ESTADO PARA EL SISTEMA NACIONAL DE LAS ORQUESTAS JUVENILES E INFANTILES DE VENEZUELA",cabecera)

        #Lo incluimos en el Platypus story.

        #story.append(parrafo)
        #story.append(Spacer(0,20))

        #Ahora incluimos una imagen.

        fichero_imagen = "bitmaps/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen), width=200,height=50)
        imagen_logo.hAlign = 'LEFT'
        story.append(imagen_logo)
        story.append(Spacer(0,20))

        #Definimos un párrafo. Vamos a crear un texto largo para demostrar cómo se genera más de una hoja.

        cadena = "FICHA DE REGISTRO DE PROFESORES"

        #Damos un estilo BodyText al segundo párrafo, que será el texto a escribir.

        estilo = estiloHoja['BodyText']
        parrafo2 = Paragraph(cadena, subtitulo)

        #Y lo incluimos en el story.

        story.append(parrafo2)
        story.append(Spacer(0,20))

        parrafo3=Paragraph(u'NOMBRE DEL NÚCLEO O MÓDULO:'+unicode(datosNucleo[0][3]), nucleo)
        parrafo4=Paragraph('ENTIDAD FEDERAL:'+unicode(datosNucleo[0][4]), EntidadFederal)
        parrafo5=Paragraph('MUNICIPIO:'+unicode(datosNucleo[0][5]), municipio)
        parrafo6=Paragraph('FECHA DE CORTE: del %s al %s'%(fecha_Inicio, fecha_Fin), fechaCorte)

        if comision:
            parrafo7=Paragraph(U'PROFESORES EN COMISIÓN DE SERVICIO', subtitulo)
        else:
            parrafo7=Paragraph('PROFESORES POR HORA Y FIJOS', subtitulo)
        story.append(parrafo3)
        story.append(parrafo4)
        story.append(parrafo5)
        story.append(parrafo6)

        #Dejamos espacio.

        story.append(Spacer(0,20))

        #Y a continuación tendríamos la Tabla:

        #Dejamos espacio.

        story.append(Spacer(0,20))
        story.append(parrafo7)
        story.append(Spacer(0,20))

        #Definimos las filas de una tabla.

        filasContenido=[]
        fila1 = ['Prof. Nº','Apellido y Nombre', 'Cédula de Identidad','Cátedra', 'Horas Trabajadas']
        filasContenido.append(fila1)

        for profesor in datosProf:
            horasGenerales=self.BD.sumarHorasDictadas(profesor[0],fecha_Inicio, fecha_Fin)
            catedrasDictadas=self.BD.listarCatedrasasistenciaProf(profesor[0])
            listaCatedras=''
            for i in range(len(catedrasDictadas)):
                listaCatedras=unicode(catedrasDictadas[i][0])+'\n'+listaCatedras

            filasContenido.append([unicode(profesor[0]), profesor[1]+', '+profesor[2], unicode(profesor[3]), listaCatedras, horasGenerales])

        #Definimos la tabla.

        tabla = Table(filasContenido)

        #Podemos dar estilo a los elementos de una tabla. En esta ocasión vamos a poner de color azul Mañana,Tarde y Noche y en color rojo los días de la semana.

        tabla.setStyle([('TEXTCOLOR',(0,0),(4,0),colors.blue),('TEXTCOLOR',(1,1),(0,-1),colors.blue), ('FONTSIZE',(0,0),(-1,-1),8)])

        tabla.setStyle([('TEXTCOLOR',(4,1),(-1,-1),colors.red)])

        #Y la asignamos al platypus story.

        story.append(tabla)

        #Damos color de fondo a las cabeceras.

        tabla.setStyle([('BACKGROUND',(0,0),(4,0),colors.gray)])

        #Creamos una caja alrededor de las celdas.

        tabla.setStyle([('BOX',(0,0),(-1,-1),0.25,colors.black)])

        #Y ponemos una malla (rejilla) a la tabla.

        tabla.setStyle([('INNERGRID',(0,0),(-1,-1),0.25,colors.black), ('VALIGN',(0,1),(-1,-1),'TOP')])

        #Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.

        now=datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H%M%S")

        if comision:
            name = "FormaUnica_ComServ-%s-%s.pdf" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()
        else:
            name = "FormaUnica_HorasyFijos-%s-%s.pdf" % (date_str, os.getpid())
            temp = tempfile.NamedTemporaryFile(prefix = name, suffix = '.pdf', dir='temp',)
            temp.close()

        #Creamos un DocTemplate en una hoja CARTA, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc = SimpleDocTemplate(temp.name, pagesize = letter, showBoundary = 1)
        doc.build(story)

        self.open_report(temp.name)
        self.tempFile=temp.name

    def open_report(self,path):

        try:
            if os.name == 'posix':
                os.popen('evince %s'% path)
            else:
                os.startfile(path)
        except:
            print sys.exc_value
            print sys.exc_type


