#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo para Manejo General del Sistema (CONTROLADOR)
## Ultima Revisión: 19-11-2012 11:05 a.m
# +-------------------------------------------------+#
#
# Autor: Lic. Mario Castro
#
# Fecha: 18 de Mayo de 2012
#
# +-------------------------------------------------+#
###########################################################################

import wx
import wx.grid as  gridlib
import wx.lib.dialogs
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin
from wx.lib.wordwrap import wordwrap
import wx.lib.masked as masked

if wx.Platform == '__WXMSW__':
    from wx.lib.pdfwin import PDFWindow

import sys
import os
import hashlib
import sqlite3 as lite
from report import Reportes
from nomina_vista import (FrameLogin, FramePrincipal, FrameEliminarProf, PanelBienvenida,PanelCarga,
                                         PanelEdicion,PanelAsistencia,FrameReporteProfesor, FrameReporteCatedras,
                                         FrameFormaUnica, WizardConfigInicial, FrameRecuerdaPass, FrameFichaProfesor,
                                         FrameFichaGeneral, FrameProyeccion, FrameCoreccionAsistencia, Frame_CambioContrasena)

from nomina_vista import (ID_CARGAR_ASISTENCIA,
                                        ID_CORREGIR_ASISTENCIA,
                                        ID_CARGAR_PROFESOR,
                                        ID_EDITAR_PROFESORES,
                                        ID_ELIMINAR_PROFESORES,
                                        ID_FORMA_UNICA,
                                        ID_REPORTE_POR_PROFESOR,
                                        ID_REPORTE_POR_CTEDRA,
                                        ID_FORMA_UNICA_CS,
                                        ID_REPORTE_POR_PROFESOR_CS,
                                        ID_REPORTE_POR_CTEDRA_CS,
                                        ID_FICHA_POR_PROFESOR,
                                        ID_FICHA_GENERAL,
                                        ID_CLCULO_DE_PROYECCIN,
                                        ID_ACERCA_DE,
                                        ID_LICENCIA)

from modelo import ModeloBD

from datetime import datetime, date, timedelta
import time
import string
import logging
import traceback

try:
    dirName = os.path.dirname(os.path.abspath(__file__))
except:
    dirName = os.path.dirname(os.path.abspath(sys.argv[0]))

tempDir=os.path.relpath(os.path.join(dirName, 'temp'))
bitmapDir = os.path.relpath(os.path.join(dirName, 'bitmaps'))
iconDir=os.path.relpath(os.path.join(dirName, 'icon'))
licenceDir=os.path.relpath(os.path.join(dirName, 'license'))
sys.path.append(os.path.split(dirName)[0])
padding = 5

#######################
######DEFINICION DE CLASES
#######################

class DatePickerCtrl(wx.DatePickerCtrl):
    """
    Hace un Override de la Superclase para Cambiar el color de fondo del control
    """
    def __init__(self, *args, **kw):
        wx.DatePickerCtrl.__init__(self, *args, **kw)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    """
    Mixin de ListCtrl para presentar un Checkbox en cada fila
    """
    def __init__(self, parent):
        wx.ListCtrl.__init__( self, parent, -1, size=(-1,165), style=wx.LC_REPORT )
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

