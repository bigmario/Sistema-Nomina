#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Manejo de Base de Datos Sqlite3 (MODELO)
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 18 de Mayo de 2012
#
# +-------------------------------------------------+#
###########################################################################

import sqlite3

class ModeloBD:

    def __init__(self):
        self.conectar()

    def conectar(self):
        """
        Conecta con la Base de daos
        """
        self.cnn = sqlite3.connect('database/BDnomina.db')
        self.cnn.row_factory = sqlite3.Row
        self.cursor = self.cnn.cursor()

    def CrearBD(self):
        """
        Crea la Base de Datos
        """
        try:
            query = open('SQL/BDNomina - MEJORADO.sql', 'r').read()
            self.conectar()
            if self.cursor.executescript(query):
                mensajeExito=wx.MessageDialog(self,'Base de Datos Creada Exitosamente',"Creando Base de Datos", wx.OK|wx.ICON_HAND)
                mensajeExito.ShowModal()
        except sqlite3.Error, e:
            self.cnn.rollback()
            mensajeError=wx.MessageDialog(self,'La Base de Datos no pudo ser Creada \n\nError: %s'%e,"Error en Base de Datos", wx.OK|wx.ICON_HAND)
            mensajeError.ShowModal()
        finally:
            self.desconectar()

    def verificaUsuario(self, usuario, hashClave):
        """
        Verifica si el usuario esta registrado
        """
        self.conectar()
        self.cursor.execute("""SELECT idadmin, loginadmin, passadmin FROM admin WHERE loginadmin=? and passadmin=?""",(usuario, hashClave))
        sesion=self.cursor.fetchone()
        self.desconectar()
        return sesion

    def CambiarClave(self, clave_actual, clave_nueva, conf_clave_nueva):
        """
        Cambia la Contrasena
        """
        self.conectar()
        try:
            if clave_nueva==conf_clave_nueva:
                self.cursor.execute("""UPDATE admin SET passadmin=? WHERE passadmin=?""",(clave_nueva, clave_actual))
                self.cnn.commit()
                return True
            else:
                return False
        except sqlite3.Error:
            self.cnn.rollback()
            return False
        finally:
            self.desconectar()

    def ContarRegistrosAdmin(self):
        """
        Cuenta los registros en la base de datos de administrador
        """
        self.conectar()
        self.cursor.execute("""SELECT COUNT(*) FROM admin""")
        resultado=self.cursor.fetchone()
        numero=resultado[0]
        self.desconectar()
        return numero

    def desconectar(self):
        """
        Desconecta de la base de datos
        """
        self.cursor.close()
        self.cnn.close()

    def agregarAdmin(self, nombreUsuario, passwd):
        """
        Agrega administrador a la aplicacion
        """
        self.conectar()
        try:
            self.cursor.execute("""INSERT INTO admin(loginadmin, passadmin) VALUES (?,?)""", (nombreUsuario, passwd))
            self.cnn.commit()
        except sqlite3.Error:
            self.cnn.rollback()
        finally:
            self.desconectar()

    def agregarProfesor(self, nombre, apellido, cedula, fechaNacimiento, telefono, fechaIngreso, email, listacatedras, activo,tipoProf, horasTotales, listadias, observacion, listaHoraEntradaM, listaHoraSalidaM, listaHoraEntradaT, listaHoraSalidaT, horasManana, horasTarde):
        """
        Agrega profesores a la base de datos
        """
        self.conectar()
        self.cursor.execute("""INSERT INTO profesor (nombreprofesor, apellidoprofesor, ciprofesor, fechanacimiento, telefonoprofesor, email, activoprofesor, tipoprofesor) VALUES (?,?,?,?,?,?,?,?)""", (nombre, apellido, cedula, fechaNacimiento, telefono, email, activo, tipoProf))

        contadorDias=0

        for dia in listadias:
            if (listaHoraEntradaM[contadorDias] != '00:00:00' and listaHoraSalidaM[contadorDias] != '00:00:00') or (listaHoraEntradaT[contadorDias] != '00:00:00' and listaHoraSalidaT[contadorDias] != '00:00:00'):
                self.cursor.execute("""INSERT INTO dias ( profesor_ciprofesor, fechaingreso, catedra_idcatedra, dia, horaentradamanana, horasalidamanana, horaentradatarde, horasalidatarde, horasmanana, horastarde, horaslaborales, observaciones ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (cedula, fechaIngreso, listacatedras[contadorDias], dia, listaHoraEntradaM[contadorDias], listaHoraSalidaM[contadorDias], listaHoraEntradaT[contadorDias], listaHoraSalidaT[contadorDias], horasManana[contadorDias], horasTarde[contadorDias], horasTotales[contadorDias], observacion[contadorDias]))
            contadorDias=contadorDias+1

        self.cnn.commit()
        self.desconectar()

    def modificarProfesorSinHorario(self, idEditar, nombre, apellido, cedula, fechaNacimiento, telefono, email, activo,tipoProf):
        """
        Modifica profesores en la base de datos
        """
        self.conectar()
        sql = """UPDATE profesor SET nombreprofesor=?, apellidoprofesor=?, ciprofesor=?, fechanacimiento=?, telefonoprofesor=?, email=?, activoprofesor=?, tipoprofesor=? WHERE ciprofesor=?"""
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute(sql,(nombre, apellido, cedula, fechaNacimiento, telefono, email, activo, tipoProf, idEditar))

        self.cnn.commit()
        self.desconectar()

    def modificarHorarioProfesor(self, idEditar, fechaIngreso, listacatedras, horasTotales, horasM, horasT, horaEntradaM, horaSalidaM, horaEntradaT, horaSalidaT, listadias, observ):
        """
        Modifica profesores en la base de datos
        """
        self.conectar()
        contadorDias=0

        for dia in listadias:
            if (horaEntradaM[contadorDias] != '00:00:00' and horaSalidaM[contadorDias] != '00:00:00') or (horaEntradaT[contadorDias] != '00:00:00' and horaSalidaT[contadorDias] != '00:00:00'):
                self.cursor.execute("""INSERT INTO dias ( profesor_ciprofesor, catedra_idcatedra, dia, horaentradamanana, horasalidamanana, horaentradatarde, horasalidatarde, horasmanana, horastarde, horaslaborales, observaciones, fechaingreso) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (idEditar, listacatedras[contadorDias], dia, horaEntradaM[contadorDias], horaSalidaM[contadorDias], horaEntradaT[contadorDias], horaSalidaT[contadorDias], horasM[contadorDias], horasT[contadorDias], horasTotales[contadorDias], observ[contadorDias], fechaIngreso))
            contadorDias=contadorDias+1

        self.cnn.commit()
        self.desconectar()

    def eliminarProfesor(self, id):
        """
        Elimina profesores de la base de datos
        """
        self.conectar()
        try:
            sql1 = """DELETE FROM profesor WHERE ciprofesor=?"""
            self.cursor.execute("PRAGMA foreign_keys = ON")
            self.cursor.execute(sql1, (id,))
            self.cnn.commit()
        except sqlite3.Error,e:
            print "Error eliminando Profesor %s"%e
            self.cnn.rollback()
        finally:
            self.desconectar()

    def listarProfesores(self):
        """
        Lista todos los profesores registrados
        """
        self.conectar()
        sql = """SELECT * FROM Profesor ORDER BY nombreprofesor"""
        self.cursor.execute(sql)
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

    def listarProfesoresReporte(self, comision):
        """
        Lista todos los profesores registrados
        """
        self.conectar()
        if comision:
            sql = """SELECT * FROM Profesor WHERE tipoprofesor=? ORDER BY nombreprofesor"""
            self.cursor.execute(sql, (1,))
        else:
            sql = """SELECT * FROM Profesor WHERE tipoprofesor=? OR tipoprofesor=? ORDER BY nombreprofesor"""
            self.cursor.execute(sql, (0, 2,))
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

    def buscarProfesor(self, nombre):
        """
        busca todos los datos de un profesor especifico enre  todos los registrados
        """
        self.conectar()
        sql="""SELECT * FROM profesor WHERE nombreprofesor like ? OR apellidoprofesor like ? OR ciprofesor like ?"""
        self.cursor.execute(sql, ('%'+unicode(nombre)+'%', '%'+unicode(nombre)+'%','%'+unicode(nombre)+'%',))
        prof= self.cursor.fetchall()
        self.desconectar()
        return prof

    def buscarID_Profesor(self, nombre=None):
        """
        busca el ID de un profesor especifico enre  todos los registrados
        """
        self.conectar()
        if nombre:
            sql="""SELECT DISTINCT ciprofesor FROM profesor WHERE ciprofesor = ?"""
            self.cursor.execute(sql, (nombre, ))
        else:
            sql="""SELECT DISTINCT ciprofesor FROM profesor"""
            self.cursor.execute(sql)
        prof= self.cursor.fetchone()
        self.desconectar()
        return prof

    def obtenerDatosProf(self, profesor):
        self.conectar()
        sql="""SELECT * FROM profesor WHERE ciprofesor = ?"""
        self.cursor.execute(sql, (profesor, ))
        datosProf= self.cursor.fetchone()
        self.desconectar()
        return datosProf

    def obtenerHoras(self):
        self.conectar()
        sql="""SELECT * FROM horas"""
        self.cursor.execute(sql)
        horaEntradaProf= self.cursor.fetchall()
        self.desconectar()
        return horaEntradaProf

    def obtenerHorasProf(self, idProfesor):
        self.conectar()
        sql="""SELECT horaentradamanana, horasalidamanana, horaentradatarde, horasalidatarde, horasmanana, horastarde, horaslaborales, fechaingreso FROM dias WHERE profesor_ciprofesor=?"""
        self.cursor.execute(sql, (idProfesor,))
        horasProf= self.cursor.fetchall()
        self.desconectar()
        return horasProf

    def obtenerHorasLaborales(self, idProfesor):
        self.conectar()
        sql="""SELECT horaslaborales FROM dias WHERE profesor_ciprofesor=?"""
        self.cursor.execute(sql, (idProfesor,))
        horasLab= self.cursor.fetchone()
        self.desconectar()
        return horasLab

    def obtenerObservDiarias(self, idProfesor):
        self.conectar()
        sql="""SELECT observaciones FROM dias WHERE profesor_ciprofesor=?"""
        self.cursor.execute(sql, (idProfesor,))
        observ= self.cursor.fetchall()
        self.desconectar()
        return observ

    def obtenerDiasLaborales(self, id_profesor):
        self.conectar()
        sql="""SELECT dia FROM dias WHERE profesor_ciprofesor=?"""
        self.cursor.execute(sql, (id_profesor,))
        dia= self.cursor.fetchall()
        self.desconectar()
        return dia

    def CargarAsistencia(self, horas, profesor, catedra, fecha_Asistencia, dia_asistencia_espanol, hora_Entrada, hora_Salida, observaciones):
        """
        Carga en Base de Datos la asistencia de un profesor
        """
        self.conectar()
        try:
            sql="""INSERT INTO asistencia (horasasistenciaprofesor, fechaasistencia, diaasistencia, horaentradaasistencia, horasalidaasistencia, observaciones, catedra_idcatedra, profesor_ciprofesor) VALUES (?,?,?,?,?,?,?,?)"""
            self.cursor.execute(sql, (horas, fecha_Asistencia, dia_asistencia_espanol, hora_Entrada, hora_Salida, observaciones, catedra, profesor))
            self.cnn.commit()
        except sqlite3.Error:
            self.cnn.rollback()
        finally:
            self.desconectar()

    def eliminarAsistencia(self, id, inicio, fin):
        """
        Elimina profesores de la base de datos
        """
        self.conectar()
        sql = """DELETE FROM asistencia WHERE profesor_ciprofesor=? AND fechaasistencia BETWEEN ? and ?"""

        self.cursor.execute(sql, (id,inicio, fin))
        self.cnn.commit()
        self.desconectar()

    def VerAsistencia(self, profesor, inicio, fin):
        """
        Carga en Base de Datos la asistencia de un profesor
        """
        self.conectar()
        sql="""SELECT horasasistenciaprofesor, fechaasistencia, diaasistencia, horaentradaasistencia, horasalidaasistencia, observaciones, catedra_idcatedra, profesor_ciprofesor FROM asistencia WHERE profesor_ciprofesor= ? AND fechaasistencia BETWEEN ? and ?"""
        self.cursor.execute(sql, (profesor,inicio,fin))
        asistencia = self.cursor.fetchall()
        self.desconectar()
        return asistencia

    def contarAsistencias(self, profesor, inicio, fin):
        """
        cuenta el numero de asistencias de un profesor en un lapso determinado
        """
        self.conectar()
        sql="""SELECT COUNT (fechaasistencia) FROM asistencia WHERE profesor_ciprofesor=? AND fechaasistencia BETWEEN ? and ?"""
        self.cursor.execute(sql, (profesor,inicio,fin))
        num_asistencias = self.cursor.fetchall()
        self.desconectar()
        return num_asistencias

    def CorregirAsistencia(self, numero_asistencias, listaFechasCorregidas, listaDiasCorregidas, listaIDCatedrasCoregidas, listaHorasEntradaCorregidas, listaHorasSalidaCorregidas, listaHorasCorregidas, listaObservacionesCorregidas, profesor):
        """
        Carga en Base de Datos la asistencia de un profesor
        """
        self.conectar()
        try:
            for i in range(numero_asistencias):
                #sql="""UPDATE asistencia SET horasasistenciaprofesor=?, fechaasistencia=?, diaasistencia=?, horaentradaasistencia=?, horasalidaasistencia=?, observaciones=?, catedra_idcatedra=?, profesor_ciprofesor=? WHERE profesor_ciprofesor=? and """
                sql="""INSERT INTO asistencia (horasasistenciaprofesor, fechaasistencia, diaasistencia, horaentradaasistencia, horasalidaasistencia, observaciones, catedra_idcatedra, profesor_ciprofesor) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
                self.cursor.execute(sql, (listaHorasCorregidas[i], listaFechasCorregidas[i], listaDiasCorregidas[i], listaHorasEntradaCorregidas[i], listaHorasSalidaCorregidas[i], listaObservacionesCorregidas[i], listaIDCatedrasCoregidas[i][0], profesor))
                self.cnn.commit()
        except sqlite3.Error:
            self.cnn.rollback()
        finally:
            self.desconectar()

    def listarID_CatedrasAsistencia(self, profesor):
        """
        Lista todos los catedras registrados
        """
        self.conectar()
        sql ="""SELECT DISTINCT nombrecatedra FROM catedra INNER JOIN dias WHERE dias.profesor_ciprofesor=? AND catedra.idcatedra = dias.catedra_idcatedra ORDER BY catedra_idcatedra"""
        #sql = """SELECT catedra_idcatedra FROM profesor_has_catedra WHERE profesor_ciprofesor=? ORDER BY catedra_idcatedra"""
        self.cursor.execute(sql,(profesor,))
        listadoIDS = self.cursor.fetchall()
        self.desconectar()
        return listadoIDS

    def listarCatedras(self):
        """
        Lista todos los catedras registrados
        """
        self.conectar()
        sql = """SELECT * FROM catedra ORDER BY idcatedra"""
        self.cursor.execute(sql)
        listado = self.cursor.fetchall()
        self.desconectar()
        return listado

    def CargarCatedras(self):
        self.conectar()
        lista_catedras=((1, u"VIOLíN"), (2, "VIOLA"), (3, "VIOLONCELLO"),
                                (4, "CONTRABAJO"), (5, "FLAUTA"), (6, "CLARINETE"),
                                (7, "OBOE"), (8, "FAGOTTE"), (9, "SAXOFON"), (10, "CORNO"),
                                (11, "TROMPETA"), (12, "TROMBON"), (13, "BOMBARDINO"),
                                (14, "TUBA"), (15, u"PERCUSIÓN"), (16, "PIANO PRINCIPAL"),
                                (17, u"CANTO LÍRICO"), (18, "LENGUAJE MUSICAL"),
                                (19, u"HISTORIA DE LA MÚSICA"), (20, u"ARMONÍA"),
                                (21, "CONTRAPUNTO"), (22, "PIANO COMPLEMENTARIO"),
                                (23, u"PIANO ACOMPAÑANTE"), (24, u"DIRECCIÓN ORQUESTAL"),
                                (25, u"BATERÍA"), (26, u"ARPA CRIOLLA"), (27,u"MARACAS"), (28,u"BAJO POPULAR"), (29, u"TALLERES DE VIOLíN"),
                                (30, "TALLERES DE VIOLA"), (31, "TLLERES DE VIOLONCELLO"),
                                (32, "TALLERES DE CONTRABAJO"), (33, "TALLERES DE FLAUTA"), (34, "TALLERES DE CLARINETE"),
                                (35, "TALLERES DE OBOE"), (36, "TALLERES DE FAGOTTE"), (37, "TALLERES DE SAXOFON"), (38, "TALLERES DE CORNO"),
                                (39, "TALERES DE TROMPETA"), (40, u"TALLERES DE TROMBÓN"), (41, "TALLERES DE BOMBARDINO"),
                                (42, "TALLERES DE TUBA"), (43, u"TALERES DE PERCUSIÓN"), (44, u"SECIONALES DE VIENTO-MADERA"), (45, "SECCIONALES DE VIENTO-METAL"),
                                (46, u"SECCIONALES DE PERCUSIÓN"), (47, "SECCIONALES DE CUERDAS"), (48, u"CLASES GRUPALES DE VIOLíN"),
                                (49, "CLASES GRUPALES DE VIOLA"), (50, "CLASES GRUPALES DE VIOLONCELLO"),
                                (51, "CLASES GRUPALES DE CONTRABAJO"), (52, "CLASES GRUPALES DE FLAUTA"), (53, "CLASES GRUPALES DE CLARINETE"),
                                (54, "CLASES GRUPALES DE OBOE"), (55, "CLASES GRUPALES DE FAGOTTE"), (56, "CLASES GRUPALES DE SAXOFON"), (57, "CLASES GRUPALES DE CORNO"),
                                (58, "CLASES GRUPALES DE TROMPETA"), (59, u"CLASES GRUPALES DE TROMBÓN"), (60, "CLASES GRUPALES DE BOMBARDINO"),
                                (61, "CLASES GRUPALES DE TUBA"), (62, u"CLASES GRUPALES DE PERCUSIÓN"), (63, u"BIG BAND"),
                                (64, u"ENSABLE DE VIOLíN"), (65, "ENSAMBLE DE VIOLA"), (66, "ENSAMBLE DE VIOLONCELLO"),
                                (67, "ENSAMBLE DE CONTRABAJO"), (68, "ENSAMBLE DE FLAUTA"), (69, "ENSAMBLE DE CLARINETE"),
                                (70, "ENSAMBLE DE OBOE"), (71, "ENSAMBLE DE FAGOTTE"), (72, "ENSAMBLE DE SAXOFON"), (73, "ENSAMBLE DE CORNO"),
                                (74, "ENSAMBLE DE TROMPETA"), (75, u"ENSAMBLE DE TROMBÓN"), (76, "ENSAMBLE DE BOMBARDINO"),
                                (77, "ENSAMBLE DE TUBA"), (78, u"ENSAMBLE DE PERCUSIÓN"), (79, u"FLAUTA DULCE"), (80, u"KINDER MUSICAL"), (81, u"CANTORÍA"),
                                (82, u"TÉCNICA VOCAL"),)
        self.cursor.execute("""DELETE FROM catedra""")
        self.cursor.executemany("""INSERT INTO catedra (idcatedra, nombrecatedra) VALUES (?,?);""", lista_catedras)
        self.cnn.commit()
        self.desconectar()

    def buscarID_catedra(self,nombre):
        """
        busca el ID de una catedra especifica enre  todas las registradas
        """
        self.conectar()
        sql="""SELECT idcatedra FROM catedra WHERE nombrecatedra = ?"""
        self.cursor.execute(sql, (nombre, ))
        cat= self.cursor.fetchone()
        self.desconectar()
        return cat

    def buscarIDCatedraDictada(self,idProf):
        """
        busca el ID de una catedra especifica enre  todas las registradas
        """
        self.conectar()
        sql="""SELECT catedra_idcatedra FROM dias WHERE profesor_ciprofesor = ?"""
        self.cursor.execute(sql, (idProf, ))
        cat= self.cursor.fetchall()
        self.desconectar()
        return cat

    def buscarNomCatedraDictada(self,idProf, rep=False, asistencia=False):
        """
        busca el nombre de una catedra especifica enre  todas las registradas
        """
        self.conectar()

        if not rep and not asistencia:
            sql="""SELECT nombrecatedra FROM catedra INNER JOIN dias WHERE dias.catedra_idcatedra = catedra.idcatedra AND dias.profesor_ciprofesor=?"""
            self.cursor.execute(sql, (idProf, ))
        elif rep and not asistencia:
            sql="""SELECT DISTINCT nombrecatedra FROM catedra INNER JOIN dias WHERE dias.catedra_idcatedra = catedra.idcatedra AND dias.profesor_ciprofesor=?"""
            self.cursor.execute(sql, (idProf, ))
        elif not rep and asistencia:
            sql="""SELECT nombrecatedra FROM catedra INNER JOIN asistencia WHERE asistencia.catedra_idcatedra = catedra.idcatedra AND asistencia.profesor_ciprofesor=?"""
            self.cursor.execute(sql, (idProf, ))
        cat= self.cursor.fetchall()
        self.desconectar()
        return cat

    def eliminarCatedras(self, id):
        """
        Elimina profesores de la base de datos
        """
        self.conectar()
        sql = """DELETE FROM dias WHERE profesor_ciprofesor=?"""

        self.cursor.execute(sql, (id,))
        self.cnn.commit()
        self.desconectar()

    def buscar_dia_Prof(self,idProf,ficha=False):
        """
        busca el dia de una catedra especifica enre  todas las registradas
        """
        self.conectar()
        if not ficha:
            #sql="""SELECT dia FROM dias WHERE profesor_ciprofesor = ? ORDER BY catedra_idcatedra"""
            sql="""SELECT dia FROM dias WHERE profesor_ciprofesor = ?"""
        else:
            sql="""SELECT dia FROM dias WHERE profesor_ciprofesor = ? ORDER BY dia"""
        self.cursor.execute(sql, (idProf, ))
        dias= self.cursor.fetchall()
        self.desconectar()
        return dias

    def formaUnicaProfesores(self,fecha_Inicio,fecha_Fin, comision):
        """
        crea un reporte unico de todos los profesores del nucleo
        """
        self.conectar()
        if comision:
            sql="""SELECT DISTINCT profesor.apellidoprofesor, profesor.nombreprofesor, profesor.ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE  asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND profesor.tipoprofesor=? AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY profesor.nombreprofesor ASC"""
            self.cursor.execute(sql, (1, fecha_Inicio,fecha_Fin,))
        else:
            sql="""SELECT DISTINCT profesor.apellidoprofesor, profesor.nombreprofesor, profesor.ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE  asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND (profesor.tipoprofesor = ? OR profesor.tipoprofesor = ?) AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY profesor.nombreprofesor ASC"""
            self.cursor.execute(sql, (0, 2, fecha_Inicio,fecha_Fin,))
        fUnica= self.cursor.fetchall()
        self.desconectar()
        return fUnica

    def reporteProfesor(self, cat, profesor,fecha_Inicio,fecha_Fin, comision):
        """
        crea un reporte de asistencia por catedra de todos los profesores del nucleo
        """
        self.conectar()
        if comision:
            sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND asistencia.profesor_ciprofesor=? AND asistencia.catedra_idcatedra=? AND profesor.tipoprofesor = ? AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
            self.cursor.execute(sql, (profesor, cat, 1, fecha_Inicio,fecha_Fin,))
        else:
            sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND asistencia.profesor_ciprofesor=? AND asistencia.catedra_idcatedra=? AND (profesor.tipoprofesor = ? OR profesor.tipoprofesor = ?) AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
            self.cursor.execute(sql, (profesor, cat, 0, 2, fecha_Inicio,fecha_Fin,))
        rep_Prof= self.cursor.fetchall()
        self.desconectar()
        return rep_Prof

    def reporteCatedras(self, catedra, ciprofesor,fecha_Inicio,fecha_Fin, comision, todos=False):
        """
        crea un reporte por catedra de todas las dictadas en el nucleo
        """
        self.conectar()
        if not todos:
            if comision:
                sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND asistencia.catedra_idcatedra=?  AND profesor.ciprofesor=? AND profesor.tipoprofesor = ? AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
                self.cursor.execute(sql, (catedra,ciprofesor, 1, fecha_Inicio,fecha_Fin,))
            elif not comision:
                sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND asistencia.catedra_idcatedra=?  AND profesor.ciprofesor=? AND (profesor.tipoprofesor = ? OR profesor.tipoprofesor = ?) AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
                self.cursor.execute(sql, (catedra,ciprofesor, 0, 2, fecha_Inicio,fecha_Fin,))
        else:
            if comision:
                sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND profesor.ciprofesor=? AND profesor.tipoprofesor = ? AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
                self.cursor.execute(sql, (ciprofesor, 1, fecha_Inicio,fecha_Fin,))
            elif not comision:
                sql="""SELECT DISTINCT * FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.profesor_ciprofesor=profesor.ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND profesor.ciprofesor=?  AND (profesor.tipoprofesor = ? OR profesor.tipoprofesor = ?) AND asistencia.fechaasistencia BETWEEN ? and ? ORDER BY asistencia.fechaasistencia"""
                self.cursor.execute(sql, (ciprofesor, 0, 2, fecha_Inicio,fecha_Fin,))
        rep_Cat= self.cursor.fetchall()
        self.desconectar()
        return rep_Cat

    def obtenerNombreCatedraX(self, cat):
        self.conectar()
        self.cursor.execute("""SELECT nombrecatedra FROM catedra WHERE idcatedra=?""", (cat,))
        nombreCatedraSeleccionada=self.cursor.fetchone()
        self.desconectar()
        return nombreCatedraSeleccionada

    def obtenerCatedraProf(self, prof):
        self.conectar()
        self.cursor.execute("""SELECT DISTINCT nombrecatedra  FROM dias JOIN profesor JOIN catedra WHERE dias.catedra_idcatedra=catedra.idcatedra AND dias.profesor_ciprofesor=profesor.ciprofesor AND dias.profesor_ciprofesor=?""", (prof,))
        nombreCatedra=self.cursor.fetchall()
        self.desconectar()
        return nombreCatedra

    def listarNomProfesoresCatedras(self, comision, catedra):
        """
        lista los  nombres de profesores por catedra con asistencia
        """
        self.conectar()
        if comision and catedra != 'todas':
            sql="""SELECT DISTINCT apellidoprofesor, nombreprofesor, ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE profesor.ciprofesor=asistencia.profesor_ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND catedra.idcatedra=? AND profesor.tipoprofesor=?"""
            self.cursor.execute(sql, (catedra, 1))
        elif not comision and catedra != 'todas':
            sql="""SELECT DISTINCT apellidoprofesor, nombreprofesor, ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE profesor.ciprofesor=asistencia.profesor_ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND catedra.idcatedra=? AND (profesor.tipoprofesor=? OR profesor.tipoprofesor=?)"""
            self.cursor.execute(sql, (catedra, 0, 2))
        elif comision and catedra == 'todas':
            sql="""SELECT DISTINCT apellidoprofesor, nombreprofesor, ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE profesor.ciprofesor=asistencia.profesor_ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND profesor.tipoprofesor=? ORDER BY catedra.idcatedra"""
            self.cursor.execute(sql, (1,))
        elif not comision and catedra == 'todas':
            sql="""SELECT DISTINCT apellidoprofesor, nombreprofesor, ciprofesor FROM profesor INNER JOIN catedra INNER JOIN asistencia WHERE profesor.ciprofesor=asistencia.profesor_ciprofesor AND catedra.idcatedra=asistencia.catedra_idcatedra AND (profesor.tipoprofesor=? OR profesor.tipoprofesor=?) ORDER BY catedra.idcatedra"""
            self.cursor.execute(sql, (0, 2))
        nomProfe= self.cursor.fetchall()
        self.desconectar()
        return nomProfe

    def listarNomProfesoresCatedrasDictadas(self, catedra):
        """
        lista los  nombres de profesores por catedra dictada
        """
        self.conectar()
        sql="""SELECT DISTINCT apellidoprofesor, nombreprofesor, ciprofesor FROM profesor INNER JOIN catedra INNER JOIN dias WHERE profesor.ciprofesor=dias.profesor_ciprofesor AND catedra.idcatedra=dias.catedra_idcatedra AND catedra.idcatedra=?"""
        self.cursor.execute(sql, (catedra,))
        nomProfe= self.cursor.fetchall()
        self.desconectar()
        return nomProfe

    def listarCatedrasDictadasProf(self, prof):
        """
        busca el ID de una catedra especifica enre  todas las registradas
        """
        self.conectar()
        sql="""SELECT DISTINCT * FROM catedra INNER JOIN profesor INNER JOIN profesor_has_catedra WHERE profesor_has_catedra.catedra_idcatedra=catedra.idcatedra AND profesor_has_catedra.profesor_idprofesor=profesor.idprofesor AND profesor.idprofesor=?"""
        self.cursor.execute(sql, (prof, ))
        catDictadas= self.cursor.fetchall()
        self.desconectar()
        return catDictadas

    def listarCatedrasasistenciaProf(self, prof):
        """
        listar las catedras con asistencia por profesor
        """
        self.conectar()
        sql="""SELECT DISTINCT nombrecatedra FROM catedra INNER JOIN asistencia WHERE asistencia.catedra_idcatedra=catedra.idcatedra AND asistencia.profesor_ciprofesor=?"""
        self.cursor.execute(sql, (prof, ))
        catDictadas= self.cursor.fetchall()
        self.desconectar()
        return catDictadas

    def listarCatedrasConAsistencia(self, comision, prof=None):
        """
        busca el ID de una catedra especifica enre  todas las registradas
        """
        self.conectar()
        if prof is not None:
            if comision:
                sql="""SELECT DISTINCT catedra.nombrecatedra, asistencia.catedra_idcatedra FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.catedra_idcatedra=catedra.idcatedra AND profesor.ciprofesor=asistencia.profesor_ciprofesor AND profesor.ciprofesor=? AND profesor.tipoprofesor=?"""
                self.cursor.execute(sql, (prof, 1))
            else:
                sql="""SELECT DISTINCT catedra.nombrecatedra, asistencia.catedra_idcatedra FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.catedra_idcatedra=catedra.idcatedra AND profesor.ciprofesor=asistencia.profesor_ciprofesor AND profesor.ciprofesor=? AND (profesor.tipoprofesor=? OR profesor.tipoprofesor=?)"""
                self.cursor.execute(sql, (prof, 0, 2))
        else:
            if comision:
                sql="""SELECT DISTINCT catedra.nombrecatedra, asistencia.catedra_idcatedra FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.catedra_idcatedra=catedra.idcatedra AND profesor.ciprofesor=asistencia.profesor_ciprofesor AND profesor.tipoprofesor=? ORDER BY catedra.idcatedra"""
                self.cursor.execute(sql, (1,))
            else:
                sql="""SELECT DISTINCT catedra.nombrecatedra, asistencia.catedra_idcatedra FROM asistencia INNER JOIN catedra INNER JOIN profesor WHERE asistencia.catedra_idcatedra=catedra.idcatedra AND profesor.ciprofesor=asistencia.profesor_ciprofesor AND (profesor.tipoprofesor=? OR profesor.tipoprofesor=?) ORDER BY catedra.idcatedra"""
                self.cursor.execute(sql, (0, 2))
        catDictadas= self.cursor.fetchall()
        self.desconectar()
        return catDictadas

    def sumarHorasDictadas(self, profesor, fecha_inicio=None, fecha_fin=None, catedra=None):
        """
        Suma el Total de horas trabajadas por catedra para cada profesor
        """
        self.conectar()
        if fecha_inicio and fecha_fin:
            if catedra:
                sql="""SELECT horasasistenciaprofesor FROM asistencia WHERE profesor_ciprofesor=? AND catedra_idcatedra=? AND fechaasistencia BETWEEN ? and ?"""
                self.cursor.execute(sql, (profesor, catedra, fecha_inicio, fecha_fin))
            else:
                 sql="""SELECT horasasistenciaprofesor FROM asistencia WHERE profesor_ciprofesor=? AND fechaasistencia BETWEEN ? and ?"""
                 self.cursor.execute(sql, (profesor, fecha_inicio, fecha_fin))
        else:
            if catedra:
                sql="""SELECT horasasistenciaprofesor FROM asistencia WHERE profesor_ciprofesor=? AND catedra_idcatedra=?"""
                self.cursor.execute(sql, (profesor, catedra))
            else:
                sql="""SELECT horasasistenciaprofesor FROM asistencia WHERE profesor_ciprofesor=?"""
                self.cursor.execute(sql, (profesor,))
        horas= self.cursor.fetchall()
        self.desconectar()

        horas2=[]
        for h in horas:
            horas2.append(h[0])

        total = 0
        for hora in horas2:
            h, m, s = map(int, hora.split(":"))
            total += 3600*h + 60*m + s

        horasTotales=("%02d:%02d:%02d" % (total / 3600, total / 60 % 60, total % 60), total)
        return horasTotales

    def configuracionInicial(self, nucleo, entFed, municipio, nombreAdmin, passAdmin, preguntaSeg, respuestaSeg):
        self.conectar()
        try:
            sql="""INSERT INTO admin (loginadmin, passadmin, nombrenucleo, entidadfederal, municipio, preguntaseg, respuestaseg) VALUES (?,?,?,?,?,?,?)"""
            self.cursor.execute(sql, (nombreAdmin, passAdmin, nucleo, entFed, municipio, preguntaSeg, respuestaSeg))
            self.cnn.commit()
            self.desconectar()
        except sqlite3.Error:
            self.cnn.rollback()

    def obtenerDatosNucleo(self):
        self.conectar()
        sql="""SELECT * FROM admin"""
        self.cursor.execute(sql)
        datosNucleo= self.cursor.fetchall()
        self.desconectar()
        return datosNucleo

    def recordarPass(self, pregunta, respuesta):
        self.conectar()
        sql="""SELECT loginadmin, passadmin FROM admin WHERE preguntaseg=? AND respuestaseg=?"""
        self.cursor.execute(sql, (pregunta, respuesta))
        passRecuperado=self.cursor.fetchone()
        self.desconectar()
        return passRecuperado

    def fichaProfesor(self, profesor=None, general=False):
        self.conectar()
        if profesor is not None and not general:
            sql="""SELECT DISTINCT *  FROM  dias JOIN catedra WHERE dias.profesor_ciprofesor=? AND catedra.idcatedra=dias.catedra_idcatedra ORDER BY dias.dia"""
            self.cursor.execute(sql, (profesor,))
        else:
            sql="""SELECT DISTINCT *  FROM  dias JOIN catedra WHERE catedra.idcatedra=dias.catedra_idcatedra ORDER BY dias.profesor_ciprofesor"""
            self.cursor.execute(sql)
        ficha=self.cursor.fetchall()
        self.desconectar()
        return ficha

    def calcularPromedioHoras(self, profesor, fecha_inicio, fecha_fin):
        self.conectar()
        sql="""SELECT horasasistenciaprofesor FROM asistencia WHERE profesor_ciprofesor=? AND fechaasistencia BETWEEN ? and ? """
        self.cursor.execute(sql, (profesor,fecha_inicio, fecha_fin))
        horas=self.cursor.fetchall()
        return horas