class RecuerdaPass(FrameRecuerdaPass):
    """
    Clase para recuperar contraseñas
    """

    def txtRespPreguntaSegOnTextEnter( self, event ):
        self.mostrarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())

    def mostrarPass(self, pregunta, respuesta):
        passRecuperado=app.BD.recordarPass(pregunta, respuesta)
        if not passRecuperado==None:
            mensaje=wx.MessageDialog(self,u'Nombre de usuario y Contraseña Recuperados:\n\nNombre de Usuario: %s\n\nContraseña: %s'%(passRecuperado[0], passRecuperado[1]),u"Recuperando Contraseña", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Respuesta Incorrecta',u"Recuperando Contraseña", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnAcettarRecuerdaPassOnButtonClick( self, event ):
       self.mostrarPass(self.choicePreguntaSeg.GetStringSelection(), self.txtRespPreguntaSeg.GetValue())

    def btnCancelRecuerdaPassOnButtonClick( self, event ):
        self.Close()

class CambioContrasena(Frame_CambioContrasena):

    def txt_ConfirmaContrasenaNueva_CambioOnTextEnter(self, event):
        self.CambiarContrasena()

    def btnCambioContrasenaOnButtonClick( self, event ):
        self.CambiarContrasena()

    def CambiarContrasena(self):
        self.clave_actual=self.txt_contrasenaActual_Cambio.GetValue()
        hashClaveActual = hashlib.md5()
        hashClaveActual.update(self.clave_actual)

        self.clave_nueva=self.txt_contrasenaNueva_Cambio.GetValue()
        hashClaveNueva = hashlib.md5()
        hashClaveNueva.update(self.clave_nueva)

        self.conf_clave_nueva=self.txt_ConfirmaContrasenaNueva_Cambio.GetValue()
        hashConfClaveNueva = hashlib.md5()
        hashConfClaveNueva.update(self.conf_clave_nueva)

        if app.BD.CambiarClave(self.clave_actual,self.clave_nueva,self.conf_clave_nueva):
            mensaje=wx.MessageDialog(self,u'Contraseña Modificada',u"Cambiando Contraseña", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.Close()
        else:
            mensaje=wx.MessageDialog(self,u'Contraseña NO Modificada',u"Cambiando Contraseña", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.Close()

    def btnCancelaCambioContrasenaOnButtonClick( self, event ):
        self.Close()

    def Frame_CambioContrasenaOnClose(self, event):
        self.MakeModal(False)
        self.Destroy()

class WizardInicio(WizardConfigInicial):
    """
    Clase para presentar el Wizard de Confifuracion inicial
    """

    def choiceEntFedOnChoice( self, event ):
        self.choiceMunicipio.Clear()

        if self.choiceEntFed.GetSelection() == 1:
            #capital
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Libertador (Caracas)")


        if self.choiceEntFed.GetSelection() == 2:
            #amazonas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Alto Orinoco (La Esmeralda)")
            self.choiceMunicipio.Append("Atabapo (San Fernando de Atabapo)")
            self.choiceMunicipio.Append("Atures (Puerto Ayacucho)")
            self.choiceMunicipio.Append(u"Autana (Isla Ratón)")
            self.choiceMunicipio.Append("Manapiare (San Juan de Manapiare)")
            self.choiceMunicipio.Append("Maroa (Maroa)")
            self.choiceMunicipio.Append(u"Río Negro (San Carlos de Río Negro)")


        if self.choiceEntFed.GetSelection() == 3:
            #anzoategui
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Anaco (Anaco)")
            self.choiceMunicipio.Append("Aragua (Aragua de Barcelona)")
            self.choiceMunicipio.Append(u"Bolívar (Barcelona)")
            self.choiceMunicipio.Append("Bruzual (Clarines)")
            self.choiceMunicipio.Append("Cajigal (Onoto)")
            self.choiceMunicipio.Append("Carvajal (Valle de Guanape)")
            self.choiceMunicipio.Append(u"Diego Bautista Urbaneja (Lechería)")
            self.choiceMunicipio.Append("Freites (Cantaura)")
            self.choiceMunicipio.Append(u"Guanipa (San José de Guanipa)")
            self.choiceMunicipio.Append("Guanta (Guanta)")
            self.choiceMunicipio.Append("Independencia (Soledad)")
            self.choiceMunicipio.Append("Libertad (San Mateo)")
            self.choiceMunicipio.Append("McGregor (El Chaparro)")
            self.choiceMunicipio.Append(u"Miranda (Pariaguán)")
            self.choiceMunicipio.Append("Monagas (San Diego de Cabrutica)")
            self.choiceMunicipio.Append(u"Peñalver (Puerto Píritu)")
            self.choiceMunicipio.Append(u"Píritu (Píritu)")
            self.choiceMunicipio.Append("San Juan de Capistrano (Boca de Uchire)")
            self.choiceMunicipio.Append("Santa Ana (Santa Ana)")
            self.choiceMunicipio.Append(u"Simón Rodriguez (El Tigre)")
            self.choiceMunicipio.Append("Sotillo (Puerto La Cruz)")


        if self.choiceEntFed.GetSelection() == 4:
            #apure
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Achaguas (Achaguas)" )
            self.choiceMunicipio.Append("Biruaca (Biruaca)")
            self.choiceMunicipio.Append(u"Muñoz (Bruzual)")
            self.choiceMunicipio.Append(u"Páez (Guasdualito)")
            self.choiceMunicipio.Append("Pedro Camejo (San Juan de Payara)")
            self.choiceMunicipio.Append(u"Rómulo Gallegos (Elorza)")
            self.choiceMunicipio.Append("San Fernando (San Fernando de Apure)")



        if self.choiceEntFed.GetSelection() == 5:
            #aragua
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Bolívar (San Mateo)")
            self.choiceMunicipio.Append("Camatagua (Camatagua)")
            self.choiceMunicipio.Append(u"Francisco Linares Alcántara (Santa Rita)")
            self.choiceMunicipio.Append("Girardot (Maracay)")
            self.choiceMunicipio.Append(u"José Angel Lamas (Santa Cruz de Aragua)")
            self.choiceMunicipio.Append(u"José Félix Ribas (La Victoria)")
            self.choiceMunicipio.Append(u"José Rafael Revenga (El Consejo)")
            self.choiceMunicipio.Append("Libertador (Palo Negro)")
            self.choiceMunicipio.Append(u"Mario Briceño Iragorry (El Limón)")
            self.choiceMunicipio.Append("San Casimiro (San Casimiro)")
            self.choiceMunicipio.Append(u"San Sebastián (San Sebastián de Los Reyes (Venezuela))")
            self.choiceMunicipio.Append(u"Santiago Mariño (Turmero)")
            self.choiceMunicipio.Append(u"Santos Michelena (Las Tejerías)")
            self.choiceMunicipio.Append("Sucre (Cagua)")
            self.choiceMunicipio.Append("Tovar (Colonia Tovar)")
            self.choiceMunicipio.Append("Urdaneta (Barbacoas)")
            self.choiceMunicipio.Append("Zamora (Villa de Cura)")


        if self.choiceEntFed.GetSelection() == 6:
            #barinas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Alberto Arvelo Torrealba (Sabaneta)")
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (El Cantón)")
            self.choiceMunicipio.Append(u"Antonio José de Sucre (Socopó)")
            self.choiceMunicipio.Append("Arismendi (Arismendi)")
            self.choiceMunicipio.Append("Barinas (Barinas)")
            self.choiceMunicipio.Append("Bolívar (Barinitas)")
            self.choiceMunicipio.Append("Cruz Paredes (Barrancas)")
            self.choiceMunicipio.Append(u"Ezequiel Zamora (Santa Bárbara)")
            self.choiceMunicipio.Append("Obispos (Obispos)")
            self.choiceMunicipio.Append("Pedraza (Ciudad Bolivia)")
            self.choiceMunicipio.Append("Rojas (Libertad)")
            self.choiceMunicipio.Append("Sosa (Ciudad de Nutrias)")


        if self.choiceEntFed.GetSelection() == 7:
            #bolivar
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Caroní (Ciudad Guayana)" )
            self.choiceMunicipio.Append(u"Cedeño (Caicara del Orinoco)")
            self.choiceMunicipio.Append("El Callao (El Callao)" )
            self.choiceMunicipio.Append(u"Gran Sabana (Santa Elena de Uairén)")
            self.choiceMunicipio.Append(u"Heres (Ciudad Bolívar))" )
            self.choiceMunicipio.Append("Piar (Upata)")
            self.choiceMunicipio.Append(u"Raúl Leoni (Ciudad Piar)" )
            self.choiceMunicipio.Append("Roscio (Guasipati)")
            self.choiceMunicipio.Append("Sifontes (El Dorado)" )
            self.choiceMunicipio.Append("Sucre (Maripa)")
            self.choiceMunicipio.Append("Padre Pedro Chien (El Palmar)" )


        if self.choiceEntFed.GetSelection() == 8:
            #carabobo
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Bejuma (Bejuma)")
            self.choiceMunicipio.Append("Carlos Arvelo (G\u00FCig\u00FCe)")
            self.choiceMunicipio.Append("Diego Ibarra (Mariara)")
            self.choiceMunicipio.Append("Guacara (Guacara)")
            self.choiceMunicipio.Append(u"Juan José Mora (Morón)")
            self.choiceMunicipio.Append("Libertador (Tocuyito)")
            self.choiceMunicipio.Append("Los Guayos (Los Guayos)")
            self.choiceMunicipio.Append("Miranda (miranda)")
            self.choiceMunicipio.Append(u"Montalbán (Montalbán)")
            self.choiceMunicipio.Append("Naguanagua (Naguanagua)")
            self.choiceMunicipio.Append("Puerto Cabello (Puerto Cabello)")
            self.choiceMunicipio.Append("San Diego")
            self.choiceMunicipio.Append(u"San Joaquín (San Joaquín)")
            self.choiceMunicipio.Append("Valencia (Valencia)")


        if self.choiceEntFed.GetSelection() == 9:
            #cojedes
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Anzoátegui (cojedes)")
            self.choiceMunicipio.Append(u"Falcón (Tinaquillo)" )
            self.choiceMunicipio.Append("Girardot (El Baúl)")
            self.choiceMunicipio.Append("Lima Blanco (Macapo)")
            self.choiceMunicipio.Append("Pao de San Juan Bautista (El Pao)")
            self.choiceMunicipio.Append("Ricaurte (Libertad)")
            self.choiceMunicipio.Append(u"Rómulo Gallegos (Las Vegas)")
            self.choiceMunicipio.Append("San Carlos (San Carlos)")
            self.choiceMunicipio.Append("Tinaco (Tinaco)")


        if self.choiceEntFed.GetSelection() == 10:
            #delta
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Antonio Díaz (Curiapo)" )
            self.choiceMunicipio.Append("Casacoima (Sierra Imataca)")
            self.choiceMunicipio.Append("Pedernales (Pedernales)")
            self.choiceMunicipio.Append("Tucupita (Tucupita)")


        if self.choiceEntFed.GetSelection() == 11:
            #falcon
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acosta (San Juan de los Cayos)")
            self.choiceMunicipio.Append(u"Bolívar (San Luis)")
            self.choiceMunicipio.Append("Buchivacoa (Capatárida)")
            self.choiceMunicipio.Append("Cacique Manaure (Yaracal)")
            self.choiceMunicipio.Append("Carirubana (Punto Fijo)")
            self.choiceMunicipio.Append("Colina (La Vela de Coro)")
            self.choiceMunicipio.Append("Dabajuro (Dabajuro)")
            self.choiceMunicipio.Append("Democracia (Pedregal)")
            self.choiceMunicipio.Append(u"Falcón (Pueblo Nuevo)")
            self.choiceMunicipio.Append("Federación (Churuguara)")
            self.choiceMunicipio.Append("Jacura (Jacura)")
            self.choiceMunicipio.Append("Los Taques (Santa Cruz de Los Taques)")
            self.choiceMunicipio.Append("Mauroa (Mene de Mauroa)")
            self.choiceMunicipio.Append("Miranda (Santa Ana de Coro)")
            self.choiceMunicipio.Append("Monseñor Iturriza (Chichiriviche)")
            self.choiceMunicipio.Append("Palmasola (Palmasola)")
            self.choiceMunicipio.Append("Petit (Cabure)")
            self.choiceMunicipio.Append(u"Píritu (Píritu)")
            self.choiceMunicipio.Append("San Francisco (Mirimire)")
            self.choiceMunicipio.Append("Silva (Tucacas)")
            self.choiceMunicipio.Append("Sucre (La Cruz de Taratara)")
            self.choiceMunicipio.Append("Tocópero (Tocópero)")
            self.choiceMunicipio.Append(u"Unión (Santa Cruz de Bucaral)")
            self.choiceMunicipio.Append("Urumaco (Urumaco)")


        if self.choiceEntFed.GetSelection() == 12:
            #guarico
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Camaguán (Camaguán).")
            self.choiceMunicipio.Append("Chaguaramas (Chaguaramas)" )
            self.choiceMunicipio.Append("El Socorro (El Socorro)" )
            self.choiceMunicipio.Append("Sebastian Francisco de Miranda (Calabozo)" )
            self.choiceMunicipio.Append(u"José Félix Ribas (Tucupido)" )
            self.choiceMunicipio.Append(u"José Tadeo Monagas (Altagracia de Orituco)" )
            self.choiceMunicipio.Append(u"Juan Germán Roscio (San Juan de Los Morros)" )
            self.choiceMunicipio.Append(u"Julián Mellado (El Sombrero)" )
            self.choiceMunicipio.Append("Las Mercedes (Las Mercedes)" )
            self.choiceMunicipio.Append("Leonardo Infante (Valle de La Pascua)" )
            self.choiceMunicipio.Append("Pedro Zaraza (Zaraza)" )
            self.choiceMunicipio.Append("Ortiz (Ortiz)" )
            self.choiceMunicipio.Append("San Gerónimo de Guayabal (Guayabal)" )
            self.choiceMunicipio.Append(u"San José de Guaribe (San José de Guaribe)" )
            self.choiceMunicipio.Append("Santa María de Ipire (Santa María de Ipire)" )


        if self.choiceEntFed.GetSelection() == 13:
            #lara
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (Sanare)" )
            self.choiceMunicipio.Append("Crespo (Duaca)")
            self.choiceMunicipio.Append("Iribarren (Barquisimeto)")
            self.choiceMunicipio.Append(u"Jiménez (Quibor)")
            self.choiceMunicipio.Append(u"Morán (El Tocuyo)")
            self.choiceMunicipio.Append("Palavecino (Cabudare)")
            self.choiceMunicipio.Append(u"Simón Planas (Sarare)")
            self.choiceMunicipio.Append("Torres (Carora)")


        if self.choiceEntFed.GetSelection() == 14:
            #merida
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Alberto Adriani (El Vigía)")
            self.choiceMunicipio.Append(u"Andrés Bello (La Azulita)")
            self.choiceMunicipio.Append("Antonio Pinto Salinas (Santa Cruz de Mora)")
            self.choiceMunicipio.Append("Aricagua (Aricagua)")
            self.choiceMunicipio.Append(u"Arzobispo Chacón (Canaguá)")
            self.choiceMunicipio.Append(u"Campo Elías (Ejido)")
            self.choiceMunicipio.Append("Caracciolo Parra Olmedo (Tucaní)")
            self.choiceMunicipio.Append("Cardenal Quintero (Santo Domingo)")
            self.choiceMunicipio.Append("Guaraque (Guaraque)")
            self.choiceMunicipio.Append(u"Julio César Salas (Arapuey)")
            self.choiceMunicipio.Append("Justo Briceño (Torondoy)")
            self.choiceMunicipio.Append("Libertador (Mérida)")
            self.choiceMunicipio.Append("Miranda (Timotes)")
            self.choiceMunicipio.Append("Obispo Ramos de Lora (Santa Elena de Arenales)")
            self.choiceMunicipio.Append("Padre Noguera (Santa María de Caparo)")
            self.choiceMunicipio.Append("Pueblo Llano (Pueblo Llano)")
            self.choiceMunicipio.Append("Rangel (Mucuchíes)")
            self.choiceMunicipio.Append("Rivas Dávila (Bailadores)")
            self.choiceMunicipio.Append("Santos Marquina (Tabay)")
            self.choiceMunicipio.Append("Sucre (Lagunillas)")
            self.choiceMunicipio.Append("Tovar (To)")
            self.choiceMunicipio.Append("Tulio Febres Cordero (Nueva bolivarvia)")
            self.choiceMunicipio.Append("Zea (Zea)")


        if self.choiceEntFed.GetSelection() == 15:
            #miranda
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acevedo (Caucagua)" )
            self.choiceMunicipio.Append(u"Andrés Bello (San José de Barlovento)")
            self.choiceMunicipio.Append("Baruta (Baruta)")
            self.choiceMunicipio.Append(u"Brión (Higuerote)")
            self.choiceMunicipio.Append("Buroz (Mamporal)")
            self.choiceMunicipio.Append("Carrizal (Carrizal)")
            self.choiceMunicipio.Append("Chacao (Chacao)")
            self.choiceMunicipio.Append(u"Cristóbal Rojas (Charallave)")
            self.choiceMunicipio.Append("El Hatillo (Santa Rosalía de Palermo)")
            self.choiceMunicipio.Append("Guaicaipuro (Los Teques)")
            self.choiceMunicipio.Append("Independencia (Santa Teresa del Tuy)")
            self.choiceMunicipio.Append("Lander (Ocumare del Tuy)")
            self.choiceMunicipio.Append("Los Salias (San Antonio de los Altos)a")
            self.choiceMunicipio.Append(u"Páez (Río Chico)")
            self.choiceMunicipio.Append(u"Páez Castillo (Santa Lucía)")
            self.choiceMunicipio.Append(u"Pedro Gual (Cúpira)")
            self.choiceMunicipio.Append("Plaza (Guarenas)")
            self.choiceMunicipio.Append(u"Simón Bolívar (San Francisco de Yare)")
            self.choiceMunicipio.Append("Sucre (Petare)")
            self.choiceMunicipio.Append(u"Urdaneta (Cúa)")
            self.choiceMunicipio.Append("Zamora (Guatire)")


        if self.choiceEntFed.GetSelection() == 16:
            #monagas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Acosta (San Antonio de Capayacuar)" )
            self.choiceMunicipio.Append("Aguasay (Aguasay)")
            self.choiceMunicipio.Append(u"Bolívar (Caripito)")
            self.choiceMunicipio.Append("Caripe (Caripe)")
            self.choiceMunicipio.Append("Cedeño (Caicara)")
            self.choiceMunicipio.Append("Ezequiel Zamora (Punta de Mata)")
            self.choiceMunicipio.Append("Libertador (Temblador)")
            self.choiceMunicipio.Append(u"Maturín (Maturín)")
            self.choiceMunicipio.Append(u"Piar (aragua de Maturín)")
            self.choiceMunicipio.Append("Punceres (Quiriquire)")
            self.choiceMunicipio.Append(u"Santa Bárbara (Santa Bárbara)")
            self.choiceMunicipio.Append("Sotillo (Barrancas del Orinco)")
            self.choiceMunicipio.Append("Uracoa (Uracoa)")


        if self.choiceEntFed.GetSelection() == 17:
            #nuevaEsparta
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Antolín del Campo (La Plaza de Paraguachí)")
            self.choiceMunicipio.Append("Arismendi (La Asunción)")
            self.choiceMunicipio.Append(u"Díaz (San Juan Bautista)")
            self.choiceMunicipio.Append(u"García (El Valle del Espíritu Santo)")
            self.choiceMunicipio.Append(u"Gómez (Santa Ana)")
            self.choiceMunicipio.Append("Maneiro (Pampatar)")
            self.choiceMunicipio.Append("Marcano (Juan Griego)")
            self.choiceMunicipio.Append(u"Mariño (Porlamar)")
            self.choiceMunicipio.Append(u"Península de Macanao (Boca de Río)")
            self.choiceMunicipio.Append("Tubores (Punta de Piedras)")
            self.choiceMunicipio.Append("Villalba (San Pedro de Coche)")


        if self.choiceEntFed.GetSelection() == 18:
            #portuguesa
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Agua Blanca (Agua Blanca)" )
            self.choiceMunicipio.Append("Araure (Araure)")
            self.choiceMunicipio.Append(u"Esteller (Píritu)")
            self.choiceMunicipio.Append("Guanare (Guanare)")
            self.choiceMunicipio.Append("Guanarito (Guanarito)")
            self.choiceMunicipio.Append(u"Monseñor José Vicente de Unda (Chabasquén de Unda)")
            self.choiceMunicipio.Append("Ospino (Ospino)")
            self.choiceMunicipio.Append(u"Páez (Acarigua)")
            self.choiceMunicipio.Append(u"Papelón (Papelón)")
            self.choiceMunicipio.Append(u"San Genaro de Boconoíto (Boconoíto)")
            self.choiceMunicipio.Append("San Rafael de Onoto (San Rafael de Onoto)")
            self.choiceMunicipio.Append(u"Santa Rosalía (El Playón)")
            self.choiceMunicipio.Append("Sucre (Biscucuy)")
            self.choiceMunicipio.Append(u"Turén (Villa Bruzual)")


        if self.choiceEntFed.GetSelection() == 19:
            #sucre
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Eloy Blanco (Casanay)" )
            self.choiceMunicipio.Append(u"Andrés Mata (San José de Aerocuar)")
            self.choiceMunicipio.Append("Arismendi (Río Caribe)")
            self.choiceMunicipio.Append(u"Benítez (El Pilar)")
            self.choiceMunicipio.Append(u"Bermúdez (Carúpano)")
            self.choiceMunicipio.Append(u"Bolívar (Marigï¿½itar)")
            self.choiceMunicipio.Append("Cajigal (Yaguaraparo)")
            self.choiceMunicipio.Append(u"Cruz Salmerón Acosta (Araya)")
            self.choiceMunicipio.Append("Libertador (Tunapuy)")
            self.choiceMunicipio.Append(u"Mariño (Irapa)")
            self.choiceMunicipio.Append(u"Mejía (San Antonio del Golfo)")
            self.choiceMunicipio.Append("Montes (Cumanacoa)")
            self.choiceMunicipio.Append("Ribero (Cariaco)")
            self.choiceMunicipio.Append(u"Sucre (Cumaná)")
            self.choiceMunicipio.Append(u"Valdez (Güiria)")


        if self.choiceEntFed.GetSelection() == 20:
            #tachira
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Bello (Cordero)" )
            self.choiceMunicipio.Append(u"Antonio Rómulo Costa (Las Mesas)")
            self.choiceMunicipio.Append(u"Ayacucho (Colón)")
            self.choiceMunicipio.Append(u"Bolívar (San Antonio del Táchira)")
            self.choiceMunicipio.Append(u"Cárdenas (Táriba)")
            self.choiceMunicipio.Append(u"Córdoba (Santa Ana de Táchira)")
            self.choiceMunicipio.Append(u"Fernández Feo (San Rafael del Piñal)")
            self.choiceMunicipio.Append(u"Francisco de Miranda (San José de Bolívar)")
            self.choiceMunicipio.Append(u"García de Hevia (La Fru00eda)")
            self.choiceMunicipio.Append(u"Guásimos (Palmira)")
            self.choiceMunicipio.Append("Independencia (Capacho Nuevo)")
            self.choiceMunicipio.Append(u"Jáuregui (La Grita)")
            self.choiceMunicipio.Append(u"José María gas (El Cobre)")
            self.choiceMunicipio.Append(u"Junín (Rubio)")
            self.choiceMunicipio.Append("Libertad (Capacho Viejo)")
            self.choiceMunicipio.Append("Libertador (Abejales)")
            self.choiceMunicipio.Append("Lobatera (Lobatera)")
            self.choiceMunicipio.Append("Michelena (Michelena)")
            self.choiceMunicipio.Append("Panamericano (Coloncito)")
            self.choiceMunicipio.Append(u"Pedro María Ureña (Ureña)")
            self.choiceMunicipio.Append("Rafael Urdaneta (Delicias)")
            self.choiceMunicipio.Append("Samuel Daru00edo Maldonado (La Tendida)")
            self.choiceMunicipio.Append(u"San Cristóbal (San Cristóbal)")
            self.choiceMunicipio.Append("Seboruco (Seboruco)")
            self.choiceMunicipio.Append(u"Simón Rodríguez (San Simón)")
            self.choiceMunicipio.Append("Sucre (Queniquea)")
            self.choiceMunicipio.Append("Torbes (San Josecito)")
            self.choiceMunicipio.Append("Uribante (Pregonero)")
            self.choiceMunicipio.Append("San Judas Tadeo (Umuquena)")


        if self.choiceEntFed.GetSelection() == 21:
            #trujillo
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Andrés Bello (Santa Isabel)" )
            self.choiceMunicipio.Append(u"Boconó (Boconó)")
            self.choiceMunicipio.Append(u"Bolívar (Sabana Grande)")
            self.choiceMunicipio.Append(u"Candelaria (Chejendé)")
            self.choiceMunicipio.Append("Carache (Carache)")
            self.choiceMunicipio.Append("Escuque (Escuque)")
            self.choiceMunicipio.Append(u"José Felipe Márquez Cañizalez (El Paradero)")
            self.choiceMunicipio.Append(u"Juan Vicente Campos Elías (Campo Elu00edas)")
            self.choiceMunicipio.Append("La Ceiba (Santa Apolonia)")
            self.choiceMunicipio.Append("Miranda (El Dividive)")
            self.choiceMunicipio.Append("Monte Carmelo (Monte Carmelo)")
            self.choiceMunicipio.Append(u"Motatán (Motatán)")
            self.choiceMunicipio.Append(u"Pampán (Pampán)")
            self.choiceMunicipio.Append("Pampanito (Pampanito)")
            self.choiceMunicipio.Append("Rafael Rangel (Betijoque)")
            self.choiceMunicipio.Append("San Rafael de Carvajal (Carvajal)")
            self.choiceMunicipio.Append("Sucre (Sabana de Mendoza)")
            self.choiceMunicipio.Append("Trujillo (Trujillo)")
            self.choiceMunicipio.Append("Urdaneta (La Quebrada)")
            self.choiceMunicipio.Append("Valera (Valera)")


        if self.choiceEntFed.GetSelection() == 22:
            #vargas
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Vargas (La Guaira)" )


        if self.choiceEntFed.GetSelection() == 23:
            #yaracuy
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append(u"Arístides Bastidas (San Pablo)" )
            self.choiceMunicipio.Append(u"Bolívar (Aroa)")
            self.choiceMunicipio.Append("Bruzual (Chivacoa)")
            self.choiceMunicipio.Append("Cocorote (Cocorote)")
            self.choiceMunicipio.Append("Independencia (Independencia)")
            self.choiceMunicipio.Append(u"José Antonio Páez (Sabana de Parra)")
            self.choiceMunicipio.Append("La Trinidad (Boraure)")
            self.choiceMunicipio.Append("Manuel Monge (Yumare)")
            self.choiceMunicipio.Append("Nirgua (Nirgua)")
            self.choiceMunicipio.Append(u"Peña (Yaritagua)")
            self.choiceMunicipio.Append("San Felipe (San Felipe)")
            self.choiceMunicipio.Append("Sucre (Guama)")
            self.choiceMunicipio.Append("Urachiche (Urachiche)")
            self.choiceMunicipio.Append("Veroes (Farriar)")


        if self.choiceEntFed.GetSelection() == 24:
            #zulia
            self.choiceMunicipio.Append('- - Seleccione un Municipio- -')
            self.choiceMunicipio.Append("Almirante Padilla (El Toro)" )
            self.choiceMunicipio.Append("Baralt (San Timoteo)")
            self.choiceMunicipio.Append("Cabimas (Cabimas)" )
            self.choiceMunicipio.Append("Catatumbo (Encontrados)")
            self.choiceMunicipio.Append(u"Colón (San Carlos del Zulia)" )
            self.choiceMunicipio.Append("Francisco Javier Pulgar (Pueblo Nuevo-El Chivo)")
            self.choiceMunicipio.Append(u"Jesús Enrique Losada (La Concepción)" )
            self.choiceMunicipio.Append(u"Jesús María Semprún (Casigua El Cubo)")
            self.choiceMunicipio.Append("La Cañada de Urdaneta (Concepción)" )
            self.choiceMunicipio.Append("Lagunillas (Ciudad Ojeda)")
            self.choiceMunicipio.Append(u"Machiques de Perijá (Machiques)" )
            self.choiceMunicipio.Append(u"Mara (San Rafael del Moján)")
            self.choiceMunicipio.Append("Maracaibo (Maracaibo)" )
            self.choiceMunicipio.Append("Miranda (Los Puertos de Altagracia)")
            self.choiceMunicipio.Append(u"Páez (Sinamaica)" )
            self.choiceMunicipio.Append(u"Rosario de Perijá (La Villa del Rosario)")
            self.choiceMunicipio.Append("San Francisco (San Francisco)" )
            self.choiceMunicipio.Append("Santa Rita (Santa Rita)")
            self.choiceMunicipio.Append(u"Simón Bolívar (Tu00eda Juana)" )
            self.choiceMunicipio.Append("Sucre (Bobures)")
            self.choiceMunicipio.Append("Valmore Rodríguez (Bachaquero)" )

        self.choiceMunicipio.SetSelection(0)

    def WizardConfigInicialOnWizardPageChanged(self, event):
        """
        Se Sobreescriben las etiquetas de los botones 'Next', 'Previous' y 'Finish'
        """
        cancel_btn = self.FindWindowById(wx.ID_CANCEL)
        cancel_btn.SetLabel("Cancelar")
        prev_btn = self.FindWindowById(wx.ID_BACKWARD)
        prev_btn.SetLabel("Anterior")
        next_btn = self.FindWindowById(wx.ID_FORWARD)
        if next_btn.GetLabel()=="&Finish":
            next_btn.SetLabel("Finalizar")
        else:
            next_btn.SetLabel("Siguiente")

    def WizardConfigInicialOnWizardPageChanging(self, event):
        """
        Validaciones al momento de cambiar de Pagina
        """
        page=event.GetPage()
        try:
            #si estamos en la pagina de datos de Usuario administrador
            if page==self.pagina1Wizard and event.GetDirection():
                self.nucleo=string.capwords(self.txtNucleo.GetValue())
                self.entfed=self.choiceEntFed.GetStringSelection()
                self.municipio=self.choiceMunicipio.GetStringSelection()

                if self.choiceEntFed.GetSelection() == 0 or self.choiceMunicipio.GetSelection() == 0 or self.nucleo == '':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.txtNucleo.Clear()
                    self.choiceEntFed.SetSelection(0)
                    self.choiceMunicipio.SetSelection(0)
                    event.Veto()
            elif page==self.pagina2Wizard and event.GetDirection():
                self.adminLogin=string.lower(self.txtUsuarioAdmin.GetValue())
                self.passAdmin=self.txtPassAdmin.GetValue()

                #se encripta la clave con MD5
                self.hashAdmin = hashlib.md5()
                self.hashAdmin.update(self.passAdmin)

                if self.passAdmin == '' or self.adminLogin == '':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.txtUsuarioAdmin.Clear()
                    self.txtPassAdmin.Clear()
                    event.Veto()
            elif page==self.pagina3Wizard and event.GetDirection():
                self.preguntaSeg=self.choicePreguntaSeg.GetStringSelection()
                self.respuestaSeg=self.txtRespuestaSeg.GetValue()

                if self.choicePreguntaSeg.GetSelection() == 0 or self.respuestaSeg == '':
                    mensaje=wx.MessageDialog(self,u'No deben haber Campos Vacios.\nIntente de Nuevo',"Agregando Administrador", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    self.choicePreguntaSeg.SetSelection(0)
                    self.txtRespuestaSeg.Clear()
                    event.Veto()
        except UnicodeEncodeError, e:
            #error, sacamos dialogo y decimos que hagan configuracion -- se crea un LOG del Error
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtPassAdmin.Clear()
            self.txtPassAdmin.SetFocus()
            event.Veto()


    def WizardConfigInicialOnWizardCancel( self, event ):
        pass

    def WizardConfigInicialOnWizardFinished( self, event ):
        try:
            BD=ModeloBD()

            BD.configuracionInicial(self.nucleo, self.entfed, self.municipio,self.adminLogin, self.passAdmin, self.preguntaSeg, self.respuestaSeg)
            #app.BD.configuracionInicial(self.nucleo, self.entfed, self.municipio,self.adminLogin, self.hashAdmin.hexdigest(), self.preguntaSeg, self.respuestaSeg)
            mensaje=wx.MessageDialog(self,u'Datos del Núcleo Agregados al Sistema',u"Agregando Datos del Núcleo", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

            self.frameInicio = FInicio(None)

            icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))
            favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
            wx.Frame.SetIcon(self.frameInicio, favicon)

            self.frameInicio.Show()
            self.frameInicio.txtNomUsuario.SetFocus()
        except lite.Error, e:
            #error, sacamos dialogo y decimos que hagan configuracion
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'Error en la conección a la base de Datos. \nIntente de nuevo o haga click en "Cancelar" para salir. \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNucleo.Clear()
            self.choiceEntFed.Clear()
            self.choiceMunicipio.Clear()
            self.txtUsuarioAdmin.Clear()
            self.txtPassAdmin.Clear()
            self.choicePreguntaSeg.SetSelection(0)
            self.txtRespuestaSeg.Clear()

class Proyeccion(FrameProyeccion):

    def FrameProyeccionOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def btnCancelarProyeccionProfesorOnButtonClick( self, event ):
        self.Close()

    def m_choiceProyeccionProfesorOnChoice(self, event):
        self.panelReportProy.Layout()

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None

        self.pdf = PDFWindow(self.panelReportProy)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelReportProy.SetSizer(sizer)
        self.panelReportProy.Layout()

    def btnCrearProyeccionProfesorOnButtonClick( self, event ):
        try:
            self.panelReportProy.Layout()
            profesor=self.listaCI_Prof[self.m_choiceProyeccionProfesor.GetCurrentSelection()-1]

            inicio=self.m_datePickerFechaInicioProy.GetValue().Format('%Y-%m-%d')
            fin=self.m_datePickerFechaFinProy.GetValue().Format('%Y-%m-%d')

            if inicio < fin:
                try:
                    if not self.m_choiceProyeccionProfesor.GetCurrentSelection()==0:
                        self.pdf.LoadFile(app.reporte.crearProyeccion(profesor, inicio, fin))
                        self.panelReportProy.Layout()
                        self.Layout()
                    else:
                        mensaje=wx.MessageDialog(self,u'Debe Escojer un Profesor',u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()
                except IOError, e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                    logging.error('%s - [%s]'%(e, trace))
                    mensaje=wx.MessageDialog(self,u'La Proyección solicitada NO fue Generada \n\n%s'%e,u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            else:
                mensaje=wx.MessageDialog(self,u'La Fecha de Fin debe ser Mayor que la Fecha de Inicio.\n',u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        except IndexError:
            #error, sacamos dialogo y decimos que hagan configuracion
            mensaje=wx.MessageDialog(self,u'No Hay ningún Profesor cargado en el Sistema. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def listarProfesores(self):

        self.m_choiceProyeccionProfesor.Clear()
        self.m_choiceProyeccionProfesor.Append(u"Seleccionar Profesor...")
        self.m_choiceProyeccionProfesor.SetSelection( 0 )

        profesores=app.BD.listarProfesores()

        self.listaID_Prof=[]
        self.listaCI_Prof=[]
        for profesor in profesores:
            self.m_choiceProyeccionProfesor.Append(profesor[1]+' '+profesor[2])
            self.listaCI_Prof.append(profesor[0])
            self.listaID_Prof.append(profesor[0])

class FrameFicha(FrameFichaProfesor):

    def FrameFichaProfesorOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None
        self.pdf = PDFWindow(self.panelReportFichaProf, style=wx.SUNKEN_BORDER)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelReportFichaProf.SetSizer(sizer)
        self.panelReportFichaProf.Layout()

    def btnCrearReporteProfesorFichaOnButtonClick( self, event ):
        try:
            self.panelReportFichaProf.Layout()
            if not self.m_choiceFichaProfesor.GetCurrentSelection()==0:
                self.pdf.LoadFile(app.reporte.CrearFichaProfesor(self.listaCI_Prof[self.m_choiceFichaProfesor.GetCurrentSelection()-1]))
                self.panelReportFichaProf.Layout()
                self.Layout()
            else:
                mensaje=wx.MessageDialog(self,u'Debe Escojer un Profesor',u"Error Creando Reporte", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        except IOError, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'El app.reporte de Profesor NO fue creado \n\n%s'%e,u"Error Creando Reporte", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def btnCancelarReporteProfesorFichaOnButtonClick( self, event ):
        self.Close()

    def listarProfesores(self):
        self.m_choiceFichaProfesor.Clear()
        self.m_choiceFichaProfesor.Append(u"Seleccionar Profesor...")
        self.m_choiceFichaProfesor.SetSelection( 0 )

        profesores=app.BD.listarProfesores()

        self.listaID_Prof=[]
        self.listaCI_Prof=[]
        for profesor in profesores:
            self.m_choiceFichaProfesor.Append(profesor[1]+' '+profesor[2])
            self.listaCI_Prof.append(profesor[0])
            self.listaID_Prof.append(profesor[0])

class FichaGeneral(FrameFichaGeneral):

    def FrameFichaGeneralOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None
        self.pdf = PDFWindow(self.panelReportFichaGen, style=wx.SUNKEN_BORDER)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelReportFichaGen.SetSizer(sizer)
        self.panelReportFichaGen.Layout()

    def btnCerrarFichaGenOnButtonClick( self, event ):
        self.Close()


class FormaUnica(FrameFormaUnica):
    """
    Subclase de FrameFormaUnica que muestra una Ventana para generar app.reporte - Forma Unica
    """

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None
        self.pdf = PDFWindow(self.panelFormaUnica, style=wx.SUNKEN_BORDER)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelFormaUnica.SetSizer(sizer)
        self.panelFormaUnica.Layout()

    def btnCancelarFormaUnicaOnButtonClick( self, event ):
        self.Close()

    def FrameFormaUnicaOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def m_checkBoxProyeccionFormaUnicaOnCheckBox(self, event):
        if self.m_checkBoxProyeccionFormaUnica.IsChecked():
            self.m_spinCtrlMeses_Proyectados.Enable(True)
        else:
            self.m_spinCtrlMeses_Proyectados.Enable(False)

    def btnCrearFormaUnicaOnButtonClick( self, event ):
        if self.datePickerFechaInicio.GetValue()<=self.datePickerFechaFin.GetValue():
            try:
                self.panelFormaUnica.Layout()
                if self.m_spinCtrlMeses_Proyectados.IsEnabled():
                    meses_proyectados=self.m_spinCtrlMeses_Proyectados.GetValue()
                else:
                    meses_proyectados=0
                self.pdf.LoadFile(app.reporte.CrearFormaUnica(self.datePickerFechaInicio.GetValue().Format('%Y-%m-%d').encode(), self.datePickerFechaFin.GetValue().Format('%Y-%m-%d').encode(), self.comision, self.m_checkBoxProyeccionFormaUnica.IsChecked(), meses_proyectados))
                self.panelFormaUnica.Layout()
                self.Layout
            except IOError, e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
                mensaje=wx.MessageDialog(self,u'La Forma Única NO fue creada \n\n%s'%e,u"Error Creando Forma Única", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'La Fecha de Inicio debe ser Menor a la Fecha de Fin',u"Creando Forma Única", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

class reporteProf(FrameReporteProfesor):
    """
    Subclase de FrameReporteProfesor que muestra una ventana para generar Reportes por Profesor
    """

    def FrameReporteCatedrasOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def btnCancelarReporteCatedrasOnButtonClick( self, event ):
        self.Close()

    def btnCrearReporteProfesorCatedrasOnButtonClick( self, event ):
        if self.datePickerFechaInicio.GetValue()<=self.datePickerFechaFin.GetValue():
            try:
                self.paneReporteProf.Layout()
                if not self.m_choiceProfesor.GetCurrentSelection()==0:
                    self.pdf.LoadFile(app.reporte.CrearReporteProf(self.listaCI_Prof[self.m_choiceProfesor.GetCurrentSelection()-1], self.datePickerFechaInicio.GetValue().Format('%Y-%m-%d').encode(), self.datePickerFechaFin.GetValue().Format('%Y-%m-%d').encode(), self.comision))
                    self.paneReporteProf.Layout()
                    self.Layout()
                else:
                    mensaje=wx.MessageDialog(self,u'Debe Escojer un Profesor',u"Error Creando Reporte", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            except IOError, e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
                mensaje=wx.MessageDialog(self,u'El Reporte de Profesor NO fue creado \n\n%s'%e,u"Error Creando Reporte", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'La Fecha de Inicio debe ser Menor a la Fecha de Fin',u"Creando Forma Única", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def listarProfesores(self):

        self.m_choiceProfesor.Clear()
        self.m_choiceProfesor.Append(u"Seleccionar Profesor...")
        self.m_choiceProfesor.SetSelection( 0 )

        profesores=app.BD.listarProfesoresReporte(self.comision)

        self.listaID_Prof=[]
        self.listaCI_Prof=[]
        for profesor in profesores:
            self.m_choiceProfesor.Append(profesor[1]+' '+profesor[2])
            self.listaCI_Prof.append(profesor[0])
            self.listaID_Prof.append(profesor[0])

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None
        self.pdf = PDFWindow(self.paneReporteProf, style=wx.SUNKEN_BORDER)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.paneReporteProf.SetSizer(sizer)
        self.paneReporteProf.Layout()


class reporteCat(FrameReporteCatedras):
    """
    Subclase de FrameReporteCatedras que muestra una ventana para generar Reportes por Catedra
    """

    def btnCancelarReporteProfOnButtonClick( self, event ):
        self.Close()

    def FrameReporteDocenteOnClose( self, event ):
        self.pdf.Destroy()
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def btnCrearReporteCatOnButtonClick( self, event ):
        if self.datePickerFechaInicio.GetValue()<=self.datePickerFechaFin.GetValue():
            try:
                self.panelReporteCat.Layout()
                if not self.m_choiceCatedraReporte.GetCurrentSelection() == 0 and not self.m_choiceCatedraReporte.GetCurrentSelection() == 1:
                    self.pdf.LoadFile(app.reporte.CrearReporteCatedra(self.listaID_catedras[self.m_choiceCatedraReporte.GetCurrentSelection()-2],self.datePickerFechaInicio.GetValue().Format('%Y-%m-%d').encode(), self.datePickerFechaFin.GetValue().Format('%Y-%m-%d').encode(), self.comision))
                    self.panelReporteCat.Layout()
                    self.Layout()
                elif self.m_choiceCatedraReporte.GetCurrentSelection() == 1:
                    self.pdf.LoadFile(app.reporte.CrearReporteCatedra('todas',self.datePickerFechaInicio.GetValue().Format('%Y-%m-%d').encode(), self.datePickerFechaFin.GetValue().Format('%Y-%m-%d').encode(), self.comision))
                    self.panelReporteCat.Layout()
                    self.Layout()
                else:
                    mensaje=wx.MessageDialog(self,u'Debe Escojer una Cátedra',u"Error Creando Reporte", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            except IOError, e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
                mensaje=wx.MessageDialog(self,u'El Reporte de Cátedra NO fue creado \n\n%s'%e,u"Error Creando Reporte", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'La Fecha de Inicio debe ser Menor a la Fecha de Fin',u"Creando Forma Única", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def listarCat( self ):
        self.m_choiceCatedraReporte.Clear()
        self.m_choiceCatedraReporte.Append(u"Seleccionar Cátedra...")
        self.m_choiceCatedraReporte.Append(u"Todas...")
        self.m_choiceCatedraReporte.SetSelection( 0 )

        catedras=app.BD.listarCatedras()

        self.listaID_catedras=[]
        for catedra in catedras:
            self.m_choiceCatedraReporte.Append(catedra[1])
            self.listaID_catedras.append(catedra[0])

    def iniciarPanelReporte(self):
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.pdf = None
        self.pdf = PDFWindow(self.panelReporteCat, style=wx.SUNKEN_BORDER)

        sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        self.panelReporteCat.SetSizer(sizer)
        self.panelReporteCat.Layout()


class NotEmptyValidator(wx.PyValidator):
    """
    Clase para definir un validador de entrada en los TextCtrl, en edicion y creacion de Profesores
    """

    def __init__(self):
        wx.PyValidator.__init__(self)
    def Clone(self):
        """
        Note that every validator must implement the Clone() method.
        """
        return NotEmptyValidator()

    def Validate(self, win):
        textCtrl = self.GetWindow()
        text = textCtrl.GetValue()
        if len(text) == 0 or text=='(    )    -    ' or text=='        ':
            textCtrl.SetBackgroundColour("pink")
            textCtrl.SetFocus()
            textCtrl.Refresh()
            return False
        else:
            textCtrl.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
            textCtrl.Refresh()
            return True
    def TransferToWindow(self):
        return True
    def TransferFromWindow(self):
        return True



class TimeCellEditorManana(wx.grid.PyGridCellEditor):
    """
    Clase destinada a crear un editor personalizado dentro de las Celdas de un Grid
    """

    def __init__(self):
        wx.grid.PyGridCellEditor.__init__(self)

    def Create(self, parent, id, evtHandler):
        self.timeHoraEntrada24 = TimeControlManana(parent,-1)
        self.timeHoraEntrada24.Start.SetInsertionPoint(0)
        self.SetControl(self.timeHoraEntrada24)
        if evtHandler:
            self.timeHoraEntrada24.PushEventHandler(evtHandler)
            self.timeHoraEntrada24.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnDClick)

    def BeginEdit(self, row, col, grid):
        self.startValue = grid.GetTable().GetValue(row, col)
        self.timeHoraEntrada24.Start.SetInsertionPointEnd()
        self.timeHoraEntrada24.Start.SetFocus()
        self.timeHoraEntrada24.Start.SetSelection(0, self.timeHoraEntrada24.Start.GetLastPosition())

    def EndEdit(self, row, col, grid, val):
        changed = False
        val = self.timeHoraEntrada24.Start.GetValue()
        if val != self.startValue:
            changed = True
            grid.GetTable().SetValue(row, col, val) # update the table

        self.startValue = '08:00:00'
        self.timeHoraEntrada24.Start.SetValue('08:00:00')

        return changed

    def Reset(self):
        self.timeHoraEntrada24.Start.SetValue(self.startValue)
        self.timeHoraEntrada24.Start.SetInsertionPointEnd()

    def Clone(self):
        return TimeCellEditorManana()

    def OnDClick(self, evt):
        if self.CanEnableCellControl():
           self.EnableCellEditControl()


class TimeCellEditorTarde(wx.grid.PyGridCellEditor):
    """
    Clase destinada a crear un editor personalizado dentro de las Celdas de un Grid
    """

    def __init__(self):
        wx.grid.PyGridCellEditor.__init__(self)

    def Create(self, parent, id, evtHandler):
        self.timeHoraEntrada24 = TimeControlTarde(parent,-1)
        self.timeHoraEntrada24.End.SetInsertionPoint(0)
        self.SetControl(self.timeHoraEntrada24)
        if evtHandler:
            self.timeHoraEntrada24.PushEventHandler(evtHandler)
            self.timeHoraEntrada24.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnDClick)

    def BeginEdit(self, row, col, grid):
        self.startValue = grid.GetTable().GetValue(row, col)
        self.timeHoraEntrada24.End.SetInsertionPointEnd()
        self.timeHoraEntrada24.End.SetFocus()
        self.timeHoraEntrada24.End.SetSelection(0, self.timeHoraEntrada24.End.GetLastPosition())

    def EndEdit(self, row, col, grid, val):
        changed = False
        val = self.timeHoraEntrada24.End.GetValue()
        if val != self.startValue:
            changed = True
            grid.GetTable().SetValue(row, col, val) # update the table

        self.startValue = '12:00:00'
        self.timeHoraEntrada24.End.SetValue('12:00:00')

        return changed

    def Reset(self):
        self.timeHoraEntrada24.End.SetValue(self.startValue)
        self.timeHoraEntrada24.End.SetInsertionPointEnd()

    def Clone(self):
        return TimeCellEditorTarde()

    def OnDClick(self, evt):
        if self.CanEnableCellControl():
           self.EnableCellEditControl()


class DateCellEditorAsistencia(wx.grid.PyGridCellEditor):
    """
    Clase destinada a crear un editor personalizado dentro de las Celdas de un Grid
    """

    def __init__(self):
        wx.grid.PyGridCellEditor.__init__(self)

    def Create(self, parent, id, evtHandler):
        self.fechaCorreccion = DateControlAsistencia(parent,-1)
        self.SetControl(self.fechaCorreccion)
        if evtHandler:
            self.fechaCorreccion.PushEventHandler(evtHandler)
            self.fechaCorreccion.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnDClick)

    def BeginEdit(self, row, col, grid):
        self.startValue = grid.GetTable().GetValue(row, col)
        self.fechaCorreccion.fecha.SetFocus()

    def EndEdit(self, row, col, grid, val):
        changed = False
        val = self.fechaCorreccion.fecha.GetValue().Format('%Y-%m-%d')
        if val != '':
            changed = True
            grid.GetTable().SetValue(row, col, val) # update the table

        return changed

    def Reset(self):
        self.fechaCorreccion.fecha.SetValue(self.startValue)
        self.fechaCorreccion.fecha.SetInsertionPointEnd()

    def Clone(self):
        return TimeCellEditorTarde()

    def OnDClick(self, evt):
        if self.CanEnableCellControl():
           self.EnableCellEditControl()


class DateControlAsistencia(wx.Control):
        """
        Clase creada para poder mostrar los TimeCtrl dentro de las Celdas de un Grid
        """

        def __init__(self, parent,id):
                wx.Control.__init__(self, parent, -1)

                self.fecha = wx.DatePickerCtrl(self, -1, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN)

                GridSizer = wx.BoxSizer( wx.HORIZONTAL )
                GridSizer.Add(self.fecha,0,wx.EXPAND)

                #this strange setup is needed because the gridsizer isn't layout correctly in the cell for some reason
                Sizer = wx.BoxSizer(wx.VERTICAL)
                Sizer.Add(GridSizer,0)

                Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
                Sizer2.Add(Sizer,0)

                self.SetSizer(Sizer2)
                self.Layout()


class TimeControlAsistencia(wx.Control):
        """
        Clase creada para poder mostrar los TimeCtrl dentro de las Celdas de un Grid
        """

        def __init__(self, parent,id):
                wx.Control.__init__(self, parent, -1)
                minStart="07:00:00"
                maxStart="19:00:00"

                spinStart = wx.SpinButton(self,-1,wx.DefaultPosition,wx.Size(-1,-1),0)

                self.StartAsistencia = masked.TimeCtrl(self, -1, name="24 hour control", fmt24hr=True,spinButton = spinStart)
                self.StartAsistencia.SetLimited(True)
                self.StartAsistencia.SetMin( minStart )
                self.StartAsistencia.SetMax( maxStart )

                GridSizer = wx.BoxSizer( wx.HORIZONTAL )
                GridSizer.AddMany([(self.StartAsistencia,0,wx.EXPAND), (spinStart, 0, wx.EXPAND)])

                #this strange setup is needed because the gridsizer isn't layout correctly in the cell for some reason
                Sizer = wx.BoxSizer(wx.VERTICAL)
                Sizer.Add(GridSizer,0)

                Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
                Sizer2.Add(Sizer,0)

                self.SetSizer(Sizer2)
                self.Layout()

class TimeCellEditorAsistencia(wx.grid.PyGridCellEditor):
    """
    Clase destinada a crear un editor personalizado dentro de las Celdas de un Grid
    """

    def __init__(self):
        wx.grid.PyGridCellEditor.__init__(self)

    def Create(self, parent, id, evtHandler):
        self.timeHoraEntrada24 = TimeControlAsistencia(parent,-1)
        self.timeHoraEntrada24.StartAsistencia.SetInsertionPoint(0)
        self.SetControl(self.timeHoraEntrada24)
        if evtHandler:
            self.timeHoraEntrada24.PushEventHandler(evtHandler)
            self.timeHoraEntrada24.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnDClick)

    def BeginEdit(self, row, col, grid):
        self.startValue = grid.GetTable().GetValue(row, col)
        self.timeHoraEntrada24.StartAsistencia.SetInsertionPointEnd()
        self.timeHoraEntrada24.StartAsistencia.SetFocus()
        self.timeHoraEntrada24.StartAsistencia.SetSelection(0, self.timeHoraEntrada24.StartAsistencia.GetLastPosition())

    def EndEdit(self, row, col, grid, val):
        changed = False
        val = self.timeHoraEntrada24.StartAsistencia.GetValue()
        if val != self.startValue:
            changed = True
            grid.GetTable().SetValue(row, col, val) # update the table

        self.startValue = '08:00:00'
        self.timeHoraEntrada24.StartAsistencia.SetValue('08:00:00')

        return changed

    def Reset(self):
        self.timeHoraEntrada24.StartAsistencia.SetValue(self.startValue)
        self.timeHoraEntrada24.StartAsistencia.SetInsertionPointEnd()

    def Clone(self):
        return TimeCellEditorManana()

    def OnDClick(self, evt):
        if self.CanEnableCellControl() and gridlib:
           self.EnableCellEditControl()


class TimeControlManana(wx.Control):
        """
        Clase creada para poder mostrar los TimeCtrl dentro de las Celdas de un Grid
        """

        def __init__(self, parent,id):
                wx.Control.__init__(self, parent, -1)
                minStart="08:00:00"
                maxStart="12:00:00"

                spinStart = wx.SpinButton(self,-1,wx.DefaultPosition,wx.Size(-1,-1),0)

                self.Start = masked.TimeCtrl(self, -1, name="24 hour control", fmt24hr=True,spinButton = spinStart)
                self.Start.SetLimited(True)
                self.Start.SetMin( minStart )
                self.Start.SetMax( maxStart )

                GridSizer = wx.BoxSizer( wx.HORIZONTAL )
                GridSizer.AddMany([(self.Start,0,wx.EXPAND), (spinStart, 0, wx.EXPAND)])

                #this strange setup is needed because the gridsizer isn't layout correctly in the cell for some reason
                Sizer = wx.BoxSizer(wx.VERTICAL)
                Sizer.Add(GridSizer,0)

                Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
                Sizer2.Add(Sizer,0)

                self.SetSizer(Sizer2)
                self.Layout()

class TimeControlTarde(wx.Control):
        """
        Clase creada para poder mostrar los TimeCtrl dentro de las Celdas de un Grid
        """

        def __init__(self, parent,id):
                wx.Control.__init__(self, parent, -1)
                minEnd="12:00:00"
                maxEnd="19:00:00"

                spinEnd = wx.SpinButton(self,-1,wx.DefaultPosition,wx.Size(-1,-1),0)

                self.End = masked.TimeCtrl(self, -1, name="24 hour control", fmt24hr=True,spinButton = spinEnd)
                self.End.SetLimited(True)
                self.End.SetMin( minEnd )
                self.End.SetMax( maxEnd )

                GridSizer = wx.BoxSizer( wx.HORIZONTAL )
                GridSizer.AddMany([(self.End,0,wx.EXPAND), (spinEnd, 0, wx.EXPAND)])

                #this strange setup is needed because the gridsizer isn't layout correctly in the cell for some reason
                Sizer = wx.BoxSizer(wx.VERTICAL)
                Sizer.Add(GridSizer,0)

                Sizer2 = wx.BoxSizer(wx.HORIZONTAL)
                Sizer2.Add(Sizer,0)

                self.SetSizer(Sizer2)
                self.Layout()

class EditorsAndRenderersGrid(gridlib.Grid):
    """
    Clase destinada a crear un Grid
    """

    def __init__(self, parent, filas, columnas):
        gridlib.Grid.__init__(self, parent, -1)

        self.filas=filas
        self.columnas=columnas

        catedrasDisponibles=[]
        try:
            catedras=app.BD.listarCatedras()
            self.listaID_catedras=[]
            catedrasDisponibles.append(u'')
            for catedra in catedras:
                catedrasDisponibles.append(catedra[1])
                self.listaID_catedras.append(catedra[1])
        except lite.Error, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'NO se cargaron las Cátedras %s'%e,"Cargando Profesor", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            app.BD.desconectar()

        editorCatedrasData = [(gridlib.GridCellChoiceEditor, (catedrasDisponibles, False)),]
        entrada_salida=[(''),]
        editorDias=[(u'', gridlib.GridCellChoiceEditor, (['', u'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'], False)),]

        self.CreateGrid(self.filas, self.columnas)


        self.SetColLabelValue(0, u"Día")
        self.SetColLabelValue(1, u"Cátedra")
        self.SetColLabelValue(2, u"Hora de Entrada Mañana")
        self.SetColLabelValue(3, u"Hora de Salida Mañana")
        self.SetColLabelValue(4, u"Hora de Entrada Tarde")
        self.SetColLabelValue(5, u"Hora de Salida Tarde")
        self.SetColLabelValue(6, u"Observaciones")

        for i in range(self.filas):
            for value, editorClass, args in editorDias:
                editor = editorClass(*args)
                self.SetCellValue(i, 0, value)
                self.SetCellEditor(i, 0, editor)


        for i in range(self.filas):
            for editorClass, args in editorCatedrasData:
                editor = editorClass(*args)
                self.SetCellEditor(i, 1, editor)


        for i in range(self.filas):
            for value in entrada_salida:
                self.SetCellValue(i, 2, value)
                self.SetCellEditor(i, 2, TimeCellEditorManana())
                self.SetCellValue(i, 3, value)
                self.SetCellEditor(i, 3, TimeCellEditorManana())
                self.SetCellValue(i, 4, value)
                self.SetCellEditor(i, 4, TimeCellEditorTarde())
                self.SetCellValue(i, 5, value)
                self.SetCellEditor(i, 5, TimeCellEditorTarde())


        font = self.GetFont()
        font.SetWeight(wx.BOLD)
        attr = gridlib.GridCellAttr()
        attr.SetFont(font)
        attr.SetBackgroundColour(wx.LIGHT_GREY)
        attr.SetReadOnly(True)
        attr.SetAlignment(wx.RIGHT, -1)
        attr.IncRef()

        # There is a bug in wxGTK for this method...
        self.AutoSizeColumns(True)
        self.AutoSizeRows(True)

        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)
        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)

    def OnSelectCell(self, event):
        self.f=event.GetRow()
        self.c=event.GetCol()
        event.Skip()

    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()
            # make a menu

        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,u"Limpiar Seleción")
        menu.AppendItem(item)
        menu.Append(self.popupID2, "Limpiar Todo")

        self.Bind( wx.EVT_MENU, self.OnMenuSelection, id = self.popupID1)
        self.Bind( wx.EVT_MENU, self.OnMenuSelection2, id = self.popupID2)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def showPopupMenu2(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1_2"):
            self.popupID1_2 = wx.NewId()
            # make a menu

        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1_2,u"Limpiar Celda(s)")
        menu.AppendItem(item)

        self.Bind( wx.EVT_MENU, self.OnMenuSelection3, id = self.popupID1_2)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnMenuSelection(self, event):
        filas=self.GetSelectedRows()
        for fila in filas:
            for i in range(self.columnas):
                self.SelectRow(fila)
                self.SetCellValue(fila, i, '')

    def OnMenuSelection2(self, event):
        self.ClearGrid()
        self.ForceRefresh()

    def OnMenuSelection3(self, event):
        try:
            for celda in self.celdas:
                self.SetCellValue(celda[0], celda[1], '')
        except:
            pass
        finally:
            self.SetCellValue(self.f, self.c, '')

    def OnRangeSelect(self, event):
        self.celdas=[]
        if event.Selecting():
            for i in range (event.GetTopRow(),event.GetBottomRow()+1):
                for j in range(event.GetLeftCol(),event.GetRightCol()+1):
                    self.celdas.append((i,j))


class EditorsAndRenderersGrid_Asistencia(gridlib.Grid):
    """
    Clase destinada a crear un Grid
    """

    def __init__(self, parent, filas, columnas, catedra=None):
        gridlib.Grid.__init__(self, parent, -1)

        self.catedra=catedra
        self.filas=filas
        self.columnas=columnas

        catedrasDisponibles=[]
        try:
            catedras=app.BD.listarCatedras()
            self.listaID_catedras=[]
            catedrasDisponibles.append(u'')
            for catedra in catedras:
                catedrasDisponibles.append(catedra[1])
                self.listaID_catedras.append(catedra[1])
        except lite.Error, e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'NO se cargaron las Cátedras %s'%e,"Cargando Profesor", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            app.BD.desconectar()

        editorCatedrasData = [(gridlib.GridCellChoiceEditor, (self.catedra, False)),]
        entrada_salida=[(''),]

        self.CreateGrid(self.filas, self.columnas)


        self.SetColLabelValue(0, u"Fecha")
        self.SetColLabelValue(1, u"Día")
        self.SetColLabelValue(2, u"Cátedra")
        self.SetColLabelValue(3, u"Hora de Entrada")
        self.SetColLabelValue(4, u"Hora de Salida")
        self.SetColLabelValue(5, u"Observaciones")


        for i in range(self.filas):
            for value in entrada_salida:
                self.SetCellValue(i, 0, value)
                self.SetCellEditor(i, 0, DateCellEditorAsistencia())


        for i in range(self.filas):
            self.SetReadOnly(i, 1)

        for i in range(self.filas):
            for editorClass, args in editorCatedrasData:
                editor = editorClass(*args)
                self.SetCellEditor(i, 2, editor)

        for i in range(self.filas):
            for value in entrada_salida:
                self.SetCellValue(i, 3, value)
                self.SetCellEditor(i, 3, TimeCellEditorAsistencia())
                self.SetCellValue(i, 4, value)
                self.SetCellEditor(i, 4, TimeCellEditorAsistencia())

        font = self.GetFont()
        font.SetWeight(wx.BOLD)
        attr = gridlib.GridCellAttr()
        attr.SetFont(font)
        attr.SetBackgroundColour(wx.LIGHT_GREY)
        attr.SetReadOnly(True)
        attr.SetAlignment(wx.RIGHT, -1)
        attr.IncRef()

        # There is a bug in wxGTK for this method...
        self.AutoSizeColumns(True)
        self.AutoSizeRows(True)

        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)
        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)
        self.Bind(gridlib.EVT_GRID_CELL_CHANGED, self.OnChangeCell)

    def OnChangeCell(self, event):
        if self.c==0:
            fecha=self.GetCellValue(self.f, self.c)

            aN,mN,dN=map(int, fecha.split('-'))
            dia=wx.DateTimeFromDMY(dN,mN-1,aN)

            num_dia=wx.DateTime.GetWeekDay(dia)
            nombre_dia=wx.DateTime.GetWeekDayName(num_dia)
            self.SetCellValue(self.f, self.c+1, nombre_dia)

    def OnSelectCell(self, event):
        self.f=event.GetRow()
        self.c=event.GetCol()
        event.Skip()

    def showPopupMenu(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            # make a menu

        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1,u"Limpiar Filas")
        menu.AppendItem(item)

        self.Bind( wx.EVT_MENU, self.OnMenuSelection, id = self.popupID1)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def showPopupMenu2(self, event):
        """
        Create and display a popup menu on right-click event
        """
        if not hasattr(self, "popupID1_2"):
            self.popupID1_2 = wx.NewId()
            # make a menu

        menu = wx.Menu()
        # Show how to put an icon in the menu
        item = wx.MenuItem(menu, self.popupID1_2,u"Limpiar Celda(s)")
        menu.AppendItem(item)

        self.Bind( wx.EVT_MENU, self.OnMenuSelection3, id = self.popupID1_2)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnMenuSelection(self, event):
        filas=self.GetSelectedRows()
        self.DeleteRows(filas[0], len(filas))

    def OnMenuSelection3(self, event):
        try:
            for celda in self.celdas:
                if celda[1]==3 or celda[1]==4:
                    self.SetCellValue(celda[0], celda[1], '00:00:00')
                else:
                    mensaje=wx.MessageDialog(self,u'No se puede Limpiar esta Celda',u'Error', wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
        except:
            pass
        finally:
            if self.c==3 or self.c==4:
                self.SetCellValue(self.f, self.c, '00:00:00')
            else:
                mensaje=wx.MessageDialog(self,u'No se puede Limpiar esta Celda',u'Error', wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()

    def OnRangeSelect(self, event):
        self.celdas=[]
        if event.Selecting():
            for i in range (event.GetTopRow(),event.GetBottomRow()+1):
                for j in range(event.GetLeftCol(),event.GetRightCol()+1):
                    self.celdas.append((i,j))


class CoreccionAsistencia(FrameCoreccionAsistencia):

    def FrameCoreccionAsistenciaOnClose( self, event ):
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def btnCancelarCorreccionProfesorOnButtonClick( self, event ):
        self.MakeModal(False)
        self.Destroy()
        app.limpiarDirectorios()

    def m_choiceCorreccionProfesorOnChoice(self, event):
        self.resetFrameCorrecion()

    def resetFrameCorrecion(self, corregido=False):
        try:
            if corregido:
                self.listarProfesores()
                self.m_datePickerFechaInicioCorreccion.SetValue(wx.DateTime.Today())
                self.m_datePickerFechaFinCorreccion.SetValue(wx.DateTime.Today())
            self.grid.ClearGrid()
            self.grid.ForceRefresh()
            self.Refresh()
            self.panelFechasCorregir.Layout()
        except:
            pass

    def mostrarAsistencia(self):
        inicio=self.m_datePickerFechaInicioCorreccion.GetValue().Format('%Y-%m-%d')
        fin=self.m_datePickerFechaFinCorreccion.GetValue().Format('%Y-%m-%d')

        profSeleccionado=self.m_choiceCorreccionProfesor.GetCurrentSelection()

        self.profeID=self.listaID_Prof[profSeleccionado-1]

        asistencia=app.BD.VerAsistencia(self.profeID, inicio, fin)

        listaFechas=[]
        listaDias=[]
        listaHorasEntrada=[]
        listaHorasSalida=[]
        listaObservaciones=[]

        for dia in asistencia:
            listaFechas.append(dia[1])

            listaDias.append(dia[2])

            listaHorasEntrada.append(dia[3])

            listaHorasSalida.append(dia[4])

            listaObservaciones.append(dia[5])

        catedras=app.BD.buscarIDCatedraDictada(self.profeID)
        nombrecatedrasProf=app.BD.buscarNomCatedraDictada(self.profeID, asistencia=True)

        listanombrecatedrasProf=[]
        for cat in nombrecatedrasProf:
            listanombrecatedrasProf.append(cat[0])
        numerodecatedras=len(list(catedras))
        self.catedra=listanombrecatedrasProf

        if numerodecatedras:
            for i in range(len(asistencia)):
                self.grid.SetCellValue(i, 0, unicode(listaFechas[i]))
                self.grid.SetCellValue(i, 1, unicode(listaDias[i]))
                self.grid.SetCellValue(i, 2, unicode(listanombrecatedrasProf[i]))
                self.grid.SetCellValue(i, 3, unicode(listaHorasEntrada[i]))
                self.grid.SetCellValue(i, 4, unicode(listaHorasSalida[i]))
                self.grid.SetCellValue(i, 5, unicode(listaObservaciones[i]))


    def iniciarPanelCorreccion(self, filas):
        self.fi=filas

        profSeleccionado=self.m_choiceCorreccionProfesor.GetCurrentSelection()
        self.profeID=self.listaID_Prof[profSeleccionado-1]
        nombrecatedrasProf=app.BD.buscarNomCatedraDictada(self.profeID, rep=True)
        listanombrecatedrasProf=[]
        for cat in nombrecatedrasProf:
            listanombrecatedrasProf.append(cat[0])


        sizerPanelHorasProf = wx.BoxSizer( wx.VERTICAL )
        hSizerEntrada=wx.BoxSizer( wx.VERTICAL )

        #CREAMOS EL GRID PARA EL HORARIO DEL ROFSOR
        self.grid = EditorsAndRenderersGrid_Asistencia(self.panelFechasCorregir, int(self.fi[0]), 6,listanombrecatedrasProf)
        self.grid.SetMargins(0,0)

        for i in range(self.grid.GetNumberRows()):
            self.grid.SetRowSize(i, 30)

        for i in range(self.grid.GetNumberCols()):
            self.grid.SetColSize(i, 163)

        self.grid.SetColLabelSize(20)

        self.filas=self.grid.GetNumberRows()
        self.columnas=self.grid.GetNumberCols()

        self.panelFechasCorregir.SetSizer( sizerPanelHorasProf )
        sizerPanelHorasProf.Add(hSizerEntrada,0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        hSizerEntrada.Add( self.grid, 0, wx.EXPAND, 5 )
        hSizerEntrada.Layout()
        self.panelFechasCorregir.Layout()
        self.Layout()

        self.grid.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK,self.grid.showPopupMenu)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,self.grid.showPopupMenu2)

    def btnMostrarAsistenciaProfesorOnButtonClick( self, event ):

        try:
            self.grid.Destroy()
        except:
            pass

        fechaInicio=self.m_datePickerFechaInicioCorreccion.GetValue().Format('%Y-%m-%d')
        fechaFin=self.m_datePickerFechaFinCorreccion.GetValue().Format('%Y-%m-%d')
        if not (fechaInicio > fechaFin):
            if not self.m_choiceCorreccionProfesor.GetCurrentSelection()==0:
                filas=app.BD.contarAsistencias(self.listaCI_Prof[self.m_choiceCorreccionProfesor.GetCurrentSelection()-1], fechaInicio, fechaFin)
                self.iniciarPanelCorreccion(filas[0])
                self.mostrarAsistencia()
            else:
                mensaje=wx.MessageDialog(self,u'Debe Escojer un Profesor',u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'La Fecha de Fin debe ser Mayor o Igual a la Fecha de Inicio.',u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def btnCorregirAsistenciaOnButtonClick( self, event ):
        corregir=[]
        try:
            listaFechasCorregidas=[]
            listaDiasCorregidas=[]
            listaCatedrasCoregidas=[]
            listaIDCatedrasCoregidas=[]
            listaHorasEntradaCorregidas=[]
            listaHorasSalidaCorregidas=[]
            listaObservacionesCorregidas=[]
            listaHorasCorregidas=[]

            self.panelFechasCorregir.Layout()
            profesor=self.listaCI_Prof[self.m_choiceCorreccionProfesor.GetCurrentSelection()-1]

            fechaInicio=self.m_datePickerFechaInicioCorreccion.GetValue().Format('%Y-%m-%d')
            fechaFin=self.m_datePickerFechaFinCorreccion.GetValue().Format('%Y-%m-%d')

            if not (fechaInicio[5:7] > fechaFin[5:7]):
                try:
                    if not self.m_choiceCorreccionProfesor.GetCurrentSelection()==0:
                        for i in range(self.grid.GetNumberRows()):
                            if ((self.grid.GetCellValue(i,3) != self.grid.GetCellValue(i,4) and self.grid.GetCellValue(i,3) < self.grid.GetCellValue(i,4) and self.grid.GetCellValue(i,3) != '00:00:00' and self.grid.GetCellValue(i,4) != '00:00:00')
                                or
                                (self.grid.GetCellValue(i,3)=='00:00:00' and self.grid.GetCellValue(i,4)=='00:00:00')): #si la los dias y catedra no estan vacios

                                corregir.append(True)
                                listaFechasCorregidas.append(self.grid.GetCellValue(i,0))
                                listaDiasCorregidas.append(self.grid.GetCellValue(i,1))
                                listaCatedrasCoregidas.append(self.grid.GetCellValue(i,2))
                                listaHorasEntradaCorregidas.append(self.grid.GetCellValue(i,3))
                                listaHorasSalidaCorregidas.append(self.grid.GetCellValue(i,4))

                                hora_Entrada=self.grid.GetCellValue(i,3)
                                hora_Salida=self.grid.GetCellValue(i,4)

                                # string to time tuple INICIO
                                inicio=time.strptime(hora_Entrada, "%H:%M:%S")
                                # string to time tuple FIN
                                fin=time.strptime(hora_Salida, "%H:%M:%S")

                                # time tuple to datetime object INICIO
                                t1 = datetime(*inicio[0:6])
                                # time tuple to datetime object FIN
                                t2 = datetime(*fin[0:6])

                                #Tiempo Transurido entre el INICIO y el FIN
                                listaHorasCorregidas.append(str(t2-t1))

                                listaObservacionesCorregidas.append(self.grid.GetCellValue(i,5))
                            else:
                                if (self.grid.GetCellValue(i,3)=='00:00:00' and self.grid.GetCellValue(i,4) != '00:00:00' and self.grid.GetCellValue(i,3) != self.grid.GetCellValue(i,4)):
                                    corregir.append(False)
                                elif (self.grid.GetCellValue(i,3) != '00:00:00' and self.grid.GetCellValue(i,4)=='00:00:00' and self.grid.GetCellValue(i,3) != self.grid.GetCellValue(i,4)):
                                    corregir.append(False)
                                else:
                                    corregir.append(False)

                        for catedra in listaCatedrasCoregidas:
                            listaIDCatedrasCoregidas.append(app.BD.buscarID_catedra(catedra))

                        try:
                            if not False in corregir:
                                app.BD.eliminarAsistencia(profesor, fechaInicio, fechaFin)
                                app.BD.CorregirAsistencia(len(listaFechasCorregidas), listaFechasCorregidas, listaDiasCorregidas, listaIDCatedrasCoregidas, listaHorasEntradaCorregidas, listaHorasSalidaCorregidas, listaHorasCorregidas, listaObservacionesCorregidas, profesor)
                                mensaje=wx.MessageDialog(self,u'Asistencia Corregida Exitosamente',u'Error Generando Proyección', wx.OK|wx.ICON_INFORMATION)
                                mensaje.ShowModal()
                                self.resetFrameCorrecion(corregido=True)
                            else:
                                mensaje=wx.MessageDialog(self,u'Hay campos Vacios en la Tabla, o la Hora de Entrada es Mayor que la de Salida',u'Error Corrigiendo Asistencia', wx.OK|wx.ICON_HAND)
                                mensaje.ShowModal()
                        except lite.Error, e:
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                            logging.error('%s - [%s]'%(e, trace))
                            mensaje=wx.MessageDialog(self,u'ERROR \n\n%s'%e,u'Error Corrigiendo Asistencia', wx.OK|wx.ICON_HAND)
                            mensaje.ShowModal()
                    else:
                        mensaje=wx.MessageDialog(self,u'Debe Escojer un Profesor',u'Error Corrigiendo Asistencia', wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()
                except IOError, e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                    logging.error('%s - [%s]'%(e, trace))
                    mensaje=wx.MessageDialog(self,u'La Proyección solicitada NO fue Generada \n\n%s'%e,u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            else:
                mensaje=wx.MessageDialog(self,u'La Fecha de Fin debe ser Mayor o Igual a la Fecha de Inicio.',u'Error Generando Proyección', wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
        except IndexError:
            #error, sacamos dialogo y decimos que hagan configuracion
            mensaje=wx.MessageDialog(self,u'No Hay ningún Profesor cargado en el Sistema. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def listarProfesores(self):

        self.m_choiceCorreccionProfesor.Clear()
        self.m_choiceCorreccionProfesor.Append(u"Seleccionar Profesor...")
        self.m_choiceCorreccionProfesor.SetSelection( 0 )

        profesores=app.BD.listarProfesores()

        self.listaID_Prof=[]
        self.listaCI_Prof=[]
        for profesor in profesores:
            self.m_choiceCorreccionProfesor.Append(profesor[1]+' '+profesor[2])
            self.listaCI_Prof.append(profesor[0])
            self.listaID_Prof.append(profesor[0])


class panelAsistencia (PanelAsistencia):
    """
    Clase destinada a manejar todo lo referente a la carga de Asistencia de Profesores
    """

    def m_radioBtnAsistenciaCompletaOnRadioButton(self, event):
        self.timeHoraEntrada24.Enable(True)
        self.spinHoraEntrada.Enable(True)
        self.timeHoraSalida24.Enable(True)
        self.spinHoraSalida.Enable(True)

        self.timeHoraEntrada24.SetMin( "06:00:00" )
        self.timeHoraEntrada24.SetMax( "20:00:00" )

        self.timeHoraSalida24.SetMin( "07:00:00" )
        self.timeHoraSalida24.SetMax( "21:00:00" )

        self.timeHoraEntrada24.SetValue('06:00:00')
        self.timeHoraSalida24.SetValue('21:00:00')

    def m_radioBtnAsistenciaIncompletaOnRadioButton(self, event):
        self.timeHoraEntrada24.SetMin( "00:00:00" )
        self.timeHoraEntrada24.SetMax( "00:00:00" )

        self.timeHoraSalida24.SetMin( "00:00:00" )
        self.timeHoraSalida24.SetMax( "00:00:00" )

        self.timeHoraEntrada24.SetValue('00:00:00')
        self.timeHoraSalida24.SetValue('00:00:00')

        self.timeHoraEntrada24.Enable(False)
        self.spinHoraEntrada.Enable(False)
        self.timeHoraSalida24.Enable(False)
        self.spinHoraSalida.Enable(False)

    def m_choiceNomProfOnChoice(self, event):
        """
        Carga las catedras en m_choiceCatedraProf, dependindo de lo que se seleccione en m_choiceNomProf
        """
        self.m_choiceCatedraProf.Clear()
        self.m_choiceCatedraProf.Append(u"Seleccionar Catedra...")
        self.m_choiceCatedraProf.SetSelection( 0 )
        if not self.m_choiceNomProf.GetCurrentSelection()==0:
            profSeleccionado=self.m_choiceNomProf.GetCurrentSelection()

            profeID=self.listaID_profesores[profSeleccionado-1]

            self.listacatedras=app.BD.listarID_CatedrasAsistencia(profeID)
            lista=list(self.listacatedras)
            for catedra in lista:
                self.m_choiceCatedraProf.Append(unicode(catedra[0]))
                self.m_choiceCatedraProf.Refresh()

    def IniciarHorasPanelAsistencia(self):
        """
        Crea los SpinControls para las Horas de asistencia de los profesores
        """
        self.m_choiceNomProf.Clear()
        self.m_choiceNomProf.Append("Seleccionar Profesor...")
        self.m_choiceNomProf.SetSelection( 0 )

        self.m_choiceCatedraProf.Clear()
        self.m_choiceCatedraProf.Append(u"Seleccionar Cátedra...")
        self.m_choiceCatedraProf.SetSelection( 0 )

        self.m_radioBtnAsistenciaCompleta.SetValue(True)

        profesores=app.BD.listarProfesores()

        self.listaID_profesores=[]
        for profesor in profesores:
            self.m_choiceNomProf.Append(profesor[1]+" "+profesor[2])
            self.listaID_profesores.append(profesor[0])

        self.datePickerFechaAsistencia.SetRange(wx.DateTimeFromDMY(01,01,1950), wx.DateTime.Today())
        self.datePickerFechaAsistencia.SetValue(wx.DateTime.Today())
        self.datePickerFechaAsistencia.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        self.datePickerFechaAsistencia.Refresh()


        sizerPanelHoraEntradaProf = wx.BoxSizer( wx.VERTICAL )
        sizerPanelHoraSalidaProf = wx.BoxSizer( wx.VERTICAL )
        hSizerEntrada=wx.BoxSizer( wx.HORIZONTAL )
        hSizerSalida=wx.BoxSizer( wx.HORIZONTAL )

        self.panelHoraEntradaProf.SetSizer( sizerPanelHoraEntradaProf )
        self.panelHoraSalidaProf.SetSizer( sizerPanelHoraSalidaProf )

        self.lblEntradaProf= wx.StaticText( self.panelHoraEntradaProf, wx.ID_ANY, ("Hora de Entrada"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblEntradaProf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.spinHoraEntrada = wx.SpinButton( self.panelHoraEntradaProf, -1, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.timeHoraEntrada24 = masked.TimeCtrl(self.panelHoraEntradaProf, -1, name="24 hour control", fmt24hr=True,spinButton = self.spinHoraEntrada)
        self.timeHoraEntrada24.SetLimited(True)
        self.timeHoraEntrada24.SetMin( "06:00:00" )
        self.timeHoraEntrada24.SetMax( "20:00:00" )

        self.lblSalidaProf= wx.StaticText( self.panelHoraSalidaProf, wx.ID_ANY, ("Hora de Salida"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lblSalidaProf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
        self.spinHoraSalida = wx.SpinButton( self.panelHoraSalidaProf, -1, wx.DefaultPosition,wx.DefaultSize, 0 )
        self.timeHoraSalida24 = masked.TimeCtrl(self.panelHoraSalidaProf, -1, name="24 hour control", fmt24hr=True,spinButton = self.spinHoraSalida)
        self.timeHoraSalida24.SetLimited(True)
        self.timeHoraSalida24.SetMin( "07:00:00" )
        self.timeHoraSalida24.SetMax( "21:00:00" )


        self.timeHoraEntrada24.SetValue('06:00:00')
        self.timeHoraSalida24.SetValue('21:00:00')


        sizerPanelHoraEntradaProf.Add( self.lblEntradaProf, 0, wx.ALIGN_LEFT|wx.TOP|wx.BOTTOM )
        sizerPanelHoraEntradaProf.Add(hSizerEntrada,0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        hSizerEntrada.Add( self.timeHoraEntrada24, 0, wx.ALIGN_LEFT, 5 )
        hSizerEntrada.Add( self.spinHoraEntrada, 0, wx.ALIGN_LEFT, 5 )
        self.panelHoraEntradaProf.Refresh()

        sizerPanelHoraSalidaProf.Add( self.lblSalidaProf, 0, wx.ALIGN_LEFT|wx.TOP|wx.BOTTOM )
        sizerPanelHoraSalidaProf.Add(hSizerSalida,0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        hSizerSalida.Add( self.timeHoraSalida24,0, wx.ALIGN_LEFT, 5 )
        hSizerSalida.Add( self.spinHoraSalida,  0, wx.ALIGN_LEFT, 5 )
        self.panelHoraSalidaProf.Refresh()

        hSizerEntrada.Layout()
        hSizerSalida.Layout()
        sizerPanelHoraEntradaProf.Layout()
        sizerPanelHoraSalidaProf.Layout()
        self.panelHoraEntradaProf.Layout()
        self.panelHoraSalidaProf.Layout()
        self.panelAsistProf.Layout()
        self.Layout()
        self.Refresh()

    def btnCargaAsistenciaProfOnButtonClick( self, event ):
        """
        Carga la asistencia docente en la base de datos
        """

        if not self.m_choiceNomProf.GetCurrentSelection()==0 and not self.m_choiceCatedraProf.GetCurrentSelection()==0:
            profSeleccionado=self.m_choiceNomProf.GetCurrentSelection()
            profesor=app.BD.buscarID_Profesor(self.listaID_profesores[profSeleccionado-1])

            catedraSelecionada=self.m_choiceCatedraProf.GetStringSelection()

            catedraID=app.BD.buscarID_catedra(catedraSelecionada)

            fecha_Asistencia=self.datePickerFechaAsistencia.GetValue().Format('%Y-%m-%d').encode()
            dia_asistencia=self.datePickerFechaAsistencia.GetValue().Format('%A')

            if dia_asistencia=='Sunday':
                dia_asistencia_espanol='Domingo'
            elif dia_asistencia=='Monday':
                dia_asistencia_espanol='Lunes'
            elif dia_asistencia=='Tuesday':
                dia_asistencia_espanol='Martes'
            elif dia_asistencia=='Wednesday':
                dia_asistencia_espanol=u'Miércoles'
            elif dia_asistencia=='Thursday':
                dia_asistencia_espanol='Jueves'
            elif dia_asistencia=='Friday':
                dia_asistencia_espanol='Viernes'
            elif dia_asistencia=='Saturday':
                dia_asistencia_espanol=u'Sábado'
            else:
                dia_asistencia_espanol=dia_asistencia


            hora_Entrada=self.timeHoraEntrada24.GetValue()
            hora_Salida=self.timeHoraSalida24.GetValue()

            # string to time tuple INICIO
            inicio=time.strptime(hora_Entrada, "%H:%M:%S")
            # string to time tuple FIN
            fin=time.strptime(hora_Salida, "%H:%M:%S")

            # time tuple to datetime object INICIO
            t1 = datetime(*inicio[0:6])
            # time tuple to datetime object FIN
            t2 = datetime(*fin[0:6])

            #Tiempo Transurido entre el INICIO y el FIN
            tiempoDeClase=t2-t1

            observaciones=string.capitalize(self.txtObservAsistProf.GetValue())

            if not t1>t2:
                mensaje=wx.MessageDialog(self,'Datos de Asistencia Correctos?: \n\nProfesor:%s \n\nCatedra: %s\n\nFecha: %s \n\nHora de Entrada: %s \n\nHora de Salida: %s \n\nHoras de Clase: %s \n\nObservaciones: %s'%(self.m_choiceNomProf.GetStringSelection(), catedraSelecionada, fecha_Asistencia, hora_Entrada, hora_Salida, tiempoDeClase, observaciones),"Cargando Profesor", wx.YES_NO | wx.ICON_QUESTION)
                if mensaje.ShowModal()==wx.ID_YES:
                    try:
                        app.BD.CargarAsistencia(str(tiempoDeClase), profesor[0], catedraID[0], fecha_Asistencia, dia_asistencia_espanol, hora_Entrada, hora_Salida, observaciones)
                        mensaje=wx.MessageDialog(self,u'Se ha cargado la Asistencia Correctamente para el Profesor %s de %s'%(self.m_choiceNomProf.GetStringSelection(), catedraSelecionada),"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                        self.timeHoraEntrada24.Destroy()
                        self.spinHoraEntrada.Destroy()
                        self.timeHoraSalida24.Destroy()
                        self.spinHoraSalida.Destroy()
                        self.IniciarHorasPanelAsistencia()
                        self.txtObservAsistProf.Clear()
                        self.Refresh()
                    except TypeError:
                        mensaje=wx.MessageDialog(self,u'Debe escojer una Cátedrar',"Error Cargando Asistencia", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                    except:
                        exc_type, exc_value, exc_traceback = sys.exc_info()
                        trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                        logging.error('[%s]'%(trace))
                        mensaje=wx.MessageDialog(self,u'la Asistencia NO fue cargada Correctamente para el Profesor %s de %s'%(self.m_choiceNomProf.GetStringSelection(), catedraSelecionada),"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                else:
                    mensaje=wx.MessageDialog(self,u'Ahora puede corregirlos Datos',"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                    mensaje.ShowModal()
            else:
                mensaje=wx.MessageDialog(self,u'La Hora de Entrada debe ser Menor que la Hora de Salida',"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                mensaje.ShowModal()
        else:
            mensaje=wx.MessageDialog(self,u'Debe seleccionar un profesor y una Cátedra',"Cargando Profesor", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()


class panelBienvenida (PanelBienvenida):

    pass


class panelCarga (PanelCarga):
    """
    clase destinada a manejar todo lo referente a la carga de Profesores Nuevos
    """

    def IniciarPanelHoras(self):
        """
        Crea los SpinControls para las Horas laborales de los profesores
        """

        self.txtNombreProf_Carga.SetFocus()

        self.datePickerFecNacProf.SetRange(wx.DateTimeFromDMY(01,01,1920), wx.DateTime.Today())
        self.datePickerFecIngresoProf.SetRange(wx.DateTimeFromDMY(01,01,1920), wx.DateTime.Today())


        sizerPanelHorasProf = wx.BoxSizer( wx.VERTICAL )
        hSizerEntrada=wx.BoxSizer( wx.VERTICAL )

        #CREAMOS EL GRID PARA EL HORARIO DEL ROFSOR
        self.grid = EditorsAndRenderersGrid(self.panelHorasProfCarga, 15, 7)
        self.grid.SetMargins(0,0)

        for i in range(self.grid.GetNumberRows()):
            self.grid.SetRowSize(i, 30)

        for i in range(self.grid.GetNumberCols()):
            self.grid.SetColSize(i, 163)

        self.grid.SetColLabelSize(20)

        self.filas=self.grid.GetNumberRows()
        self.columnas=self.grid.GetNumberCols()

        self.panelHorasProfCarga.SetSizer( sizerPanelHorasProf )
        sizerPanelHorasProf.Add(hSizerEntrada,0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        hSizerEntrada.Add( self.grid, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        hSizerEntrada.Layout()
        self.panelHorasProfCarga.Layout()
        self.Layout()

        self.grid.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK,self.grid.showPopupMenu)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,self.grid.showPopupMenu2)


    def btnCargaProfOnButtonClick( self, event ):

        self.validator=NotEmptyValidator()

        self.validator.SetWindow(self.txtNombreProf_Carga)
        if self.validator.Validate(self.txtNombreProf_Carga):
            validaNombre=True
        else:
            validaNombre=False

        self.validator.SetWindow(self.tctApellidoProf_Carga)
        if self.validator.Validate(self.tctApellidoProf_Carga):
            validaApellido=True
        else:
            validaApellido=False

        self.validator.SetWindow(self.txtCiProf_Carga)
        if self.validator.Validate(self.txtCiProf_Carga):
            validaCI=True
        else:
            validaCI=False

        self.validator.SetWindow(self.txtTlfProf_Carga)
        if self.validator.Validate(self.txtTlfProf_Carga):
            validaTel=True
        else:
            validaTel=False

        self.validator.SetWindow(self.txtEmailProf)
        if self.validator.Validate(self.txtEmailProf):
            validaMail=True
        else:
            validaMail=False

        activo=self.radioBox_ProfActivo.GetStringSelection()

        #Inicializo listas vacias para los dias , observaciones y las horas
        self.diasSelecionados=[]
        self.nombreCatedrasSelecionadas=[]
        self.idCatedraSeleccionada=[]
        self.horasEntradaMSeleccionadas=[]
        self.horasSalidaMSeleccionadas=[]
        self.horasEntradaTSeleccionadas=[]
        self.horasSalidaTSeleccionadas=[]
        self.observacionesDias=[]
        horasTotales_M=[]
        horasTotales_T=[]
        horasTotales_Dia=[]

        #Cargo los nombres de catedras Seleccionadas, los dias , observaciones y las horas correspondientes

        if not (validaNombre and validaApellido and validaCI and validaTel and validaMail) : #si la fila no esta vacia
            wx.MessageBox("No deben Haber campos Vacios", "Error")
            return False
        else:
            try:
                nombre=string.capwords(self.txtNombreProf_Carga.GetValue())
                apellido=string.capwords(self.tctApellidoProf_Carga.GetValue())
                ci=self.txtCiProf_Carga.GetValue()
                fechaNacimiento=self.datePickerFecNacProf.GetValue().Format('%Y-%m-%d').encode()
                fechaIngreso=self.datePickerFecIngresoProf.GetValue().Format('%Y-%m-%d').encode()
                email=self.txtEmailProf.GetValue()
                telf=self.txtTlfProf_Carga.GetValue()
                tipoProf=self.choiceTipoProfesor_Carga.GetCurrentSelection() #1 para profesor por horas, 2 para com. servicio y 3 para fijos

                #carga de los elementos del formulario de registro en listas
                for i in range(self.filas):
                    if self.grid.GetCellValue(i,0)!='' and self.grid.GetCellValue(i,1)!='' and ((self.grid.GetCellValue(i,2)!='' and self.grid.GetCellValue(i,3)!='') or (self.grid.GetCellValue(i,4)!='' and self.grid.GetCellValue(i,5)!='')): #si la los dias y catedra no estan vacios
                        self.diasSelecionados.append(self.grid.GetCellValue(i,0))

                        self.nombreCatedrasSelecionadas.append(self.grid.GetCellValue(i, 1))

                        self.observacionesDias.append(self.grid.GetCellValue(i, 6))

                        if (self.grid.GetCellValue(i,2)!='' and self.grid.GetCellValue(i,3)!='') and (self.grid.GetCellValue(i,3) > self.grid.GetCellValue(i,2)): #si las horas de la manana no estan vacias
                            self.horasEntradaMSeleccionadas.append(self.grid.GetCellValue(i, 2))
                            self.horasSalidaMSeleccionadas.append(self.grid.GetCellValue(i, 3))
                        else:
                            self.horasEntradaMSeleccionadas.append('00:00:00')
                            self.horasSalidaMSeleccionadas.append('00:00:00')

                        if (self.grid.GetCellValue(i,4)!='' and self.grid.GetCellValue(i,5)!='') and (self.grid.GetCellValue(i,5) > self.grid.GetCellValue(i,4)): #si las horas de la tarde no estan vacias
                            self.horasEntradaTSeleccionadas.append(self.grid.GetCellValue(i, 4))
                            self.horasSalidaTSeleccionadas.append(self.grid.GetCellValue(i, 5))
                        else:
                            self.horasEntradaTSeleccionadas.append('00:00:00')
                            self.horasSalidaTSeleccionadas.append('00:00:00')

                for cat in self.nombreCatedrasSelecionadas:
                    self.idCatedraSeleccionada.append(app.BD.buscarID_catedra(cat))

                if self.idCatedraSeleccionada != [] and self.idCatedraSeleccionada != [None] and self.idCatedraSeleccionada != [u''] and self.idCatedraSeleccionada != None:
                    cated=[]
                    for c in self.idCatedraSeleccionada:
                        cated.append(c[0])

                if self.diasSelecionados != [u''] and self.diasSelecionados != [None] and self.diasSelecionados != [] and self.idCatedraSeleccionada !=None:
                    dia=[]
                    for d in self.diasSelecionados:
                        dia.append(d)

                for h_M in range(len(self.horasEntradaMSeleccionadas)):
                    # string to time tuple INICIO
                    inicio_M=time.strptime(self.horasEntradaMSeleccionadas[h_M], "%H:%M:%S")
                    # string to time tuple FIN
                    fin_M=time.strptime(self.horasSalidaMSeleccionadas[h_M], "%H:%M:%S")

                    # time tuple to datetime object INICIO
                    t1_M = datetime(*inicio_M[0:6])
                    # time tuple to datetime object FIN
                    t2_M = datetime(*fin_M[0:6])

                    #Tiempo Transurido entre el INICIO y el FIN
                    horas_M=t2_M-t1_M
                    horasTotales_M.append(str(horas_M))

                for h_T in range(len(self.horasEntradaTSeleccionadas)):
                    # string to time tuple INICIO
                    inicio_T=time.strptime(self.horasEntradaTSeleccionadas[h_T], "%H:%M:%S")
                    # string to time tuple FIN
                    fin_T=time.strptime(self.horasSalidaTSeleccionadas[h_T], "%H:%M:%S")

                    # time tuple to datetime object INICIO
                    t1_T = datetime(*inicio_T[0:6])
                    # time tuple to datetime object FIN
                    t2_T = datetime(*fin_T[0:6])

                    #Tiempo Transurido entre el INICIO y el FIN
                    horas_T=t2_T-t1_T
                    horasTotales_T.append(str(horas_T))
                try:
                    for dia2 in self.diasSelecionados:
                        total = 0

                        totalM = 0
                        for horaM in  horasTotales_M:
                            hM, mM, sM = map(int, horaM.split(":"))
                            totalM += 3600*hM + 60*mM + sM

                        totalT = 0
                        for horaT in  horasTotales_T:
                            hT, mT, sT = map(int, horaT.split(":"))
                            totalT += 3600*hT + 60*mT + sT

                        total+=(totalM+totalT)
                        totalMT="%02d:%02d:%02d" % (total / 3600, total / 60 % 60, total % 60)
                        horasTotales_Dia.append(totalMT)
                except:
                    mensaje=wx.MessageDialog(self,'Las Horas de Entrada deben ser menores a las de Salida', "Error Cargando Profesor", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()

                j=0
                cargar=True
                elementos=[]
                while cargar and j <= self.filas-1:
                    if ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)!='' and self.grid.GetCellValue(j,3)!='' and self.grid.GetCellValue(j,3) > self.grid.GetCellValue(j,2)) and
                        (self.grid.GetCellValue(j,4)!='' and self.grid.GetCellValue(j,5)!='' and self.grid.GetCellValue(j,5) > self.grid.GetCellValue(j,4))): #si la los dias y catedra no estan vacios
                        cargar=True
                        elementos.append(True)
                    elif ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)!='' and self.grid.GetCellValue(j,3)!='' and self.grid.GetCellValue(j,3) > self.grid.GetCellValue(j,2)) and
                          (self.grid.GetCellValue(j,4)=='' and self.grid.GetCellValue(j,5)=='')): #si la los dias y catedra no estan vacios
                        cargar=True
                        elementos.append(True)
                    elif ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)=='' and self.grid.GetCellValue(j,3)=='') and
                          (self.grid.GetCellValue(j,4)!='' and self.grid.GetCellValue(j,5)!='' and self.grid.GetCellValue(j,5) > self.grid.GetCellValue(j,4))):
                        cargar=True
                        elementos.append(True)
                    elif self.grid.GetCellValue(j,0)=='' and self.grid.GetCellValue(j,1)=='' and self.grid.GetCellValue(j,2)=='' and self.grid.GetCellValue(j,3)=='' and self.grid.GetCellValue(j,4)=='' and self.grid.GetCellValue(j,5)=='':
                        cargar=True
                    else:
                        cargar=False
                        elementos.append(False)
                    j=j+1

                if not False in elementos and self.idCatedraSeleccionada != [] and self.idCatedraSeleccionada != [None] and self.idCatedraSeleccionada != [u''] and self.idCatedraSeleccionada != None:
                    try:
                        app.BD.agregarProfesor(nombre, apellido, ci, fechaNacimiento, telf, fechaIngreso, email, cated, activo, tipoProf, horasTotales_Dia, dia, self.observacionesDias, self.horasEntradaMSeleccionadas, self.horasSalidaMSeleccionadas, self.horasEntradaTSeleccionadas, self.horasSalidaTSeleccionadas,  horasTotales_M, horasTotales_T)
                        horasTotales_Dia=[]
                        self.txtNombreProf_Carga.Clear()
                        self.tctApellidoProf_Carga.Clear()
                        self.txtCiProf_Carga.Clear()
                        self.txtTlfProf_Carga.Clear()
                        self.txtEmailProf.Clear()
                        self.grid.Destroy()
                        self.IniciarPanelHoras()
                        mensaje=wx.MessageDialog(self,'El Profersor fue Cargado Correctamente',"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                    except IndexError:
                        mensaje=wx.MessageDialog(self,'Debe Cargar Correctamente el Horario del Profesor',"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                        mensaje.ShowModal()
                else:
                    mensaje=wx.MessageDialog(self,u'Se ha producido un Error.\nFaltan horas por cargar en el turno de la Mañana y/o Tarde, o La Hora de Entrada es mayor que la de Salida', "Error Cargando Profesor", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
            except lite.Error, e:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                logging.error('%s - [%s]'%(e, trace))
                mensaje=wx.MessageDialog(self,'El Profersor NO fue Cargado \n\nError: %s'%e,"Error Cargando Profesor", wx.OK|wx.ICON_HAND)
                mensaje.ShowModal()
                app.BD.cnn.rollback()
                app.BD.desconectar()


class panelEdicion (PanelEdicion):
    """
    clase destinada a manejar todo lo referente a la Edicion de Profesores
    """

    def m_choiceNombreProf_EdicionOnChoice( self, event ):
        if not self.m_choiceNombreProf_Edicion.GetCurrentSelection()==0:

            self.grid.Destroy()
            self.IniciarTablaHorarios()

            profSeleccionado=self.m_choiceNombreProf_Edicion.GetCurrentSelection()

            self.profeID=self.listaID_profesores[profSeleccionado-1]

            datosProfesor=app.BD.obtenerDatosProf(self.profeID)
            self.txtNombreProf_Edicion.SetValue(datosProfesor[1])
            self.tctApellidoProf_Edicion.SetValue(datosProfesor[2])
            self.txtCiProf_Edicion.SetValue(datosProfesor[0])
            self.txtTlfProf_Edicion.SetValue(datosProfesor[3])

            aN,mN,dN=map(int, datosProfesor[6].split('-'))
            nacimiento=wx.DateTimeFromDMY(dN,mN-1,aN)
            self.datePickerFecNacProf.SetValue(nacimiento)

            self.txtEmailProf.SetValue(datosProfesor[7])

            if datosProfesor[4]=='Si':
                self.radioBox_ProfActivo_Edicion.SetSelection(0)
            else:
                self.radioBox_ProfActivo_Edicion.SetSelection(1)

            if datosProfesor[5]==0:
                self.choiceTipoProfesor_Edicion.SetSelection(0)
            elif datosProfesor[5]==1:
                self.choiceTipoProfesor_Edicion.SetSelection(1)
            elif datosProfesor[5]==2:
                self.choiceTipoProfesor_Edicion.SetSelection(2)

            horas=app.BD.obtenerHorasProf(self.profeID)

            observacionesDiarias=app.BD.obtenerObservDiarias(self.profeID)

            listaHorasEntradaM=[]
            listaHorasSalidaM=[]
            listaHorasEntradaT=[]
            listaHorasSalidaT=[]
            for hora in horas:
                aI,mI,dI=map(int, hora[7].split('-'))
                ingreso=wx.DateTimeFromDMY(dI,mI-1,aI)
                self.datePickerFecIngresoProf.SetValue(ingreso)

                if hora[0]=='00:00:00':
                    listaHorasEntradaM.append('')
                else:
                    listaHorasEntradaM.append(hora[0])

                if hora[1]=='00:00:00':
                    listaHorasSalidaM.append('')
                else:
                    listaHorasSalidaM.append(hora[1])

                if hora[2]=='00:00:00':
                    listaHorasEntradaT.append('')
                else:
                    listaHorasEntradaT.append(hora[2])

                if hora[3]=='00:00:00':
                    listaHorasSalidaT.append('')
                else:
                    listaHorasSalidaT.append(hora[3])

            dias=app.BD.buscar_dia_Prof(self.profeID)

            catedras=app.BD.buscarIDCatedraDictada(self.profeID)
            nombrecatedrasProf=app.BD.buscarNomCatedraDictada(self.profeID)

            listanombrecatedrasProf=[]
            for cat in nombrecatedrasProf:
                listanombrecatedrasProf.append(cat[0])
            numerodecatedras=len(list(catedras))

            listaNomDias=[]
            if dias:
               for dia in dias:
                   for d in dia:
                       listaNomDias.append(d)
            if numerodecatedras:
                for i in range(len(listaNomDias)):
                    self.grid.SetCellValue(i, 0, unicode(listaNomDias[i]))
                    self.grid.SetCellValue(i, 1, unicode(listanombrecatedrasProf[i]))
                    self.grid.SetCellValue(i, 2, unicode(listaHorasEntradaM[i]))
                    self.grid.SetCellValue(i, 3, unicode(listaHorasSalidaM[i]))
                    self.grid.SetCellValue(i, 4, unicode(listaHorasEntradaT[i]))
                    self.grid.SetCellValue(i, 5, unicode(listaHorasSalidaT[i]))
                    self.grid.SetCellValue(i, 6, unicode(observacionesDiarias[i][0]))
        else:
            self.IniciarPanelHorasEdicion()


    def IniciarTablaHorarios(self):
        sizerPanelHorasProf = wx.BoxSizer( wx.VERTICAL )
        hSizerEntrada=wx.BoxSizer( wx.HORIZONTAL )

        self.grid = EditorsAndRenderersGrid(self.panelHorasProfEdicion, 15, 7)

        self.grid.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK,self.grid.showPopupMenu)
        self.grid.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK,self.grid.showPopupMenu2)

        self.grid.SetMargins(0,0)

        for i in range(self.grid.GetNumberRows()):
            self.grid.SetRowSize(i, 30)

        for i in range(self.grid.GetNumberCols()):
            self.grid.SetColSize(i, 163)

        self.grid.SetColLabelSize(20)

        self.filas=self.grid.GetNumberRows()
        self.columnas=self.grid.GetNumberCols()

        self.panelHorasProfEdicion.SetSizer( sizerPanelHorasProf )
        sizerPanelHorasProf.Add(hSizerEntrada,0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        hSizerEntrada.Add( self.grid, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        hSizerEntrada.Layout()
        self.panelHorasProfEdicion.Layout()
        self.Layout()


    def cargarChoiceEdicion(self):
        self.m_choiceNombreProf_Edicion.Clear()
        self.m_choiceNombreProf_Edicion.Append("Seleccionar Profesor...")
        self.m_choiceNombreProf_Edicion.SetSelection( 0 )

        profesores=app.BD.listarProfesores()

        self.listaID_profesores=[]
        for profesor in profesores:
            self.m_choiceNombreProf_Edicion.Append(profesor[1]+" "+profesor[2])
            self.listaID_profesores.append(profesor[0])

        self.IniciarTablaHorarios()

    def IniciarPanelHorasEdicion(self):

        self.txtNombreProf_Edicion.Clear()
        self.tctApellidoProf_Edicion.Clear()
        self.txtCiProf_Edicion.Clear()
        self.txtTlfProf_Edicion.Clear()
        self.datePickerFecNacProf.SetValue(wx.DateTime.Today())
        self.datePickerFecIngresoProf.SetValue(wx.DateTime.Today())
        self.txtEmailProf.Clear()
        self.radioBox_ProfActivo_Edicion.SetSelection(0)
        self.choiceTipoProfesor_Edicion.SetSelection( 0 )
        self.cargarChoiceEdicion()
        self.datePickerFecNacProf.SetRange(wx.DateTimeFromDMY(01,01,1920), wx.DateTime.Today())
        self.datePickerFecIngresoProf.SetRange(wx.DateTimeFromDMY(01,01,1920), wx.DateTime.Today())

    def btnEditProfOnButtonClick( self, event ):
        if not self.m_choiceNombreProf_Edicion.GetCurrentSelection()==0:
            self.validator=NotEmptyValidator()

            self.validator.SetWindow(self.txtNombreProf_Edicion)
            if self.validator.Validate(self.txtNombreProf_Edicion):
                validaNombre=True
            else:
                validaNombre=False

            self.validator.SetWindow(self.tctApellidoProf_Edicion)
            if self.validator.Validate(self.tctApellidoProf_Edicion):
                validaApellido=True
            else:
                validaApellido=False

            self.validator.SetWindow(self.txtCiProf_Edicion)
            if self.validator.Validate(self.txtCiProf_Edicion):
                validaCI=True
            else:
                validaCI=False

            self.validator.SetWindow(self.txtTlfProf_Edicion)
            if self.validator.Validate(self.txtTlfProf_Edicion):
                validaTel=True
            else:
                validaTel=False

            self.validator.SetWindow(self.txtEmailProf)
            if self.validator.Validate(self.txtEmailProf):
                validaMail=True
            else:
                validaMail=False

            activo=self.radioBox_ProfActivo_Edicion.GetStringSelection()

            #Cargo los nombres de catedras Seleccionadas, los dias y las horas correspondientes en tres listas respectivas
            self.diasSelecionados=[]
            self.nombreCatedrasSelecionadas=[]
            self.horasEntradaMSeleccionadas=[]
            self.horasSalidaMSeleccionadas=[]
            self.horasEntradaTSeleccionadas=[]
            self.horasSalidaTSeleccionadas=[]
            self.observaciones=[]
            horasTotales_Dia=[]
            horasTotales_M=[]
            horasTotales_T=[]

            if not (validaNombre and validaApellido and validaCI and validaTel and validaMail): #si la fila no esta vacia
                wx.MessageBox("No deben Haber campos Vacios", "Error")
                return False
            else:
                try:
                    nombre=string.capwords(self.txtNombreProf_Edicion.GetValue())
                    apellido=string.capwords(self.tctApellidoProf_Edicion.GetValue())
                    ci=self.txtCiProf_Edicion.GetValue()
                    telf=self.txtTlfProf_Edicion.GetValue()
                    fechaNacimiento=self.datePickerFecNacProf.GetValue().Format('%Y-%m-%d').encode()
                    fechaIngreso=self.datePickerFecIngresoProf.GetValue().Format('%Y-%m-%d').encode()
                    email=self.txtEmailProf.GetValue()
                    activo=self.radioBox_ProfActivo_Edicion.GetStringSelection()
                    tipoProf=self.choiceTipoProfesor_Edicion.GetCurrentSelection() #1 para profesor por horas, 2 para com. servicio y 3 para fijos

                    for i in range(self.filas):
                        if ((self.grid.GetCellValue(i,0)!='' and self.grid.GetCellValue(i,1)!='' and self.grid.GetCellValue(i,2)!='' and self.grid.GetCellValue(i,3)!='' and self.grid.GetCellValue(i,3) > self.grid.GetCellValue(i,2)) or
                           (self.grid.GetCellValue(i,0)!='' and self.grid.GetCellValue(i,1)!='' and self.grid.GetCellValue(i,4)!='' and self.grid.GetCellValue(i,5)!='' and self.grid.GetCellValue(i,5) > self.grid.GetCellValue(i,4)) or
                           (self.grid.GetCellValue(i,0)!='' and self.grid.GetCellValue(i,1)!='' and self.grid.GetCellValue(i,2)!='' and self.grid.GetCellValue(i,3)!='' and self.grid.GetCellValue(i,4)!='' and self.grid.GetCellValue(i,5)!='' and self.grid.GetCellValue(i,3) > self.grid.GetCellValue(i,2) and self.grid.GetCellValue(i,5) > self.grid.GetCellValue(i,4))) : #si la los dias y catedra no estan vacios
                            self.diasSelecionados.append(self.grid.GetCellValue(i,0))
                            self.nombreCatedrasSelecionadas.append(self.grid.GetCellValue(i, 1))
                            self.observaciones.append(self.grid.GetCellValue(i, 6))

                            if (self.grid.GetCellValue(i,2)!='' and self.grid.GetCellValue(i,3)!='') and (self.grid.GetCellValue(i,3) > self.grid.GetCellValue(i,2)): #si las horas de la manana no estan vacias
                                self.horasEntradaMSeleccionadas.append(self.grid.GetCellValue(i, 2))
                                self.horasSalidaMSeleccionadas.append(self.grid.GetCellValue(i, 3))
                            else:
                                self.horasEntradaMSeleccionadas.append('00:00:00')
                                self.horasSalidaMSeleccionadas.append('00:00:00')

                            if (self.grid.GetCellValue(i,4)!='' and self.grid.GetCellValue(i,5)!='') and (self.grid.GetCellValue(i,5) > self.grid.GetCellValue(i,4)): #si las horas de la tarde no estan vacias
                                self.horasEntradaTSeleccionadas.append(self.grid.GetCellValue(i, 4))
                                self.horasSalidaTSeleccionadas.append(self.grid.GetCellValue(i, 5))
                            else:
                                self.horasEntradaTSeleccionadas.append('00:00:00')
                                self.horasSalidaTSeleccionadas.append('00:00:00')

                    #catedras nuevas
                    if self.nombreCatedrasSelecionadas != [] and self.nombreCatedrasSelecionadas != [None]:
                        idCatedrasNuevas=[]
                        for c in self.nombreCatedrasSelecionadas:
                            idCatedrasNuevas.append(app.BD.buscarID_catedra(c))
                        idcatednueva=[]
                        for i in idCatedrasNuevas:
                            idcatednueva.append(i[0])

                    for h_M in range(len(self.horasEntradaMSeleccionadas)):
                        # string to time tuple INICIO
                        inicio_M=time.strptime(self.horasEntradaMSeleccionadas[h_M], "%H:%M:%S")
                        # string to time tuple FIN
                        fin_M=time.strptime(self.horasSalidaMSeleccionadas[h_M], "%H:%M:%S")

                        # time tuple to datetime object INICIO
                        t1_M = datetime(*inicio_M[0:6])
                        # time tuple to datetime object FIN
                        t2_M = datetime(*fin_M[0:6])

                        #Tiempo Transurido entre el INICIO y el FIN
                        horas_M=t2_M-t1_M
                        horasTotales_M.append(str(horas_M))

                    for h_T in range(len(self.horasEntradaTSeleccionadas)):
                        # string to time tuple INICIO
                        inicio_T=time.strptime(self.horasEntradaTSeleccionadas[h_T], "%H:%M:%S")
                        # string to time tuple FIN
                        fin_T=time.strptime(self.horasSalidaTSeleccionadas[h_T], "%H:%M:%S")

                        # time tuple to datetime object INICIO
                        t1_T = datetime(*inicio_T[0:6])
                        # time tuple to datetime object FIN
                        t2_T = datetime(*fin_T[0:6])

                        #Tiempo Transurido entre el INICIO y el FIN
                        horas_T=t2_T-t1_T
                        horasTotales_T.append(str(horas_T))

                    try:
                        for dia in self.diasSelecionados:
                            total = 0
                            totalM = 0
                            totalMT = ''
                            for horaM in  horasTotales_M:
                                hM, mM, sM = map(int, horaM.split(":"))
                                totalM += 3600*hM + 60*mM + sM

                            totalT = 0
                            for horaT in  horasTotales_T:
                                hT, mT, sT = map(int, horaT.split(":"))
                                totalT += 3600*hT + 60*mT + sT

                            total+=totalM+totalT
                            totalMT="%02d:%02d:%02d" % (total / 3600, total / 60 % 60, total % 60)
                            horasTotales_Dia.append(totalMT)
                    except:
                        mensaje=wx.MessageDialog(self,'Las Horas de Entrada deben ser menores a las de Salida_2', "Error Cargando Profesor", wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()

                    j=0
                    editar=True
                    elementos=[]
                    while editar and j <= self.filas-1:
                        if ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)!='' and self.grid.GetCellValue(j,3)!='' and self.grid.GetCellValue(j,3) > self.grid.GetCellValue(j,2)) and
                            (self.grid.GetCellValue(j,4)!='' and self.grid.GetCellValue(j,5)!='' and self.grid.GetCellValue(j,5) > self.grid.GetCellValue(j,4))): #si la los dias y catedra no estan vacios
                            editar=True
                            elementos.append(True)
                        elif ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)!='' and self.grid.GetCellValue(j,3)!='' and self.grid.GetCellValue(j,3) > self.grid.GetCellValue(j,2)) and
                              (self.grid.GetCellValue(j,4)=='' and self.grid.GetCellValue(j,5)=='')): #si la los dias y catedra no estan vacios
                            editar=True
                            elementos.append(True)
                        elif ((self.grid.GetCellValue(j,0)!='' and self.grid.GetCellValue(j,1)!='') and (self.grid.GetCellValue(j,2)=='' and self.grid.GetCellValue(j,3)=='') and
                              (self.grid.GetCellValue(j,4)!='' and self.grid.GetCellValue(j,5)!='' and self.grid.GetCellValue(j,5) > self.grid.GetCellValue(j,4))):
                            editar=True
                            elementos.append(True)
                        elif self.grid.GetCellValue(j,0)=='' and self.grid.GetCellValue(j,1)=='' and self.grid.GetCellValue(j,2)=='' and self.grid.GetCellValue(j,3)=='' and self.grid.GetCellValue(j,4)=='' and self.grid.GetCellValue(j,5)=='':
                            editar=True
                        else:
                            editar=False
                            elementos.append(False)
                        j=j+1

                    if not False in elementos and self.nombreCatedrasSelecionadas != [] and self.nombreCatedrasSelecionadas != [None]:
                        try:
                            app.BD.eliminarCatedras(self.profeID)
                            app.BD.modificarProfesorSinHorario(self.profeID, nombre, apellido, ci, fechaNacimiento, telf, email, activo, tipoProf)
                            app.BD.modificarHorarioProfesor(ci, fechaIngreso, idcatednueva, horasTotales_Dia, horasTotales_M, horasTotales_T, self.horasEntradaMSeleccionadas, self.horasSalidaMSeleccionadas, self.horasEntradaTSeleccionadas, self.horasSalidaTSeleccionadas, self.diasSelecionados, self.observaciones)
                            horasTotales_Dia=[]
                            self.txtNombreProf_Edicion.Clear()
                            self.tctApellidoProf_Edicion.Clear()
                            self.txtCiProf_Edicion.Clear()
                            self.txtTlfProf_Edicion.Clear()

                            self.datePickerFecNacProf.SetValue(wx.DateTime.Today())
                            self.datePickerFecIngresoProf.SetValue(wx.DateTime.Today())
                            self.txtEmailProf.Clear()

                            self.choiceTipoProfesor_Edicion.SetSelection( 0 )
                            self.grid.Destroy()
                            self.IniciarTablaHorarios()
                            mensaje=wx.MessageDialog(self,'Se modificaron los Datos Personales y el Horario del Profersor',"Editando Profesor", wx.OK|wx.ICON_INFORMATION)
                            mensaje.ShowModal()
                        except IndexError:
                            mensaje=wx.MessageDialog(self,'Debe Editar Correctamente el Horario del Profesor',"Cargando Profesor", wx.OK|wx.ICON_INFORMATION)
                            mensaje.ShowModal()
                    else:
                        mensaje=wx.MessageDialog(self,u'Se ha producido un Error.\nFaltan Días, Cátedras u horas por cargar en el turno de la Mañana y/o Tarde, o La Hora de Entrada es mayor que la de Salida', "Error Cargando Profesor", wx.OK|wx.ICON_HAND)
                        mensaje.ShowModal()
                except lite.Error, e:
                    exc_type, exc_value, exc_traceback = sys.exc_info()
                    trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
                    logging.error('%s - [%s]'%(e, trace))
                    mensaje=wx.MessageDialog(self,'El Profersor NO fue Editado \n\Error: %s'%e,"Error Editando Profesor", wx.OK|wx.ICON_HAND)
                    mensaje.ShowModal()
                    app.BD.cnn.rollback()
                    app.BD.desconectar()
        else:
            mensaje=wx.MessageDialog(self,'Debe seleccionar un profesor para editar',"Cargando Profesor", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

class FrameElimprof(FrameEliminarProf):
    """
    clase destinada a manejar todo lo referente a la Eliminacion de Profesores
    """

    def searchProfCtrlOnEnterWindow( self, event ):
        self.m_statusBarElim.SetStatusText(u"Ingrese el nombre, apellido o cédula del profesor a buscar")

    def searchProfCtrlOnCancelButton(self, event):
        self.searchProfCtrl.Clear()

    def FrameEliminarProfOnClose(self, event):
        self.MakeModal(False)
        self.Destroy()

    def iniciarListaProf(self):
        app.IconizarFrames(self)
        #Damos formato a la lista
        self.sizerListaProf = wx.BoxSizer(wx.VERTICAL)
        self.panelListaProf.SetSizer( self.sizerListaProf)

        self.ListadoProf  = CheckListCtrl(self.panelListaProf)
        self.ListadoProf.InsertColumn(0, u'Cédula de Identidad')
        self.ListadoProf.InsertColumn(1, 'Nombre')
        self.ListadoProf.InsertColumn(2, 'Apellido')

        self.ListadoProf.SetColumnWidth(0, 150)
        self.ListadoProf.SetColumnWidth(1, 150)
        self.ListadoProf.SetColumnWidth(2, 150)

        self.sizerListaProf.Add(self.ListadoProf, 1, wx.EXPAND | wx.TOP, 3)
        self.panelListaProf.Layout()
        self.ListadoProf.Layout()

    def cargarListadoDeProf(self):
        if self.searchProfCtrl.IsEmpty():
            todos=True
            lista=app.BD.listarProfesores()
        else:
            todos=False
            lista=app.BD.buscarProfesor(self.searchProfCtrl.GetValue())

        if not lista==[]:
            #Cargamos en la lista, el listado de usuarios obtenidos de la app.BD
            self.ListadoProf.Layout()
            if todos:
                for item in lista:
                    index = self.ListadoProf.InsertStringItem(sys.maxint, str(item[0]))
                    self.ListadoProf.SetStringItem(index, 1, item[1])
                    self.ListadoProf.SetStringItem(index, 2, item[2])
                self.searchProfCtrl.Clear()
            else:
                for item in lista:
                    index = self.ListadoProf.InsertStringItem(sys.maxint, str(item[0]))
                    self.ListadoProf.SetStringItem(index, 1, item[1])
                    self.ListadoProf.SetStringItem(index, 2, item[2])
                self.searchProfCtrl.Clear()
        else:
            self.ListadoProf.DeleteAllItems()
            mensaje=wx.MessageDialog(self,'No hay Resultados Coincidentes..!!',"Busqueda", wx.OK|wx.ICON_INFORMATION)
            mensaje.ShowModal()

    def btnCancelElimUsuOnButtonClick( self, event ):
        self.MakeModal(False)
        self.Destroy()

    def selTODOOnButtonClick( self, event ):
        num = self.ListadoProf.GetItemCount()
        for i in range(num):
            self.ListadoProf.CheckItem(i)

    def deSelTodoOnButtonClick( self, event ):
        num = self.ListadoProf.GetItemCount()
        for i in range(num):
            self.ListadoProf.CheckItem(i, False)

    def btnElimProfOnButtonClick( self, event ):
        listaBorrar=[]
        num = self.ListadoProf.GetItemCount()
        for i in range(num):
            if self.ListadoProf.IsChecked(i):
                listaBorrar.append(i)
        sorted(listaBorrar)
        listaBorrar.reverse()
        for j in listaBorrar:
                item= self.ListadoProf.GetItemText(j)
                app.BD.eliminarProfesor(item)
                self.ListadoProf.DeleteItem(j)
        mensaje=wx.MessageDialog(self,'Profesor(es) Eliminado(s)..!!',"Eliminando", wx.OK|wx.ICON_INFORMATION)
        mensaje.ShowModal()
        self.searchProfCtrl.Clear()

    def cargar(self):
        try:
            self.cargarListadoDeProf()
        except lite.Error, e:
            #error, sacamos dialogo
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,"Hubo un Error. %s" %e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()

    def searchProfCtrlOnSearchButton( self, event ):
        self.ListadoProf.DeleteAllItems()
        self.cargar()

    def searchProfCtrlOnTextEnter( self, event ):
        self.ListadoProf.DeleteAllItems()
        self.cargar()


class FPrincipal(FramePrincipal):
    """
    clase destinada a manejar todo lo referente a la Ventana Principal del Sistema
    """

    def cambiarContraseaOnMenuSelection(self, event):
        self.limpiarPantalla()
        ventanaCambioPass = CambioContrasena(self)
        app.IconizarFrames(ventanaCambioPass)
        ventanaCambioPass.Show()
        ventanaCambioPass.MakeModal()

    def licenciaOnMenuSelection( self, event ):
        licencia = os.path.normpath(os.path.join(licenceDir, "copying"))
        licenseText = open(licencia, "r")
        msg = licenseText.read()
        licenseText.close()
        msg2=wordwrap(msg, 500, wx.ClientDC(self))
        dlg = wx.lib.dialogs.ScrolledMessageDialog(self, msg2, "Licencia")
        dlg.ShowModal()

    def acercaDeOnMenuSelection(self, event):
        # First we create and fill the info object
        info = wx.AboutDialogInfo()
        info.Name = u"Sistema de Control de Nómina Docente"
        info.Version = "1.0"
        info.Description = wordwrap(
            u"El Sistema de Control de Nómina Docente permite la carga de docentes para el cálculo "
            u"de las horas en las que imparten cátedra, asi como la emision de los reportes respectivos ",
            350, wx.ClientDC(self))
        info.WebSite = ("http://www.fesnojiv.gob.ve", u"Página Web FUNDAMUSICAL Bolívar")
        info.Developers = [ "Lic. Mario Castro - mariocastro.pva@gmail.com" ]
        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)

    def IniciarSizers(self):
        self.carga=panelCarga(self)
        self.edicion=panelEdicion(self)
        self.bienvenida=panelBienvenida(self)
        self.asistencia=panelAsistencia(self)

        app.IconizarFrames(self)

        self.sizerFramePrincipal = wx.BoxSizer( wx.HORIZONTAL )
        self.SetSizer( self.sizerFramePrincipal )
        self.sizerFramePrincipal.Add(self.carga, 1, wx.EXPAND | wx.TOP, 3)
        self.sizerFramePrincipal.Add(self.edicion, 1, wx.EXPAND | wx.TOP, 3)
        self.sizerFramePrincipal.Add(self.asistencia, 1, wx.EXPAND | wx.TOP, 3)

    def ShowPanelCarga(self):
        if not self.editarProfesores.IsEnabled():
            self.editarProfesores.Enable(True)
            self.m_toolBar1.EnableTool(ID_EDITAR_PROFESORES, True)
        elif not self.cargarAsistencia.IsEnabled():
            self.cargarAsistencia.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_ASISTENCIA, True)

        self.cargarProfesor.Enable(False)
        self.m_toolBar1.EnableTool(ID_CARGAR_PROFESOR, False)

        if self.asistencia.IsShown():
            self.asistencia.Hide()
            self.asistencia.timeHoraEntrada24.Destroy()
            self.asistencia.timeHoraSalida24.Destroy()
            self.asistencia.spinHoraSalida.Destroy()
            self.asistencia.spinHoraEntrada.Destroy()
            self.carga.Show()
        elif self.edicion.IsShown():
            self.edicion.Hide()
            self.edicion.grid.Destroy()
            self.carga.Show()
        else:
            self.carga.Show()
            self.carga.grid.ClearGrid()
        self.carga.Layout()
        self.Layout()

    def ShowPanelEdicion(self):
        if not self.cargarProfesor.IsEnabled():
            self.cargarProfesor.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_PROFESOR, True)
        elif not self.cargarAsistencia.IsEnabled():
            self.cargarAsistencia.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_ASISTENCIA, True)

        self.editarProfesores.Enable(False)
        self.m_toolBar1.EnableTool(ID_EDITAR_PROFESORES, False)

        if self.asistencia.IsShown():
            self.asistencia.Hide()
            self.asistencia.timeHoraEntrada24.Destroy()
            self.asistencia.timeHoraSalida24.Destroy()
            self.asistencia.spinHoraSalida.Destroy()
            self.asistencia.spinHoraEntrada.Destroy()
            self.edicion.Show()
        elif self.carga.IsShown():
            self.carga.Hide()
            self.carga.grid.Destroy()
            self.edicion.Show()
        else:
            self.edicion.Show()
            self.edicion.grid.ClearGrid()
        self.edicion.Layout()
        self.Layout()

    def ShowPanelAsistencia(self):
        if not self.cargarProfesor.IsEnabled():
            self.cargarProfesor.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_PROFESOR, True)
        elif not self.editarProfesores.IsEnabled():
            self.editarProfesores.Enable(True)
            self.m_toolBar1.EnableTool(ID_EDITAR_PROFESORES, True)

        self.cargarAsistencia.Enable(False)
        self.m_toolBar1.EnableTool(ID_CARGAR_ASISTENCIA, False)

        if self.carga.IsShown():
            self.carga.Hide()
            self.carga.grid.Destroy()
            self.asistencia.Show()
        elif self.edicion.IsShown():
            self.edicion.Hide()
            self.edicion.grid.Destroy()
            self.asistencia.Show()
        else:
            self.asistencia.Show()
        self.asistencia.Layout()
        self.Layout()

    def FramePrincipalOnClose(self, event):
        self.Destroy()

    def SalirOnMenuSelection( self, event ):
        box=wx.MessageDialog(self, u"Realmente Desea Salir ?","Advertencia", wx.YES_NO | wx.ICON_QUESTION)
        if box.ShowModal()==wx.ID_YES:
            self.Close()

    def cargarProfesorOnMenuSelection( self, event ):
        self.bienvenida.Hide()
        try:
            app.BD.CargarCatedras()
        except lite.Error:
            app.BD.cnn.rollback()
        self.carga.IniciarPanelHoras()
        self.ShowPanelCarga()

    def editarProfesoresOnMenuSelection( self, event ):
        self.bienvenida.Hide()
        try:
            app.BD.CargarCatedras()
        except lite.Error:
            app.BD.cnn.rollback()
        self.edicion.IniciarPanelHorasEdicion()
        self.ShowPanelEdicion()

    def cargarAsistenciaOnMenuSelection( self, event ):
        self.limpiarPantalla()
        self.bienvenida.Hide()
        self.asistencia.IniciarHorasPanelAsistencia()
        self.ShowPanelAsistencia()

    def corregirAsistenciaOnMenuSelection(self, event):
        self.limpiarPantalla()
        ventanaCorreccionAsistencia=CoreccionAsistencia(self)
        app.IconizarFrames(ventanaCorreccionAsistencia)
        ventanaCorreccionAsistencia.listarProfesores()
        ventanaCorreccionAsistencia.Show()
        ventanaCorreccionAsistencia.MakeModal()

    def limpiarPantalla(self):
        if self.carga.IsShown():
            self.carga.Hide()
            self.carga.grid.Destroy()
            self.bienvenida.Show()
            self.cargarProfesor.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_PROFESOR, True)
        elif self.edicion.IsShown():
            self.edicion.Hide()
            self.edicion.grid.Destroy()
            self.bienvenida.Show()
            self.editarProfesores.Enable(True)
            self.m_toolBar1.EnableTool(ID_EDITAR_PROFESORES, True)
        elif self.asistencia.IsShown():
            self.asistencia.Hide()
            self.asistencia.timeHoraEntrada24.Destroy()
            self.asistencia.timeHoraSalida24.Destroy()
            self.asistencia.spinHoraSalida.Destroy()
            self.asistencia.spinHoraEntrada.Destroy()
            self.bienvenida.Show()
            self.cargarAsistencia.Enable(True)
            self.m_toolBar1.EnableTool(ID_CARGAR_ASISTENCIA, True)

        self.bienvenida.Layout()
        self.Layout()

    def eliminarProfesoresOnMenuSelection( self, event):
        self.limpiarPantalla()
        ventanaElimProf = FrameElimprof(self)
        app.IconizarFrames(ventanaElimProf)
        ventanaElimProf.Show()
        ventanaElimProf.iniciarListaProf()
        ventanaElimProf.MakeModal()

    def porProfesorOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaFicha = FrameFicha(self)
        app.IconizarFrames(ventanaFicha)
        ventanaFicha.iniciarPanelReporte()
        ventanaFicha.Show()
        ventanaFicha.listarProfesores()
        ventanaFicha.MakeModal()

    def generalOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaFichaGeneral=FichaGeneral(self)
        app.IconizarFrames(ventanaFichaGeneral)
        ventanaFichaGeneral.iniciarPanelReporte()
        ventanaFichaGeneral.Show()
        ventanaFichaGeneral.pdf.LoadFile(app.reporte.CrearFichaGeneral())
        ventanaFichaGeneral.panelReportFichaGen.Layout()
        ventanaFichaGeneral.Layout()
        ventanaFichaGeneral.MakeModal()

    def reportePorProfesorOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaReporteProf=reporteProf(self)
        app.IconizarFrames(ventanaReporteProf)
        ventanaReporteProf.iniciarPanelReporte()
        ventanaReporteProf.Show()
        ventanaReporteProf.comision=False
        ventanaReporteProf.listarProfesores()
        ventanaReporteProf.MakeModal()

    def reportePorCtedraOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaReporteCatedra=reporteCat(self)
        app.IconizarFrames(ventanaReporteCatedra)
        ventanaReporteCatedra.iniciarPanelReporte()
        ventanaReporteCatedra.Show()
        ventanaReporteCatedra.comision=False
        ventanaReporteCatedra.listarCat()
        ventanaReporteCatedra.MakeModal()

    def formaUnicaOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaFormaUnica=FormaUnica(self)
        app.IconizarFrames(ventanaFormaUnica)
        ventanaFormaUnica.iniciarPanelReporte()
        ventanaFormaUnica.Show()
        ventanaFormaUnica.comision=False
        ventanaFormaUnica.MakeModal()

    def formaUNicaCSOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaFormaUnicaCS=FormaUnica(self)
        app.IconizarFrames(ventanaFormaUnicaCS)
        ventanaFormaUnicaCS.iniciarPanelReporte()
        ventanaFormaUnicaCS.Show()
        ventanaFormaUnicaCS.comision=True
        ventanaFormaUnicaCS.MakeModal()

    def reportePorProfesorCSOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaReporteProfCS=reporteProf(self)
        app.IconizarFrames(ventanaReporteProfCS)
        ventanaReporteProfCS.iniciarPanelReporte()
        ventanaReporteProfCS.Show()
        ventanaReporteProfCS.comision=True
        ventanaReporteProfCS.listarProfesores()
        ventanaReporteProfCS.MakeModal()

    def reportePorCtedraCSOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaReporteCatedraCS=reporteCat(self)
        app.IconizarFrames(ventanaReporteCatedraCS)
        ventanaReporteCatedraCS.iniciarPanelReporte()
        ventanaReporteCatedraCS.Show()
        ventanaReporteCatedraCS.comision=True
        ventanaReporteCatedraCS.listarCat()
        ventanaReporteCatedraCS.MakeModal()

    def calculoDeProyeccionOnMenuSelection( self, event ):
        self.limpiarPantalla()
        ventanaProyeccion=Proyeccion(self)
        app.IconizarFrames(ventanaProyeccion)
        ventanaProyeccion.iniciarPanelReporte()
        ventanaProyeccion.Show()
        ventanaProyeccion.listarProfesores()
        ventanaProyeccion.MakeModal()

class FInicio(FrameLogin):
    """
    clase destinada a manejar todo lo referente a la ventana de Login del Sistema
    """

    def IniciarApp(self):
        try:
            self.usuario=string.lower(self.txtNomUsuario.GetValue())
            self.password=self.txtPass.GetValue()
            hashClave = hashlib.md5()
            hashClave.update(self.txtPass.GetValue())

            #Verificamos el Usuario Correcto en la app.BD

            sesion=app.BD.verificaUsuario(self.usuario,self.password)
            #sesion=app.BD.verificaUsuario(self.usuario,hashClave.hexdigest())
            if sesion:
                self.IdUconectado=sesion[0]
                self.nomUconectado=sesion[1]
                ventanaPrincipal = FPrincipal(None)
                app.SetTopWindow(ventanaPrincipal)
                ventanaPrincipal.Show()
                ventanaPrincipal.IniciarSizers()
                self.Close()
            else:
                mensajeError=wx.MessageDialog(self, 'Este usuario no existe. \n\nDesea Intentar de nuevo?.',"Error", wx.YES_NO|wx.ICON_QUESTION)
                if mensajeError.ShowModal()==wx.ID_NO:
                    self.Close()
                else:
                    self.txtNomUsuario.Clear()
                    self.txtPass.Clear()
                    self.txtNomUsuario.SetFocus()
        except lite.Error, e:
            #error, sacamos dialogo y decimos que hagan configuracion
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('%s - [%s]'%(e, trace))
            mensaje=wx.MessageDialog(self,u'Error en la conección a la base de Datos. \nIntente de nuevo o haga click en "Cancelar" para salir. \n\n%s'%e,"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNomUsuario.Clear()
            self.txtPass.Clear()
            self.txtNomUsuario.SetFocus()
            app.BD.cnn.rollback()
            app.BD.desconectar()
        except UnicodeEncodeError:
            #error, sacamos dialogo y decimos que hagan configuracion
            mensaje=wx.MessageDialog(self,u'La contraseña no debe contener caracteres especiales. \n\n',"Error", wx.OK|wx.ICON_HAND)
            mensaje.ShowModal()
            self.txtNomUsuario.Clear()
            self.txtPass.Clear()
            self.txtNomUsuario.SetFocus()

    def iniciarAplicacionOnButtonClick(self, event):
        self.IniciarApp()

    def txtPassOnTextEnter(self, event):
        self.IniciarApp()

    def CancelarAplicacionOnButtonClick(self, event):
        box = wx.MessageDialog(self, "Realmente Desea Salir ?", "Advertencia", wx.YES_NO | wx.ICON_QUESTION)
        if box.ShowModal() == wx.ID_YES:
            self.Close()

    def txtContrasenaOnTextEnter(self, event):
        self.IniciarApp()

    def btnRecordarPassOnButtonClick( self, event ):
        ventanaRecordarPass=RecuerdaPass(self)
        ventanaRecordarPass.Show()

#####################################################
## DECLARACION DEL APPLICATION OBJECT
#####################################################
class App(wx.App):

    def __init__(self, redirect=False, filename='log.log'):
        wx.App.__init__(self, redirect, filename)

    def mostrarSplash(self):
        """
        Muestra un Splash de Bienvenida
        """
        pn = os.path.normpath(os.path.join(bitmapDir, "LogoSistema.jpg"))
        image = wx.Image(pn, wx.BITMAP_TYPE_JPEG)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 3000, None, -1)
        wx.Yield()

    def limpiarDirectorios(self):
        listaDir=os.listdir(tempDir)
        if listaDir != []:
            for item in listaDir:
                if not item=='readme.txt':
                    os.remove(os.path.join(tempDir, item))

    def IconizarFrames(self, win):
        icon = os.path.normpath(os.path.join(iconDir, "favicon.ico"))

        favicon = wx.Icon(icon, wx.BITMAP_TYPE_ICO, 16, 16)
        wx.Frame.SetIcon(win, favicon)


    def OnInit(self):

        try:
            self.BD=ModeloBD()
            self.reporte=Reportes()


            if self.BD.ContarRegistrosAdmin() == 0:
                mywiz = WizardInicio(None)
                mywiz.FitToPage(mywiz.pagina1Wizard)
                mywiz.RunWizard(mywiz.pagina1Wizard)
                mywiz.txtNucleo.SetFocus()
                mywiz.Destroy()
            else:
                self.mostrarSplash()
                self.frameInicio = FInicio(None)
                self.IconizarFrames(self.frameInicio)
                self.frameInicio.Show()
                self.frameInicio.txtNomUsuario.SetFocus()
            return True
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            trace=repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
            logging.error('[%s]'%(trace))
            return False

    def OnExit(self):
        self.limpiarDirectorios()

#######################
########LLAMADA PRINCIPAL
#######################

if __name__ == '__main__':
    logging.basicConfig(filename='logSistemaNomina.log', format='%(asctime)s : %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    app = App(redirect=False)
    app.MainLoop()
