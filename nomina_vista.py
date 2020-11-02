# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb  9 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.wizard

ID_CAMBIAR_CONTRASEA = 1000
ID_SALIR = 1001
ID_CARGAR_ASISTENCIA = 1002
ID_CORREGIR_ASISTENCIA = 1003
ID_CARGAR_PROFESOR = 1004
ID_EDITAR_PROFESORES = 1005
ID_ELIMINAR_PROFESORES = 1006
ID_FORMA_UNICA = 1007
ID_REPORTE_POR_PROFESOR = 1008
ID_REPORTE_POR_CTEDRA = 1009
ID_FORMA_UNICA_CS = 1010
ID_REPORTE_POR_PROFESOR_CS = 1011
ID_REPORTE_POR_CTEDRA_CS = 1012
ID_FICHA_POR_PROFESOR = 1013
ID_FICHA_GENERAL = 1014
ID_CLCULO_DE_PROYECCIN = 1015
ID_ACERCA_DE = 1016
ID_LICENCIA = 1017

###########################################################################
## Class FrameLogin
###########################################################################

class FrameLogin ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Control de Nómina Docente - Login", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Nombre de usuario" ), wx.VERTICAL )
		
		self.txtNomUsuario = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.txtNomUsuario, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( sbSizer1 )
		self.m_panel2.Layout()
		sbSizer1.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel3 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Contraseña" ), wx.VERTICAL )
		
		self.txtPass = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		sbSizer2.Add( self.txtPass, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( sbSizer2 )
		self.m_panel3.Layout()
		sbSizer2.Fit( self.m_panel3 )
		bSizer4.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 1, 2, 0, 0 )
		
		self.iniciarAplicacion = wx.Button( self.m_panel4, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.iniciarAplicacion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.CancelarAplicacion = wx.Button( self.m_panel4, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.CancelarAplicacion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer4 )
		self.m_panel4.Layout()
		gSizer4.Fit( self.m_panel4 )
		bSizer4.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel61 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer69.Add( self.m_panel61, 1, wx.ALL, 5 )
		
		self.btnRecordarPass = wx.Button( self.m_panel9, wx.ID_ANY, u"Olvidó su Contraseña?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer69.Add( self.btnRecordarPass, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer69, 0, wx.EXPAND, 5 )
		
		
		self.m_panel9.SetSizer( bSizer4 )
		self.m_panel9.Layout()
		bSizer4.Fit( self.m_panel9 )
		gSizer3.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtPass.Bind( wx.EVT_TEXT_ENTER, self.txtPassOnTextEnter )
		self.iniciarAplicacion.Bind( wx.EVT_BUTTON, self.iniciarAplicacionOnButtonClick )
		self.CancelarAplicacion.Bind( wx.EVT_BUTTON, self.CancelarAplicacionOnButtonClick )
		self.btnRecordarPass.Bind( wx.EVT_BUTTON, self.btnRecordarPassOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtPassOnTextEnter( self, event ):
		event.Skip()
	
	def iniciarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def CancelarAplicacionOnButtonClick( self, event ):
		event.Skip()
	
	def btnRecordarPassOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Control de Nómina Docente", pos = wx.DefaultPosition, size = wx.Size( 1300,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.administracin = wx.Menu()
		self.cambiarContrasea = wx.MenuItem( self.administracin, ID_CAMBIAR_CONTRASEA, u"Cambiar Contraseña", u"Cambio de Contraseña para el Usuario Actual", wx.ITEM_NORMAL )
		self.cambiarContrasea.SetBitmap( wx.Bitmap( u"icon/page-pencil-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.administracin.AppendItem( self.cambiarContrasea )
		
		self.salir = wx.MenuItem( self.administracin, ID_SALIR, u"Salir", u"Salir de la aplicación", wx.ITEM_NORMAL )
		self.salir.SetBitmap( wx.Bitmap( u"icon/salir.png", wx.BITMAP_TYPE_ANY ) )
		self.administracin.AppendItem( self.salir )
		
		self.m_menubar2.Append( self.administracin, u"Administración" ) 
		
		self.menuAsistencia = wx.Menu()
		self.cargarAsistencia = wx.MenuItem( self.menuAsistencia, ID_CARGAR_ASISTENCIA, u"Cargar Asistencia", u"Seleccione para cargar la asistencia de los profesores", wx.ITEM_NORMAL )
		self.cargarAsistencia.SetBitmap( wx.Bitmap( u"icon/asistencia.png", wx.BITMAP_TYPE_ANY ) )
		self.menuAsistencia.AppendItem( self.cargarAsistencia )
		
		self.corregirAsistencia = wx.MenuItem( self.menuAsistencia, ID_CORREGIR_ASISTENCIA, u"Corregir Asistencia", u"Seleccione para Corregir Horas de Asistencia", wx.ITEM_NORMAL )
		self.corregirAsistencia.SetBitmap( wx.Bitmap( u"icon/note-todo-list-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.menuAsistencia.AppendItem( self.corregirAsistencia )
		
		self.m_menubar2.Append( self.menuAsistencia, u"Asistencia" ) 
		
		self.MenuProfesores = wx.Menu()
		self.cargarProfesor = wx.MenuItem( self.MenuProfesores, ID_CARGAR_PROFESOR, u"Cargar Profesor", u"Seleccione para cargar uno o mas profesores al sistema", wx.ITEM_NORMAL )
		self.cargarProfesor.SetBitmap( wx.Bitmap( u"icon/agregar_usuario.png", wx.BITMAP_TYPE_ANY ) )
		self.MenuProfesores.AppendItem( self.cargarProfesor )
		
		self.editarProfesores = wx.MenuItem( self.MenuProfesores, ID_EDITAR_PROFESORES, u"Editar Profesores", u"Selecione para editar los datos de los profesores", wx.ITEM_NORMAL )
		self.editarProfesores.SetBitmap( wx.Bitmap( u"icon/editar.png", wx.BITMAP_TYPE_ANY ) )
		self.MenuProfesores.AppendItem( self.editarProfesores )
		
		self.eliminarProfesores = wx.MenuItem( self.MenuProfesores, ID_ELIMINAR_PROFESORES, u"Eliminar Profesores", u"Seleccione para eliminar uno o mas profesores del sistema", wx.ITEM_NORMAL )
		self.eliminarProfesores.SetBitmap( wx.Bitmap( u"icon/remover_usuario.png", wx.BITMAP_TYPE_ANY ) )
		self.MenuProfesores.AppendItem( self.eliminarProfesores )
		
		self.m_menubar2.Append( self.MenuProfesores, u"Profesores" ) 
		
		self.menuReportes = wx.Menu()
		self.reportesProfesoresPorHoraYFijos = wx.Menu()
		self.formaUnica = wx.MenuItem( self.reportesProfesoresPorHoraYFijos, ID_FORMA_UNICA, u"Forma Única", u"Genera la Forma Única", wx.ITEM_NORMAL )
		self.formaUnica.SetBitmap( wx.Bitmap( u"icon/rep_formaU.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorHoraYFijos.AppendItem( self.formaUnica )
		
		self.reportePorProfesor = wx.MenuItem( self.reportesProfesoresPorHoraYFijos, ID_REPORTE_POR_PROFESOR, u"Reporte por Profesor", u"Genera un reporte por Profesor Seleccionado", wx.ITEM_NORMAL )
		self.reportePorProfesor.SetBitmap( wx.Bitmap( u"icon/rep_catedra.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorHoraYFijos.AppendItem( self.reportePorProfesor )
		
		self.reportePorCtedra = wx.MenuItem( self.reportesProfesoresPorHoraYFijos, ID_REPORTE_POR_CTEDRA, u"Reporte por Cátedra", u"Genera un reporte por Cátedra Seleccionada", wx.ITEM_NORMAL )
		self.reportePorCtedra.SetBitmap( wx.Bitmap( u"icon/rep_Prof.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorHoraYFijos.AppendItem( self.reportePorCtedra )
		
		self.menuReportes.AppendSubMenu( self.reportesProfesoresPorHoraYFijos, u"Reportes Profesores por Hora y Fijos" )
		
		self.reportesProfesoresPorComisinDeServicio = wx.Menu()
		self.formaUNicaCS = wx.MenuItem( self.reportesProfesoresPorComisinDeServicio, ID_FORMA_UNICA_CS, u"Forma Única", wx.EmptyString, wx.ITEM_NORMAL )
		self.formaUNicaCS.SetBitmap( wx.Bitmap( u"icon/rep_formaU.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorComisinDeServicio.AppendItem( self.formaUNicaCS )
		
		self.reportePorProfesorCS = wx.MenuItem( self.reportesProfesoresPorComisinDeServicio, ID_REPORTE_POR_PROFESOR_CS, u"Reporte por Profesor", wx.EmptyString, wx.ITEM_NORMAL )
		self.reportePorProfesorCS.SetBitmap( wx.Bitmap( u"icon/rep_catedra.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorComisinDeServicio.AppendItem( self.reportePorProfesorCS )
		
		self.reportePorCtedraCS = wx.MenuItem( self.reportesProfesoresPorComisinDeServicio, ID_REPORTE_POR_CTEDRA_CS, u"Reporte por Cátedra", wx.EmptyString, wx.ITEM_NORMAL )
		self.reportePorCtedraCS.SetBitmap( wx.Bitmap( u"icon/rep_Prof.png", wx.BITMAP_TYPE_ANY ) )
		self.reportesProfesoresPorComisinDeServicio.AppendItem( self.reportePorCtedraCS )
		
		self.menuReportes.AppendSubMenu( self.reportesProfesoresPorComisinDeServicio, u"Reportes Profesores por Comisión de Servicio" )
		
		self.fichaDocente = wx.Menu()
		self.fichaPorProfesor = wx.MenuItem( self.fichaDocente, ID_FICHA_POR_PROFESOR, u"Ficha por Profesor", u"Seleccione para generar la Ficha de un Profesor", wx.ITEM_NORMAL )
		self.fichaDocente.AppendItem( self.fichaPorProfesor )
		
		self.fichaGeneral = wx.MenuItem( self.fichaDocente, ID_FICHA_GENERAL, u"Ficha General", u"Seleccione para generar un Reporte con los Datos de todos los Profesores", wx.ITEM_NORMAL )
		self.fichaDocente.AppendItem( self.fichaGeneral )
		
		self.menuReportes.AppendSubMenu( self.fichaDocente, u"Ficha Docente" )
		
		self.m_menubar2.Append( self.menuReportes, u"Reportes" ) 
		
		self.proyecciones = wx.Menu()
		self.calculoDeProyeccion = wx.MenuItem( self.proyecciones, ID_CLCULO_DE_PROYECCIN, u"Cálculo de Proyección", u"Seleccione para realizar el Cálculo de la proyeccion de Asistencia Docente", wx.ITEM_NORMAL )
		self.calculoDeProyeccion.SetBitmap( wx.Bitmap( u"icon/arrow-branch-bgr-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.proyecciones.AppendItem( self.calculoDeProyeccion )
		
		self.m_menubar2.Append( self.proyecciones, u"Proyecciones" ) 
		
		self.ayuda = wx.Menu()
		self.acercaDe = wx.MenuItem( self.ayuda, ID_ACERCA_DE, u"Acerca de...", u"Información acerca de la Aplicación", wx.ITEM_NORMAL )
		self.acercaDe.SetBitmap( wx.Bitmap( u"icon/comment-16-ns.png", wx.BITMAP_TYPE_ANY ) )
		self.ayuda.AppendItem( self.acercaDe )
		
		self.licencia = wx.MenuItem( self.ayuda, ID_LICENCIA, u"Licencia", u"Información de Licencia \"GNU GENERAL PUBLIC LICENSE\"", wx.ITEM_NORMAL )
		self.licencia.SetBitmap( wx.Bitmap( u"icon/licencia.png", wx.BITMAP_TYPE_ANY ) )
		self.ayuda.AppendItem( self.licencia )
		
		self.m_menubar2.Append( self.ayuda, u"Ayuda" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar1.AddLabelTool( ID_CARGAR_ASISTENCIA, u"Cargar Asistencia", wx.Bitmap( u"icon/page-forum-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga click  para cargar la asistencia de los profesores", u"Haga click  para cargar la asistencia de los profesores", None ) 
		
		self.m_toolBar1.AddLabelTool( ID_CORREGIR_ASISTENCIA, u"tool", wx.Bitmap( u"icon/note-todo-list-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga Click para Corregir Horas de Asistencia", u"Haga Click para Corregir Horas de Asistencia", None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolBar1.AddLabelTool( ID_CARGAR_PROFESOR, u"Agregar Profesor", wx.Bitmap( u"icon/person-plus-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga click para Agregar uno o más Profesores", u"Haga click para Agregar uno o más Profesores", None ) 
		
		self.m_toolBar1.AddLabelTool( ID_EDITAR_PROFESORES, u"Editar Profesor", wx.Bitmap( u"icon/page-pencil-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga click para editar los datos de uno o más Profesores", u"Haga click para editar los datos de uno o más Profesores", None ) 
		
		self.m_toolBar1.AddLabelTool( ID_ELIMINAR_PROFESORES, u"Eliminar Profesor", wx.Bitmap( u"icon/person-minus-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Haga click para Eliminar uno o más Profesores", u"Haga click para Eliminar uno o más Profesores", None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_toolBar1.AddLabelTool( ID_CLCULO_DE_PROYECCIN, u"tool", wx.Bitmap( u"icon/arrow-branch-bgr-24-ns.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Seleccione para realizar el Cálculo de la proyeccion de Asistencia Docente", u"Seleccione para realizar el Cálculo de la proyeccion de Asistencia Docente", None ) 
		
		self.m_toolBar1.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FramePrincipalOnClose )
		self.Bind( wx.EVT_MENU, self.cambiarContraseaOnMenuSelection, id = self.cambiarContrasea.GetId() )
		self.Bind( wx.EVT_MENU, self.SalirOnMenuSelection, id = self.salir.GetId() )
		self.Bind( wx.EVT_MENU, self.cargarAsistenciaOnMenuSelection, id = self.cargarAsistencia.GetId() )
		self.Bind( wx.EVT_MENU, self.corregirAsistenciaOnMenuSelection, id = self.corregirAsistencia.GetId() )
		self.Bind( wx.EVT_MENU, self.cargarProfesorOnMenuSelection, id = self.cargarProfesor.GetId() )
		self.Bind( wx.EVT_MENU, self.editarProfesoresOnMenuSelection, id = self.editarProfesores.GetId() )
		self.Bind( wx.EVT_MENU, self.eliminarProfesoresOnMenuSelection, id = self.eliminarProfesores.GetId() )
		self.Bind( wx.EVT_MENU, self.formaUnicaOnMenuSelection, id = self.formaUnica.GetId() )
		self.Bind( wx.EVT_MENU, self.reportePorProfesorOnMenuSelection, id = self.reportePorProfesor.GetId() )
		self.Bind( wx.EVT_MENU, self.reportePorCtedraOnMenuSelection, id = self.reportePorCtedra.GetId() )
		self.Bind( wx.EVT_MENU, self.formaUNicaCSOnMenuSelection, id = self.formaUNicaCS.GetId() )
		self.Bind( wx.EVT_MENU, self.reportePorProfesorCSOnMenuSelection, id = self.reportePorProfesorCS.GetId() )
		self.Bind( wx.EVT_MENU, self.reportePorCtedraCSOnMenuSelection, id = self.reportePorCtedraCS.GetId() )
		self.Bind( wx.EVT_MENU, self.porProfesorOnMenuSelection, id = self.fichaPorProfesor.GetId() )
		self.Bind( wx.EVT_MENU, self.generalOnMenuSelection, id = self.fichaGeneral.GetId() )
		self.Bind( wx.EVT_MENU, self.calculoDeProyeccionOnMenuSelection, id = self.calculoDeProyeccion.GetId() )
		self.Bind( wx.EVT_MENU, self.acercaDeOnMenuSelection, id = self.acercaDe.GetId() )
		self.Bind( wx.EVT_MENU, self.licenciaOnMenuSelection, id = self.licencia.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FramePrincipalOnClose( self, event ):
		event.Skip()
	
	def cambiarContraseaOnMenuSelection( self, event ):
		event.Skip()
	
	def SalirOnMenuSelection( self, event ):
		event.Skip()
	
	def cargarAsistenciaOnMenuSelection( self, event ):
		event.Skip()
	
	def corregirAsistenciaOnMenuSelection( self, event ):
		event.Skip()
	
	def cargarProfesorOnMenuSelection( self, event ):
		event.Skip()
	
	def editarProfesoresOnMenuSelection( self, event ):
		event.Skip()
	
	def eliminarProfesoresOnMenuSelection( self, event ):
		event.Skip()
	
	def formaUnicaOnMenuSelection( self, event ):
		event.Skip()
	
	def reportePorProfesorOnMenuSelection( self, event ):
		event.Skip()
	
	def reportePorCtedraOnMenuSelection( self, event ):
		event.Skip()
	
	def formaUNicaCSOnMenuSelection( self, event ):
		event.Skip()
	
	def reportePorProfesorCSOnMenuSelection( self, event ):
		event.Skip()
	
	def reportePorCtedraCSOnMenuSelection( self, event ):
		event.Skip()
	
	def porProfesorOnMenuSelection( self, event ):
		event.Skip()
	
	def generalOnMenuSelection( self, event ):
		event.Skip()
	
	def calculoDeProyeccionOnMenuSelection( self, event ):
		event.Skip()
	
	def acercaDeOnMenuSelection( self, event ):
		event.Skip()
	
	def licenciaOnMenuSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameEliminarProf
###########################################################################

class FrameEliminarProf ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Busqueda y Eliminación de Profesores", pos = wx.DefaultPosition, size = wx.Size( 570,316 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerEliminarProf = wx.BoxSizer( wx.VERTICAL )
		
		self.panelBusquedaProf = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerBusquedaProf = wx.BoxSizer( wx.VERTICAL )
		
		self.searchProfCtrl = wx.SearchCtrl( self.panelBusquedaProf, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PROCESS_ENTER )
		self.searchProfCtrl.ShowSearchButton( True )
		self.searchProfCtrl.ShowCancelButton( False )
		self.searchProfCtrl.SetToolTipString( u"Ingrese el nombre, apellido o cédula del profesor a buscar" )
		
		sizerBusquedaProf.Add( self.searchProfCtrl, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.panelBusquedaProf.SetSizer( sizerBusquedaProf )
		self.panelBusquedaProf.Layout()
		sizerBusquedaProf.Fit( self.panelBusquedaProf )
		sizerEliminarProf.Add( self.panelBusquedaProf, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelListaProf = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sizerEliminarProf.Add( self.panelListaProf, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.panelBtnElimProf = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		sizerbotElimProf = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnElimProf = wx.Button( self.panelBtnElimProf, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerbotElimProf.Add( self.btnElimProf, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.btnCancelElimProf = wx.Button( self.panelBtnElimProf, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerbotElimProf.Add( self.btnCancelElimProf, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		sizerbotElimProf.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.selTODO = wx.Button( self.panelBtnElimProf, wx.ID_ANY, u"Seleccionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerbotElimProf.Add( self.selTODO, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.deSelTodo = wx.Button( self.panelBtnElimProf, wx.ID_ANY, u"De-Seleccionar Todo", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerbotElimProf.Add( self.deSelTodo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.panelBtnElimProf.SetSizer( sizerbotElimProf )
		self.panelBtnElimProf.Layout()
		sizerbotElimProf.Fit( self.panelBtnElimProf )
		sizerEliminarProf.Add( self.panelBtnElimProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerEliminarProf )
		self.Layout()
		self.m_statusBarElim = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameEliminarProfOnClose )
		self.searchProfCtrl.Bind( wx.EVT_ENTER_WINDOW, self.searchProfCtrlOnEnterWindow )
		self.searchProfCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchProfCtrlOnSearchButton )
		self.searchProfCtrl.Bind( wx.EVT_TEXT_ENTER, self.searchProfCtrlOnTextEnter )
		self.btnElimProf.Bind( wx.EVT_BUTTON, self.btnElimProfOnButtonClick )
		self.btnCancelElimProf.Bind( wx.EVT_BUTTON, self.btnCancelElimUsuOnButtonClick )
		self.selTODO.Bind( wx.EVT_BUTTON, self.selTODOOnButtonClick )
		self.deSelTodo.Bind( wx.EVT_BUTTON, self.deSelTodoOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameEliminarProfOnClose( self, event ):
		event.Skip()
	
	def searchProfCtrlOnEnterWindow( self, event ):
		event.Skip()
	
	def searchProfCtrlOnSearchButton( self, event ):
		event.Skip()
	
	def searchProfCtrlOnTextEnter( self, event ):
		event.Skip()
	
	def btnElimProfOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelElimUsuOnButtonClick( self, event ):
		event.Skip()
	
	def selTODOOnButtonClick( self, event ):
		event.Skip()
	
	def deSelTodoOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelAsistencia
###########################################################################

class PanelAsistencia ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 790,531 ), style = wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		
		self.Hide()
		
		sizerPanelAsistencia = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Asistencia de Profesores", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( 15, 74, 90, 92, False, "Tahoma" ) )
		
		sizerPanelAsistencia.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelAsistProf = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 790,-1 ), wx.TAB_TRAVERSAL )
		sizerpanelAsistProf = wx.BoxSizer( wx.VERTICAL )
		
		sbSizerNomProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Profesor" ), wx.VERTICAL )
		
		m_choiceNomProfChoices = [ u"Seleccionar Profesor" ]
		self.m_choiceNomProf = wx.Choice( self.panelAsistProf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNomProfChoices, 0 )
		self.m_choiceNomProf.SetSelection( 0 )
		sbSizerNomProf.Add( self.m_choiceNomProf, 0, wx.ALL, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerNomProf, 0, wx.EXPAND, 5 )
		
		sbSizerCatedraProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Cátedra" ), wx.VERTICAL )
		
		m_choiceCatedraProfChoices = [ u"Seleccionar Cátedra" ]
		self.m_choiceCatedraProf = wx.Choice( self.panelAsistProf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceCatedraProfChoices, 0 )
		self.m_choiceCatedraProf.SetSelection( 0 )
		sbSizerCatedraProf.Add( self.m_choiceCatedraProf, 0, wx.ALL, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerCatedraProf, 0, wx.EXPAND, 5 )
		
		sbSizerFechaAsistProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Fecha de Asistencia" ), wx.VERTICAL )
		
		self.datePickerFechaAsistencia = wx.DatePickerCtrl( self.panelAsistProf, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		sbSizerFechaAsistProf.Add( self.datePickerFechaAsistencia, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerFechaAsistProf, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizerAsistenciaIncompleta = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Asistencia Completa" ), wx.VERTICAL )
		
		bSizer109 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_radioBtnAsistenciaCompleta = wx.RadioButton( self.panelAsistProf, wx.ID_ANY, u"Si", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtnAsistenciaCompleta.SetValue( True ) 
		bSizer109.Add( self.m_radioBtnAsistenciaCompleta, 0, wx.ALL, 5 )
		
		
		bSizer109.AddSpacer( ( 50, 0), 1, wx.EXPAND, 5 )
		
		self.m_radioBtnAsistenciaIncompleta = wx.RadioButton( self.panelAsistProf, wx.ID_ANY, u"No", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer109.Add( self.m_radioBtnAsistenciaIncompleta, 0, wx.ALL, 5 )
		
		
		sbSizerAsistenciaIncompleta.Add( bSizer109, 0, 0, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerAsistenciaIncompleta, 0, wx.EXPAND, 5 )
		
		sbSizerHoraEntradaProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Hora de Entrada" ), wx.HORIZONTAL )
		
		self.panelHoraEntradaProf = wx.Panel( self.panelAsistProf, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), wx.TAB_TRAVERSAL )
		sbSizerHoraEntradaProf.Add( self.panelHoraEntradaProf, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerHoraEntradaProf, 0, wx.EXPAND, 5 )
		
		sbSizerHoraSalidaProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Hora de Salida" ), wx.HORIZONTAL )
		
		self.panelHoraSalidaProf = wx.Panel( self.panelAsistProf, wx.ID_ANY, wx.DefaultPosition, wx.Size( 700,-1 ), wx.TAB_TRAVERSAL )
		sbSizerHoraSalidaProf.Add( self.panelHoraSalidaProf, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerHoraSalidaProf, 0, wx.EXPAND, 5 )
		
		sbSizerObservProf = wx.StaticBoxSizer( wx.StaticBox( self.panelAsistProf, wx.ID_ANY, u"Observaciones" ), wx.VERTICAL )
		
		self.txtObservAsistProf = wx.TextCtrl( self.panelAsistProf, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,80 ), wx.TE_MULTILINE )
		sbSizerObservProf.Add( self.txtObservAsistProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sizerpanelAsistProf.Add( sbSizerObservProf, 0, wx.EXPAND, 5 )
		
		self.panelBtnCargaAsistProf = wx.Panel( self.panelAsistProf, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBtnCargaAsistProf = wx.BoxSizer( wx.VERTICAL )
		
		self.btnCargaAsistenciaProf = wx.Button( self.panelBtnCargaAsistProf, wx.ID_ANY, u"Cargar Asistencia", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.btnCargaAsistenciaProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelBtnCargaAsistProf.Add( self.btnCargaAsistenciaProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelBtnCargaAsistProf.SetSizer( sizerPanelBtnCargaAsistProf )
		self.panelBtnCargaAsistProf.Layout()
		sizerPanelBtnCargaAsistProf.Fit( self.panelBtnCargaAsistProf )
		sizerpanelAsistProf.Add( self.panelBtnCargaAsistProf, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelAsistProf.SetSizer( sizerpanelAsistProf )
		self.panelAsistProf.Layout()
		sizerPanelAsistencia.Add( self.panelAsistProf, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerPanelAsistencia )
		self.Layout()
		
		# Connect Events
		self.m_choiceNomProf.Bind( wx.EVT_CHOICE, self.m_choiceNomProfOnChoice )
		self.m_radioBtnAsistenciaCompleta.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtnAsistenciaCompletaOnRadioButton )
		self.m_radioBtnAsistenciaIncompleta.Bind( wx.EVT_RADIOBUTTON, self.m_radioBtnAsistenciaIncompletaOnRadioButton )
		self.btnCargaAsistenciaProf.Bind( wx.EVT_BUTTON, self.btnCargaAsistenciaProfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_choiceNomProfOnChoice( self, event ):
		event.Skip()
	
	def m_radioBtnAsistenciaCompletaOnRadioButton( self, event ):
		event.Skip()
	
	def m_radioBtnAsistenciaIncompletaOnRadioButton( self, event ):
		event.Skip()
	
	def btnCargaAsistenciaProfOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelEdicion
###########################################################################

class PanelEdicion ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 790,601 ), style = wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.Hide()
		
		sizerPanelEditProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTituloEdicion = wx.StaticText( self, wx.ID_ANY, u"Edición de Profesor", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTituloEdicion.Wrap( -1 )
		self.lblTituloEdicion.SetFont( wx.Font( 15, 74, 93, 92, False, "Tahoma" ) )
		
		sizerPanelEditProfesor.Add( self.lblTituloEdicion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 1 )
		
		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblListaProfEdicion = wx.StaticText( self, wx.ID_ANY, u"Seleccione un Profesor para Editar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblListaProfEdicion.Wrap( -1 )
		self.lblListaProfEdicion.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer42.Add( self.lblListaProfEdicion, 0, wx.ALL, 5 )
		
		m_choiceNombreProf_EdicionChoices = []
		self.m_choiceNombreProf_Edicion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceNombreProf_EdicionChoices, 0 )
		self.m_choiceNombreProf_Edicion.SetSelection( 0 )
		bSizer42.Add( self.m_choiceNombreProf_Edicion, 0, wx.ALL, 0 )
		
		
		sizerPanelEditProfesor.Add( bSizer42, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerPanelEditProfesor.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 2 )
		
		bSizer99 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel78 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer102 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNombreProf_Edicion = wx.StaticText( self.m_panel78, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombreProf_Edicion.Wrap( -1 )
		self.lblNombreProf_Edicion.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer102.Add( self.lblNombreProf_Edicion, 0, wx.ALL, 5 )
		
		self.txtNombreProf_Edicion = wx.TextCtrl( self.m_panel78, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer102.Add( self.txtNombreProf_Edicion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel78.SetSizer( bSizer102 )
		self.m_panel78.Layout()
		bSizer102.Fit( self.m_panel78 )
		bSizer99.Add( self.m_panel78, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel79 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer103 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblApellidoProf_Edicion = wx.StaticText( self.m_panel79, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblApellidoProf_Edicion.Wrap( -1 )
		self.lblApellidoProf_Edicion.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer103.Add( self.lblApellidoProf_Edicion, 0, wx.ALL, 5 )
		
		self.tctApellidoProf_Edicion = wx.TextCtrl( self.m_panel79, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer103.Add( self.tctApellidoProf_Edicion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel79.SetSizer( bSizer103 )
		self.m_panel79.Layout()
		bSizer103.Fit( self.m_panel79 )
		bSizer99.Add( self.m_panel79, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelEditProfesor.Add( bSizer99, 0, wx.EXPAND, 5 )
		
		bSizer100 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel80 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer104 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblCiProf_Edicion = wx.StaticText( self.m_panel80, wx.ID_ANY, u"Cédula de Identidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCiProf_Edicion.Wrap( -1 )
		self.lblCiProf_Edicion.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer104.Add( self.lblCiProf_Edicion, 0, wx.ALL, 5 )
		
		self.txtCiProf_Edicion=wx.lib.masked.TextCtrl( self.m_panel80, -1, '',size=(130, -1), mask = '########')
		bSizer104.Add( self.txtCiProf_Edicion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel80.SetSizer( bSizer104 )
		self.m_panel80.Layout()
		bSizer104.Fit( self.m_panel80 )
		bSizer100.Add( self.m_panel80, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer100.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel81 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFecNacProf = wx.StaticText( self.m_panel81, wx.ID_ANY, u"Fecha de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFecNacProf.Wrap( -1 )
		self.lblFecNacProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer105.Add( self.lblFecNacProf, 0, wx.ALL, 5 )
		
		self.datePickerFecNacProf = wx.DatePickerCtrl( self.m_panel81, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer105.Add( self.datePickerFecNacProf, 0, wx.ALL, 5 )
		
		
		self.m_panel81.SetSizer( bSizer105 )
		self.m_panel81.Layout()
		bSizer105.Fit( self.m_panel81 )
		bSizer100.Add( self.m_panel81, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelEditProfesor.Add( bSizer100, 0, wx.EXPAND, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel82 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer106 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTlfProf_Edicion = wx.StaticText( self.m_panel82, wx.ID_ANY, u"Teléfono de Contacto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTlfProf_Edicion.Wrap( -1 )
		self.lblTlfProf_Edicion.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer106.Add( self.lblTlfProf_Edicion, 0, wx.ALL, 5 )
		
		self.txtTlfProf_Edicion=wx.lib.masked.TextCtrl( self.m_panel82, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer106.Add( self.txtTlfProf_Edicion, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel82.SetSizer( bSizer106 )
		self.m_panel82.Layout()
		bSizer106.Fit( self.m_panel82 )
		bSizer101.Add( self.m_panel82, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer101.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel84 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer107 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFecIngresoProf = wx.StaticText( self.m_panel84, wx.ID_ANY, u"Fecha de Ingreso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFecIngresoProf.Wrap( -1 )
		self.lblFecIngresoProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer107.Add( self.lblFecIngresoProf, 0, wx.ALL, 5 )
		
		self.datePickerFecIngresoProf = wx.DatePickerCtrl( self.m_panel84, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer107.Add( self.datePickerFecIngresoProf, 0, wx.ALL, 5 )
		
		
		self.m_panel84.SetSizer( bSizer107 )
		self.m_panel84.Layout()
		bSizer107.Fit( self.m_panel84 )
		bSizer101.Add( self.m_panel84, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer101.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel85 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer108 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblEmailProf = wx.StaticText( self.m_panel85, wx.ID_ANY, u"E-Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblEmailProf.Wrap( -1 )
		self.lblEmailProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer108.Add( self.lblEmailProf, 0, wx.ALL, 5 )
		
		self.txtEmailProf = wx.TextCtrl( self.m_panel85, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer108.Add( self.txtEmailProf, 0, wx.ALL, 5 )
		
		
		self.m_panel85.SetSizer( bSizer108 )
		self.m_panel85.Layout()
		bSizer108.Fit( self.m_panel85 )
		bSizer101.Add( self.m_panel85, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelEditProfesor.Add( bSizer101, 0, wx.EXPAND, 5 )
		
		sizerCatgoriaProfesor_Edicion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblTipoProfesor_Edicion = wx.StaticText( self, wx.ID_ANY, u"Tipo de Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTipoProfesor_Edicion.Wrap( -1 )
		self.lblTipoProfesor_Edicion.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerCatgoriaProfesor_Edicion.Add( self.lblTipoProfesor_Edicion, 0, wx.ALL, 5 )
		
		choiceTipoProfesor_EdicionChoices = [ u"Profesor por Hora", u"Comisión de Servicio", u"Profesor Fijo" ]
		self.choiceTipoProfesor_Edicion = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTipoProfesor_EdicionChoices, 0 )
		self.choiceTipoProfesor_Edicion.SetSelection( 0 )
		sizerCatgoriaProfesor_Edicion.Add( self.choiceTipoProfesor_Edicion, 0, wx.ALL, 5 )
		
		
		sizerCatgoriaProfesor_Edicion.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		radioBox_ProfActivo_EdicionChoices = [ u"Si", u"No" ]
		self.radioBox_ProfActivo_Edicion = wx.RadioBox( self, wx.ID_ANY, u"Profesor Activo", wx.DefaultPosition, wx.DefaultSize, radioBox_ProfActivo_EdicionChoices, 2, wx.RA_SPECIFY_COLS )
		self.radioBox_ProfActivo_Edicion.SetSelection( 0 )
		sizerCatgoriaProfesor_Edicion.Add( self.radioBox_ProfActivo_Edicion, 0, wx.ALL, 0 )
		
		
		sizerPanelEditProfesor.Add( sizerCatgoriaProfesor_Edicion, 0, 0, 5 )
		
		self.PanelHorasDias_Edicion = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 790,-1 ), wx.TAB_TRAVERSAL )
		sizerHorasDias_Edicion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self.PanelHorasDias_Edicion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer98 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelHorasProfEdicion = wx.Panel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		bSizer98.Add( self.panelHorasProfEdicion, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		self.m_scrolledWindow2.SetSizer( bSizer98 )
		self.m_scrolledWindow2.Layout()
		bSizer98.Fit( self.m_scrolledWindow2 )
		sizerHorasDias_Edicion.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.PanelHorasDias_Edicion.SetSizer( sizerHorasDias_Edicion )
		self.PanelHorasDias_Edicion.Layout()
		sizerPanelEditProfesor.Add( self.PanelHorasDias_Edicion, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnEditProf = wx.Button( self, wx.ID_ANY, u"Editar", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.btnEditProf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		sizerPanelEditProfesor.Add( self.btnEditProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerPanelEditProfesor )
		self.Layout()
		
		# Connect Events
		self.m_choiceNombreProf_Edicion.Bind( wx.EVT_CHOICE, self.m_choiceNombreProf_EdicionOnChoice )
		self.btnEditProf.Bind( wx.EVT_BUTTON, self.btnEditProfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_choiceNombreProf_EdicionOnChoice( self, event ):
		event.Skip()
	
	def btnEditProfOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelCarga
###########################################################################

class PanelCarga ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 790,700 ), style = wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		
		self.Hide()
		
		sizerPanelCargaProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTituloCarga = wx.StaticText( self, wx.ID_ANY, u"Carga de Profesor Nuevo", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTituloCarga.Wrap( -1 )
		self.lblTituloCarga.SetFont( wx.Font( 15, 74, 93, 92, False, "Tahoma" ) )
		
		sizerPanelCargaProfesor.Add( self.lblTituloCarga, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer83 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel62 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblNombreProfCarga = wx.StaticText( self.m_panel62, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombreProfCarga.Wrap( -1 )
		self.lblNombreProfCarga.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer76.Add( self.lblNombreProfCarga, 0, wx.ALL, 5 )
		
		self.txtNombreProf_Carga = wx.TextCtrl( self.m_panel62, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer76.Add( self.txtNombreProf_Carga, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel62.SetSizer( bSizer76 )
		self.m_panel62.Layout()
		bSizer76.Fit( self.m_panel62 )
		bSizer83.Add( self.m_panel62, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel63 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer77 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblApellidoProf_Carga = wx.StaticText( self.m_panel63, wx.ID_ANY, u"Apellido", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblApellidoProf_Carga.Wrap( -1 )
		self.lblApellidoProf_Carga.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer77.Add( self.lblApellidoProf_Carga, 0, wx.ALL, 5 )
		
		self.tctApellidoProf_Carga = wx.TextCtrl( self.m_panel63, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		bSizer77.Add( self.tctApellidoProf_Carga, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel63.SetSizer( bSizer77 )
		self.m_panel63.Layout()
		bSizer77.Fit( self.m_panel63 )
		bSizer83.Add( self.m_panel63, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelCargaProfesor.Add( bSizer83, 0, wx.EXPAND, 5 )
		
		bSizer84 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel64 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblCiProf_Carga = wx.StaticText( self.m_panel64, wx.ID_ANY, u"Cédula de Identidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCiProf_Carga.Wrap( -1 )
		self.lblCiProf_Carga.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer78.Add( self.lblCiProf_Carga, 0, wx.ALL, 5 )
		
		self.txtCiProf_Carga=wx.lib.masked.TextCtrl( self.m_panel64, -1, '', size=(130, -1), mask = '########')
		bSizer78.Add( self.txtCiProf_Carga, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel64.SetSizer( bSizer78 )
		self.m_panel64.Layout()
		bSizer78.Fit( self.m_panel64 )
		bSizer84.Add( self.m_panel64, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer84.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel65 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer79 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFecNacProf = wx.StaticText( self.m_panel65, wx.ID_ANY, u"Fecha de Nacimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFecNacProf.Wrap( -1 )
		self.lblFecNacProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer79.Add( self.lblFecNacProf, 0, wx.ALL, 5 )
		
		self.datePickerFecNacProf = wx.DatePickerCtrl( self.m_panel65, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer79.Add( self.datePickerFecNacProf, 0, wx.ALL, 5 )
		
		
		self.m_panel65.SetSizer( bSizer79 )
		self.m_panel65.Layout()
		bSizer79.Fit( self.m_panel65 )
		bSizer84.Add( self.m_panel65, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelCargaProfesor.Add( bSizer84, 0, wx.EXPAND, 5 )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel66 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer80 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTlfProf_Carga = wx.StaticText( self.m_panel66, wx.ID_ANY, u"Teléfono de Contacto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTlfProf_Carga.Wrap( -1 )
		self.lblTlfProf_Carga.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer80.Add( self.lblTlfProf_Carga, 0, wx.ALL, 5 )
		
		self.txtTlfProf_Carga=wx.lib.masked.TextCtrl( self.m_panel66, -1, '', size=(130, -1), mask = '(####) ###-####')
		bSizer80.Add( self.txtTlfProf_Carga, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel66.SetSizer( bSizer80 )
		self.m_panel66.Layout()
		bSizer80.Fit( self.m_panel66 )
		bSizer85.Add( self.m_panel66, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer85.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel67 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblFecIngresoProf = wx.StaticText( self.m_panel67, wx.ID_ANY, u"Fecha de Ingreso", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFecIngresoProf.Wrap( -1 )
		self.lblFecIngresoProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer81.Add( self.lblFecIngresoProf, 0, wx.ALL, 5 )
		
		self.datePickerFecIngresoProf = wx.DatePickerCtrl( self.m_panel67, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer81.Add( self.datePickerFecIngresoProf, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel67.SetSizer( bSizer81 )
		self.m_panel67.Layout()
		bSizer81.Fit( self.m_panel67 )
		bSizer85.Add( self.m_panel67, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer85.AddSpacer( ( 76, 0), 0, wx.EXPAND, 5 )
		
		self.m_panel68 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer82 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblEmailProf = wx.StaticText( self.m_panel68, wx.ID_ANY, u"E-Mail", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblEmailProf.Wrap( -1 )
		self.lblEmailProf.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer82.Add( self.lblEmailProf, 0, wx.ALL, 5 )
		
		self.txtEmailProf = wx.TextCtrl( self.m_panel68, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		bSizer82.Add( self.txtEmailProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel68.SetSizer( bSizer82 )
		self.m_panel68.Layout()
		bSizer82.Fit( self.m_panel68 )
		bSizer85.Add( self.m_panel68, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerPanelCargaProfesor.Add( bSizer85, 0, wx.EXPAND, 5 )
		
		sizerCatgoriaProfesor_Carga = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblTipoProfesor_Carga = wx.StaticText( self, wx.ID_ANY, u"Tipo de Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTipoProfesor_Carga.Wrap( -1 )
		self.lblTipoProfesor_Carga.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerCatgoriaProfesor_Carga.Add( self.lblTipoProfesor_Carga, 0, wx.ALL, 5 )
		
		choiceTipoProfesor_CargaChoices = [ u"Profesor por Hora", u"Comisión de Servicio", u"Profesor Fijo" ]
		self.choiceTipoProfesor_Carga = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceTipoProfesor_CargaChoices, 0 )
		self.choiceTipoProfesor_Carga.SetSelection( 0 )
		sizerCatgoriaProfesor_Carga.Add( self.choiceTipoProfesor_Carga, 0, wx.ALL, 5 )
		
		
		sizerCatgoriaProfesor_Carga.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
		
		radioBox_ProfActivoChoices = [ u"Si", u"No" ]
		self.radioBox_ProfActivo = wx.RadioBox( self, wx.ID_ANY, u"Profesor Activo", wx.DefaultPosition, wx.DefaultSize, radioBox_ProfActivoChoices, 2, wx.RA_SPECIFY_COLS )
		self.radioBox_ProfActivo.SetSelection( 0 )
		sizerCatgoriaProfesor_Carga.Add( self.radioBox_ProfActivo, 0, wx.ALL, 0 )
		
		
		sizerPanelCargaProfesor.Add( sizerCatgoriaProfesor_Carga, 0, 0, 5 )
		
		self.PanelHorasDias_Carga = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 790,600 ), wx.TAB_TRAVERSAL )
		sizerHorasDias_Carga = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow6 = wx.ScrolledWindow( self.PanelHorasDias_Carga, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		bSizer167 = wx.BoxSizer( wx.VERTICAL )
		
		self.panelHorasProfCarga = wx.Panel( self.m_scrolledWindow6, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		bSizer167.Add( self.panelHorasProfCarga, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_scrolledWindow6.SetSizer( bSizer167 )
		self.m_scrolledWindow6.Layout()
		bSizer167.Fit( self.m_scrolledWindow6 )
		sizerHorasDias_Carga.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.PanelHorasDias_Carga.SetSizer( sizerHorasDias_Carga )
		self.PanelHorasDias_Carga.Layout()
		sizerPanelCargaProfesor.Add( self.PanelHorasDias_Carga, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnCargaProf = wx.Button( self, wx.ID_ANY, u"Cargar", wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		self.btnCargaProf.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		sizerPanelCargaProfesor.Add( self.btnCargaProf, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerPanelCargaProfesor )
		self.Layout()
		
		# Connect Events
		self.btnCargaProf.Bind( wx.EVT_BUTTON, self.btnCargaProfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnCargaProfOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class PanelBienvenida
###########################################################################

class PanelBienvenida ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.Point( 240,10 ), size = wx.Size( 790,474 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sizerPanelBienvenida = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel38 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel41 = wx.Panel( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44.Add( self.m_panel41, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline12 = wx.StaticLine( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline10 = wx.StaticLine( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline10, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel51 = wx.Panel( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel51, wx.ID_ANY, wx.Bitmap( u"bitmaps/cabecera.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer56.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel51.SetSizer( bSizer56 )
		self.m_panel51.Layout()
		bSizer56.Fit( self.m_panel51 )
		bSizer44.Add( self.m_panel51, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer44.Add( self.m_staticline11, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel40 = wx.Panel( self.m_panel38, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer44.Add( self.m_panel40, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel38.SetSizer( bSizer44 )
		self.m_panel38.Layout()
		bSizer44.Fit( self.m_panel38 )
		sizerPanelBienvenida.Add( self.m_panel38, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.SetSizer( sizerPanelBienvenida )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class FrameReporteProfesor
###########################################################################

class FrameReporteProfesor ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reportes por Profesor", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerReporteProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1ReporteProfesor = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1ReporteProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFechasReporteProfesor = wx.Panel( self.panel1ReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFechasReporteProfesor = wx.BoxSizer( wx.HORIZONTAL )
		
		self.panelFecha1ReporteProfesor = wx.Panel( self.panelFechasReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha1ReporteProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaInicio = wx.DatePickerCtrl( self.panelFecha1ReporteProfesor, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha1ReporteProfesor.Add( self.datePickerFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaInicio = wx.StaticText( self.panelFecha1ReporteProfesor, wx.ID_ANY, u"Fecha de Inicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaInicio.Wrap( -1 )
		self.lblFechaInicio.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha1ReporteProfesor.Add( self.lblFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha1ReporteProfesor.SetSizer( sizerPanelFecha1ReporteProfesor )
		self.panelFecha1ReporteProfesor.Layout()
		sizerPanelFecha1ReporteProfesor.Fit( self.panelFecha1ReporteProfesor )
		sizerPanelFechasReporteProfesor.Add( self.panelFecha1ReporteProfesor, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panelFecha2ReporteProfesor = wx.Panel( self.panelFechasReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha2ReporteProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaFin = wx.DatePickerCtrl( self.panelFecha2ReporteProfesor, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha2ReporteProfesor.Add( self.datePickerFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaFin = wx.StaticText( self.panelFecha2ReporteProfesor, wx.ID_ANY, u"Fecha de Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaFin.Wrap( -1 )
		self.lblFechaFin.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha2ReporteProfesor.Add( self.lblFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha2ReporteProfesor.SetSizer( sizerPanelFecha2ReporteProfesor )
		self.panelFecha2ReporteProfesor.Layout()
		sizerPanelFecha2ReporteProfesor.Fit( self.panelFecha2ReporteProfesor )
		sizerPanelFechasReporteProfesor.Add( self.panelFecha2ReporteProfesor, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelFechasReporteProfesor.SetSizer( sizerPanelFechasReporteProfesor )
		self.panelFechasReporteProfesor.Layout()
		sizerPanelFechasReporteProfesor.Fit( self.panelFechasReporteProfesor )
		sizerPanel1ReporteProfesor.Add( self.panelFechasReporteProfesor, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelEscojerProfesorCatedra = wx.Panel( self.panel1ReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelEscojerProfesorCatedra = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblProfesor = wx.StaticText( self.panelEscojerProfesorCatedra, wx.ID_ANY, u"Escoja un Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblProfesor.Wrap( -1 )
		self.lblProfesor.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblProfesor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choiceProfesorChoices = []
		self.m_choiceProfesor = wx.Choice( self.panelEscojerProfesorCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceProfesorChoices, 0 )
		self.m_choiceProfesor.SetSelection( 0 )
		bSizer41.Add( self.m_choiceProfesor, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		sizerPenelEscojerProfesorCatedra.Add( bSizer41, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelEscojerProfesorCatedra.SetSizer( sizerPenelEscojerProfesorCatedra )
		self.panelEscojerProfesorCatedra.Layout()
		sizerPenelEscojerProfesorCatedra.Fit( self.panelEscojerProfesorCatedra )
		sizerPanel1ReporteProfesor.Add( self.panelEscojerProfesorCatedra, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.panelLeyendaEscojerProfesorCatedra = wx.Panel( self.panel1ReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerPanelLeyendaEscojerProfesorCatedra = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.panelLeyendaEscojerProfesorCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorCatedra.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblLeyendaEscojerCatedra = wx.StaticText( self.panelLeyendaEscojerProfesorCatedra, wx.ID_ANY, u"Escoja una Cátedra para generar un reporte de Asistencia docente de la misma", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaEscojerCatedra.Wrap( -1 )
		SizerPanelLeyendaEscojerProfesorCatedra.Add( self.lblLeyendaEscojerCatedra, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.panelLeyendaEscojerProfesorCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorCatedra.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelLeyendaEscojerProfesorCatedra.SetSizer( SizerPanelLeyendaEscojerProfesorCatedra )
		self.panelLeyendaEscojerProfesorCatedra.Layout()
		SizerPanelLeyendaEscojerProfesorCatedra.Fit( self.panelLeyendaEscojerProfesorCatedra )
		sizerPanel1ReporteProfesor.Add( self.panelLeyendaEscojerProfesorCatedra, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelBotonesEscojerProfesorCatedra = wx.Panel( self.panel1ReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesEscojerProfesorCatedra = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCrearReporteProfesorCatedras = wx.Button( self.panelBotonesEscojerProfesorCatedra, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorCatedra.Add( self.btnCrearReporteProfesorCatedras, 0, wx.ALL, 5 )
		
		self.btnCancelarReporteProfesorCatedras = wx.Button( self.panelBotonesEscojerProfesorCatedra, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorCatedra.Add( self.btnCancelarReporteProfesorCatedras, 0, wx.ALL, 5 )
		
		
		self.panelBotonesEscojerProfesorCatedra.SetSizer( sizerPanelBotonesEscojerProfesorCatedra )
		self.panelBotonesEscojerProfesorCatedra.Layout()
		sizerPanelBotonesEscojerProfesorCatedra.Fit( self.panelBotonesEscojerProfesorCatedra )
		sizerPanel1ReporteProfesor.Add( self.panelBotonesEscojerProfesorCatedra, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.paneReporteProf = wx.Panel( self.panel1ReporteProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanel1ReporteProfesor.Add( self.paneReporteProf, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel1ReporteProfesor.SetSizer( sizerPanel1ReporteProfesor )
		self.panel1ReporteProfesor.Layout()
		sizerPanel1ReporteProfesor.Fit( self.panel1ReporteProfesor )
		sizerReporteProfesor.Add( self.panel1ReporteProfesor, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerReporteProfesor )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameReporteCatedrasOnClose )
		self.m_choiceProfesor.Bind( wx.EVT_CHOICE, self.m_choiceProfesorOnChoice )
		self.btnCrearReporteProfesorCatedras.Bind( wx.EVT_BUTTON, self.btnCrearReporteProfesorCatedrasOnButtonClick )
		self.btnCancelarReporteProfesorCatedras.Bind( wx.EVT_BUTTON, self.btnCancelarReporteCatedrasOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameReporteCatedrasOnClose( self, event ):
		event.Skip()
	
	def m_choiceProfesorOnChoice( self, event ):
		event.Skip()
	
	def btnCrearReporteProfesorCatedrasOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarReporteCatedrasOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameFichaProfesor
###########################################################################

class FrameFichaProfesor ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ficha de Profesor", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerFichaProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFichaProfesor = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFichaProfesor = wx.BoxSizer( wx.VERTICAL )
		
		self.panelEscojerProfesorFicha = wx.Panel( self.panelFichaProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelEscojerProfesorFicha = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblProfesor = wx.StaticText( self.panelEscojerProfesorFicha, wx.ID_ANY, u"Escoja un Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblProfesor.Wrap( -1 )
		self.lblProfesor.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblProfesor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choiceFichaProfesorChoices = []
		self.m_choiceFichaProfesor = wx.Choice( self.panelEscojerProfesorFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceFichaProfesorChoices, 0 )
		self.m_choiceFichaProfesor.SetSelection( 0 )
		bSizer41.Add( self.m_choiceFichaProfesor, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		sizerPenelEscojerProfesorFicha.Add( bSizer41, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelEscojerProfesorFicha.SetSizer( sizerPenelEscojerProfesorFicha )
		self.panelEscojerProfesorFicha.Layout()
		sizerPenelEscojerProfesorFicha.Fit( self.panelEscojerProfesorFicha )
		sizerPanelFichaProfesor.Add( self.panelEscojerProfesorFicha, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.panelLeyendaEscojerProfesorFicha = wx.Panel( self.panelFichaProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerPanelLeyendaEscojerProfesorFicha = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.panelLeyendaEscojerProfesorFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorFicha.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblLeyendaEscojerFicha = wx.StaticText( self.panelLeyendaEscojerProfesorFicha, wx.ID_ANY, u"Escoja un Profesor para generar su Ficha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaEscojerFicha.Wrap( -1 )
		SizerPanelLeyendaEscojerProfesorFicha.Add( self.lblLeyendaEscojerFicha, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.panelLeyendaEscojerProfesorFicha, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorFicha.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelLeyendaEscojerProfesorFicha.SetSizer( SizerPanelLeyendaEscojerProfesorFicha )
		self.panelLeyendaEscojerProfesorFicha.Layout()
		SizerPanelLeyendaEscojerProfesorFicha.Fit( self.panelLeyendaEscojerProfesorFicha )
		sizerPanelFichaProfesor.Add( self.panelLeyendaEscojerProfesorFicha, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelBotonesEscojerProfesorFicha = wx.Panel( self.panelFichaProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesEscojerProfesorFicha = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCrearReporteProfesorFicha = wx.Button( self.panelBotonesEscojerProfesorFicha, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorFicha.Add( self.btnCrearReporteProfesorFicha, 0, wx.ALL, 5 )
		
		self.btnCancelarReporteProfesorFicha = wx.Button( self.panelBotonesEscojerProfesorFicha, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorFicha.Add( self.btnCancelarReporteProfesorFicha, 0, wx.ALL, 5 )
		
		
		self.panelBotonesEscojerProfesorFicha.SetSizer( sizerPanelBotonesEscojerProfesorFicha )
		self.panelBotonesEscojerProfesorFicha.Layout()
		sizerPanelBotonesEscojerProfesorFicha.Fit( self.panelBotonesEscojerProfesorFicha )
		sizerPanelFichaProfesor.Add( self.panelBotonesEscojerProfesorFicha, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelReportFichaProf = wx.Panel( self.panelFichaProfesor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanelFichaProfesor.Add( self.panelReportFichaProf, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelFichaProfesor.SetSizer( sizerPanelFichaProfesor )
		self.panelFichaProfesor.Layout()
		sizerPanelFichaProfesor.Fit( self.panelFichaProfesor )
		sizerFichaProfesor.Add( self.panelFichaProfesor, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerFichaProfesor )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameFichaProfesorOnClose )
		self.btnCrearReporteProfesorFicha.Bind( wx.EVT_BUTTON, self.btnCrearReporteProfesorFichaOnButtonClick )
		self.btnCancelarReporteProfesorFicha.Bind( wx.EVT_BUTTON, self.btnCancelarReporteProfesorFichaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameFichaProfesorOnClose( self, event ):
		event.Skip()
	
	def btnCrearReporteProfesorFichaOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarReporteProfesorFichaOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameFichaGeneral
###########################################################################

class FrameFichaGeneral ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ficha General de Profesores", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerFichaGeneral = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFichaGeneral = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFichaGeneral = wx.BoxSizer( wx.VERTICAL )
		
		self.panelReportFichaGen = wx.Panel( self.panelFichaGeneral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanelFichaGeneral.Add( self.panelReportFichaGen, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panelBotonesFichaGen = wx.Panel( self.panelFichaGeneral, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFichaGen = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCerrarFichaGen = wx.Button( self.panelBotonesFichaGen, wx.ID_ANY, u"Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelFichaGen.Add( self.btnCerrarFichaGen, 0, wx.ALL, 5 )
		
		
		self.panelBotonesFichaGen.SetSizer( sizerPanelFichaGen )
		self.panelBotonesFichaGen.Layout()
		sizerPanelFichaGen.Fit( self.panelBotonesFichaGen )
		sizerPanelFichaGeneral.Add( self.panelBotonesFichaGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFichaGeneral.SetSizer( sizerPanelFichaGeneral )
		self.panelFichaGeneral.Layout()
		sizerPanelFichaGeneral.Fit( self.panelFichaGeneral )
		sizerFichaGeneral.Add( self.panelFichaGeneral, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerFichaGeneral )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameFichaGeneralOnClose )
		self.btnCerrarFichaGen.Bind( wx.EVT_BUTTON, self.btnCerrarFichaGenOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameFichaGeneralOnClose( self, event ):
		event.Skip()
	
	def btnCerrarFichaGenOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameReporteCatedras
###########################################################################

class FrameReporteCatedras ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reportes por Cátedra", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerPrincipalReporteCatedras = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1ReporteCatedras = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1ReporteCatedras = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFechasReporteCatedra = wx.Panel( self.panel1ReporteCatedras, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFechasReporteReporteCatedra = wx.BoxSizer( wx.HORIZONTAL )
		
		self.panelFecha1ReporteReporteCatedra = wx.Panel( self.panelFechasReporteCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha1ReporteCatedra = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaInicio = wx.DatePickerCtrl( self.panelFecha1ReporteReporteCatedra, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha1ReporteCatedra.Add( self.datePickerFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaInicio = wx.StaticText( self.panelFecha1ReporteReporteCatedra, wx.ID_ANY, u"Fecha de Inicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaInicio.Wrap( -1 )
		self.lblFechaInicio.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha1ReporteCatedra.Add( self.lblFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha1ReporteReporteCatedra.SetSizer( sizerPanelFecha1ReporteCatedra )
		self.panelFecha1ReporteReporteCatedra.Layout()
		sizerPanelFecha1ReporteCatedra.Fit( self.panelFecha1ReporteReporteCatedra )
		sizerPanelFechasReporteReporteCatedra.Add( self.panelFecha1ReporteReporteCatedra, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panelFecha2ReporteCatedra = wx.Panel( self.panelFechasReporteCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha2ReporteCatedra = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaFin = wx.DatePickerCtrl( self.panelFecha2ReporteCatedra, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha2ReporteCatedra.Add( self.datePickerFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaFin = wx.StaticText( self.panelFecha2ReporteCatedra, wx.ID_ANY, u"Fecha de Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaFin.Wrap( -1 )
		self.lblFechaFin.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha2ReporteCatedra.Add( self.lblFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha2ReporteCatedra.SetSizer( sizerPanelFecha2ReporteCatedra )
		self.panelFecha2ReporteCatedra.Layout()
		sizerPanelFecha2ReporteCatedra.Fit( self.panelFecha2ReporteCatedra )
		sizerPanelFechasReporteReporteCatedra.Add( self.panelFecha2ReporteCatedra, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelFechasReporteCatedra.SetSizer( sizerPanelFechasReporteReporteCatedra )
		self.panelFechasReporteCatedra.Layout()
		sizerPanelFechasReporteReporteCatedra.Fit( self.panelFechasReporteCatedra )
		sizerPanel1ReporteCatedras.Add( self.panelFechasReporteCatedra, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panelEscojerCatedra = wx.Panel( self.panel1ReporteCatedras, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelEscojerCatedra = wx.BoxSizer( wx.VERTICAL )
		
		self.lblCatedra = wx.StaticText( self.panelEscojerCatedra, wx.ID_ANY, u"Escoja una Cátedra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCatedra.Wrap( -1 )
		self.lblCatedra.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPenelEscojerCatedra.Add( self.lblCatedra, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choiceCatedraReporteChoices = []
		self.m_choiceCatedraReporte = wx.Choice( self.panelEscojerCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceCatedraReporteChoices, 0 )
		self.m_choiceCatedraReporte.SetSelection( 0 )
		sizerPenelEscojerCatedra.Add( self.m_choiceCatedraReporte, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelEscojerCatedra.SetSizer( sizerPenelEscojerCatedra )
		self.panelEscojerCatedra.Layout()
		sizerPenelEscojerCatedra.Fit( self.panelEscojerCatedra )
		sizerPanel1ReporteCatedras.Add( self.panelEscojerCatedra, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.panelLeyendaEscojerCatedra = wx.Panel( self.panel1ReporteCatedras, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelLeyendaEscojerCatedra = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.panelLeyendaEscojerCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerPanelLeyendaEscojerCatedra.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblLeyendaEscojerCatedra = wx.StaticText( self.panelLeyendaEscojerCatedra, wx.ID_ANY, u"Escoja una Catedra para generar un reporte de Asistencia por Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaEscojerCatedra.Wrap( -1 )
		sizerPanelLeyendaEscojerCatedra.Add( self.lblLeyendaEscojerCatedra, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.panelLeyendaEscojerCatedra, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerPanelLeyendaEscojerCatedra.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelLeyendaEscojerCatedra.SetSizer( sizerPanelLeyendaEscojerCatedra )
		self.panelLeyendaEscojerCatedra.Layout()
		sizerPanelLeyendaEscojerCatedra.Fit( self.panelLeyendaEscojerCatedra )
		sizerPanel1ReporteCatedras.Add( self.panelLeyendaEscojerCatedra, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelBotonesEscojerCatedra = wx.Panel( self.panel1ReporteCatedras, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesEscojerCatedra = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCrearReporteCat = wx.Button( self.panelBotonesEscojerCatedra, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerCatedra.Add( self.btnCrearReporteCat, 0, wx.ALL, 5 )
		
		self.btnCancelarReporteCat = wx.Button( self.panelBotonesEscojerCatedra, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerCatedra.Add( self.btnCancelarReporteCat, 0, wx.ALL, 5 )
		
		
		self.panelBotonesEscojerCatedra.SetSizer( sizerPanelBotonesEscojerCatedra )
		self.panelBotonesEscojerCatedra.Layout()
		sizerPanelBotonesEscojerCatedra.Fit( self.panelBotonesEscojerCatedra )
		sizerPanel1ReporteCatedras.Add( self.panelBotonesEscojerCatedra, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelReporteCat = wx.Panel( self.panel1ReporteCatedras, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanel1ReporteCatedras.Add( self.panelReporteCat, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel1ReporteCatedras.SetSizer( sizerPanel1ReporteCatedras )
		self.panel1ReporteCatedras.Layout()
		sizerPanel1ReporteCatedras.Fit( self.panel1ReporteCatedras )
		sizerPrincipalReporteCatedras.Add( self.panel1ReporteCatedras, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPrincipalReporteCatedras )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameReporteDocenteOnClose )
		self.btnCrearReporteCat.Bind( wx.EVT_BUTTON, self.btnCrearReporteCatOnButtonClick )
		self.btnCancelarReporteCat.Bind( wx.EVT_BUTTON, self.btnCancelarReporteProfOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameReporteDocenteOnClose( self, event ):
		event.Skip()
	
	def btnCrearReporteCatOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarReporteProfOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameFormaUnica
###########################################################################

class FrameFormaUnica ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reporte Forma Única", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerPrincipalFrameFormaUnica = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1FormaUnica = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1FormaUnica = wx.BoxSizer( wx.VERTICAL )
		
		self.panelFechasFormaUnica = wx.Panel( self.panel1FormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFechasFormaUnica = wx.BoxSizer( wx.HORIZONTAL )
		
		self.panelFecha1FormaUnica = wx.Panel( self.panelFechasFormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha1FormaUnica = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaInicio = wx.DatePickerCtrl( self.panelFecha1FormaUnica, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha1FormaUnica.Add( self.datePickerFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaInicio = wx.StaticText( self.panelFecha1FormaUnica, wx.ID_ANY, u"Fecha de Inicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaInicio.Wrap( -1 )
		self.lblFechaInicio.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha1FormaUnica.Add( self.lblFechaInicio, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha1FormaUnica.SetSizer( sizerPanelFecha1FormaUnica )
		self.panelFecha1FormaUnica.Layout()
		sizerPanelFecha1FormaUnica.Fit( self.panelFecha1FormaUnica )
		sizerPanelFechasFormaUnica.Add( self.panelFecha1FormaUnica, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.panelFecha2FormaUnica = wx.Panel( self.panelFechasFormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelFecha2FormaUnica = wx.BoxSizer( wx.VERTICAL )
		
		self.datePickerFechaFin = wx.DatePickerCtrl( self.panelFecha2FormaUnica, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		sizerPanelFecha2FormaUnica.Add( self.datePickerFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblFechaFin = wx.StaticText( self.panelFecha2FormaUnica, wx.ID_ANY, u"Fecha de Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblFechaFin.Wrap( -1 )
		self.lblFechaFin.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanelFecha2FormaUnica.Add( self.lblFechaFin, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelFecha2FormaUnica.SetSizer( sizerPanelFecha2FormaUnica )
		self.panelFecha2FormaUnica.Layout()
		sizerPanelFecha2FormaUnica.Fit( self.panelFecha2FormaUnica )
		sizerPanelFechasFormaUnica.Add( self.panelFecha2FormaUnica, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelFechasFormaUnica.SetSizer( sizerPanelFechasFormaUnica )
		self.panelFechasFormaUnica.Layout()
		sizerPanelFechasFormaUnica.Fit( self.panelFechasFormaUnica )
		sizerPanel1FormaUnica.Add( self.panelFechasFormaUnica, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel92 = wx.Panel( self.panel1FormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer110 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel93 = wx.Panel( self.m_panel92, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_checkBoxProyeccionFormaUnica = wx.CheckBox( self.m_panel93, wx.ID_ANY, u"Incluir Proyección", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_checkBoxProyeccionFormaUnica, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer111.AddSpacer( ( 60, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText59 = wx.StaticText( self.m_panel93, wx.ID_ANY, u"Días a Proyectar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		self.m_staticText59.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer111.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_spinCtrlMeses_Proyectados = wx.SpinCtrl( self.m_panel93, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 365, 1 )
		self.m_spinCtrlMeses_Proyectados.Enable( False )
		
		bSizer111.Add( self.m_spinCtrlMeses_Proyectados, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel93.SetSizer( bSizer111 )
		self.m_panel93.Layout()
		bSizer111.Fit( self.m_panel93 )
		bSizer110.Add( self.m_panel93, 0, wx.ALL, 5 )
		
		
		self.m_panel92.SetSizer( bSizer110 )
		self.m_panel92.Layout()
		bSizer110.Fit( self.m_panel92 )
		sizerPanel1FormaUnica.Add( self.m_panel92, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelLeyendaFormaUnica = wx.Panel( self.panel1FormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelLeyendaformaUnica = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline6 = wx.StaticLine( self.panelLeyendaFormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerPenelLeyendaformaUnica.Add( self.m_staticline6, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lblLeyendaFormaUnica = wx.StaticText( self.panelLeyendaFormaUnica, wx.ID_ANY, u"Escoja un Intervalo de Fechas para Generar la forma Única", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaFormaUnica.Wrap( -1 )
		sizerPenelLeyendaformaUnica.Add( self.lblLeyendaFormaUnica, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline7 = wx.StaticLine( self.panelLeyendaFormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sizerPenelLeyendaformaUnica.Add( self.m_staticline7, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panelLeyendaFormaUnica.SetSizer( sizerPenelLeyendaformaUnica )
		self.panelLeyendaFormaUnica.Layout()
		sizerPenelLeyendaformaUnica.Fit( self.panelLeyendaFormaUnica )
		sizerPanel1FormaUnica.Add( self.panelLeyendaFormaUnica, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.panelBotonesFormaUnica = wx.Panel( self.panel1FormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesFormaUnica = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCrearFormaUnica = wx.Button( self.panelBotonesFormaUnica, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesFormaUnica.Add( self.btnCrearFormaUnica, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelarFormaUnica = wx.Button( self.panelBotonesFormaUnica, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesFormaUnica.Add( self.btnCancelarFormaUnica, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelBotonesFormaUnica.SetSizer( sizerPanelBotonesFormaUnica )
		self.panelBotonesFormaUnica.Layout()
		sizerPanelBotonesFormaUnica.Fit( self.panelBotonesFormaUnica )
		sizerPanel1FormaUnica.Add( self.panelBotonesFormaUnica, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelFormaUnica = wx.Panel( self.panel1FormaUnica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanel1FormaUnica.Add( self.panelFormaUnica, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel1FormaUnica.SetSizer( sizerPanel1FormaUnica )
		self.panel1FormaUnica.Layout()
		sizerPanel1FormaUnica.Fit( self.panel1FormaUnica )
		sizerPrincipalFrameFormaUnica.Add( self.panel1FormaUnica, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sizerPrincipalFrameFormaUnica )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameFormaUnicaOnClose )
		self.m_checkBoxProyeccionFormaUnica.Bind( wx.EVT_CHECKBOX, self.m_checkBoxProyeccionFormaUnicaOnCheckBox )
		self.btnCrearFormaUnica.Bind( wx.EVT_BUTTON, self.btnCrearFormaUnicaOnButtonClick )
		self.btnCancelarFormaUnica.Bind( wx.EVT_BUTTON, self.btnCancelarFormaUnicaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameFormaUnicaOnClose( self, event ):
		event.Skip()
	
	def m_checkBoxProyeccionFormaUnicaOnCheckBox( self, event ):
		event.Skip()
	
	def btnCrearFormaUnicaOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarFormaUnicaOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class WizardConfigInicial
###########################################################################

class WizardConfigInicial ( wx.wizard.Wizard ):
	
	def __init__( self, parent ):
		wx.wizard.Wizard.__init__ ( self, parent, id = wx.ID_ANY, title = u"Configuración Inicial del Sistema de Control Docente", bitmap = wx.Bitmap( u"bitmaps/logoWizard.png", wx.BITMAP_TYPE_ANY ), pos = wx.DefaultPosition, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.m_pages = []
		
		self.pagina1Wizard = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.pagina1Wizard )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel40 = wx.Panel( self.pagina1Wizard, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTituloPag1Wizard = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Datos del Núcleo o Módulo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTituloPag1Wizard.Wrap( -1 )
		self.lblTituloPag1Wizard.SetFont( wx.Font( 14, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer39.Add( self.lblTituloPag1Wizard, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer39.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 20 )
		
		self.lblNombreNucleo = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Nombre del Núcleo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombreNucleo.Wrap( -1 )
		self.lblNombreNucleo.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer39.Add( self.lblNombreNucleo, 0, wx.ALL, 5 )
		
		self.txtNucleo = wx.TextCtrl( self.m_panel40, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer39.Add( self.txtNucleo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lblEntFedNucleo = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Entidad Federal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblEntFedNucleo.Wrap( -1 )
		self.lblEntFedNucleo.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer39.Add( self.lblEntFedNucleo, 0, wx.ALL, 5 )
		
		choiceEntFedChoices = [ u"Selecione una Entidad Federal", u"Distrito Capital", u"Amazonas", u"Anzoátegui ", u"Apure", u"Aragua", u"Barinas", u"Bolívar", u"Carabobo", u"Cojedes", u"Delta Amacuro", u"Falcón", u"Guárico", u"Lara", u"Mérida", u"Mirand", u"Monagas", u"Nueva Esparta", u"Portuguesa", u"Sucre", u"Táchira", u"Trujillo", u"Vargas", u"Yaracuy", u"Zulia" ]
		self.choiceEntFed = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceEntFedChoices, 0 )
		self.choiceEntFed.SetSelection( 0 )
		bSizer39.Add( self.choiceEntFed, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lblMunicipioNucleo = wx.StaticText( self.m_panel40, wx.ID_ANY, u"Municipio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblMunicipioNucleo.Wrap( -1 )
		self.lblMunicipioNucleo.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer39.Add( self.lblMunicipioNucleo, 0, wx.ALL, 5 )
		
		choiceMunicipioChoices = []
		self.choiceMunicipio = wx.Choice( self.m_panel40, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceMunicipioChoices, 0 )
		self.choiceMunicipio.SetSelection( 0 )
		bSizer39.Add( self.choiceMunicipio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel40.SetSizer( bSizer39 )
		self.m_panel40.Layout()
		bSizer39.Fit( self.m_panel40 )
		bSizer38.Add( self.m_panel40, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pagina1Wizard.SetSizer( bSizer38 )
		self.pagina1Wizard.Layout()
		self.pagina2Wizard = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.pagina2Wizard )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel41 = wx.Panel( self.pagina2Wizard, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTituloPag1Wizard1 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Datos del Administrador", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTituloPag1Wizard1.Wrap( -1 )
		self.lblTituloPag1Wizard1.SetFont( wx.Font( 14, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblTituloPag1Wizard1, 0, wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.m_panel41, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer41.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 20 )
		
		self.lblUsuarioadmin = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Usuario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblUsuarioadmin.Wrap( -1 )
		self.lblUsuarioadmin.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblUsuarioadmin, 0, wx.ALL, 5 )
		
		self.txtUsuarioAdmin = wx.TextCtrl( self.m_panel41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtUsuarioAdmin.SetFont( wx.Font( 8, 74, 90, 90, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.txtUsuarioAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.txtPassAdmin = wx.TextCtrl( self.m_panel41, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.txtPassAdmin, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText55 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Recuerde que la contraseña es sensible a Mayúsculas/Minúsculas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		self.m_staticText55.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		
		self.m_panel41.SetSizer( bSizer41 )
		self.m_panel41.Layout()
		bSizer41.Fit( self.m_panel41 )
		bSizer40.Add( self.m_panel41, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pagina2Wizard.SetSizer( bSizer40 )
		self.pagina2Wizard.Layout()
		self.pagina3Wizard = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.pagina3Wizard )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel59 = wx.Panel( self.pagina3Wizard, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer67 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText42 = wx.StaticText( self.m_panel59, wx.ID_ANY, u"Pregunta de seguridad ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		self.m_staticText42.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer67.Add( self.m_staticText42, 0, wx.ALL, 0 )
		
		self.m_staticText44 = wx.StaticText( self.m_panel59, wx.ID_ANY, u"En caso de Olvidar su Contraseña", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer67.Add( self.m_staticText44, 0, wx.ALL, 0 )
		
		self.m_staticText421 = wx.StaticText( self.m_panel59, wx.ID_ANY, u"Respuesta es sensible a Mayúsculas y Acentos", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )
		self.m_staticText421.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer67.Add( self.m_staticText421, 0, wx.ALL, 0 )
		
		
		self.m_panel59.SetSizer( bSizer67 )
		self.m_panel59.Layout()
		bSizer67.Fit( self.m_panel59 )
		bSizer47.Add( self.m_panel59, 1, wx.ALL, 0 )
		
		self.m_staticline14 = wx.StaticLine( self.pagina3Wizard, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer47.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel45 = wx.Panel( self.pagina3Wizard, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer48 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblPreguntaSeg = wx.StaticText( self.m_panel45, wx.ID_ANY, u"Escoja una Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPreguntaSeg.Wrap( -1 )
		self.lblPreguntaSeg.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer48.Add( self.lblPreguntaSeg, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Seleccione....", u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.m_panel45, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		bSizer48.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel45.SetSizer( bSizer48 )
		self.m_panel45.Layout()
		bSizer48.Fit( self.m_panel45 )
		bSizer47.Add( self.m_panel45, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel46 = wx.Panel( self.pagina3Wizard, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer49 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblRespuestaSeg = wx.StaticText( self.m_panel46, wx.ID_ANY, u"Ingrese la Respuesta a la pregunta Escojida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRespuestaSeg.Wrap( -1 )
		self.lblRespuestaSeg.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer49.Add( self.lblRespuestaSeg, 0, wx.ALL, 5 )
		
		self.txtRespuestaSeg = wx.TextCtrl( self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer49.Add( self.txtRespuestaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel46.SetSizer( bSizer49 )
		self.m_panel46.Layout()
		bSizer49.Fit( self.m_panel46 )
		bSizer47.Add( self.m_panel46, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pagina3Wizard.SetSizer( bSizer47 )
		self.pagina3Wizard.Layout()
		self.pagina4Wizard = wx.wizard.WizardPageSimple( self  )
		self.add_page( self.pagina4Wizard )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel50 = wx.Panel( self.pagina4Wizard, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText39 = wx.StaticText( self.m_panel50, wx.ID_ANY, u"Finalizada la Configuración Inicial?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer55.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel50.SetSizer( bSizer55 )
		self.m_panel50.Layout()
		bSizer55.Fit( self.m_panel50 )
		bSizer54.Add( self.m_panel50, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.pagina4Wizard.SetSizer( bSizer54 )
		self.pagina4Wizard.Layout()
		bSizer54.Fit( self.pagina4Wizard )
		self.Centre( wx.BOTH )
		
		
		# Connect Events
		self.Bind( wx.wizard.EVT_WIZARD_CANCEL, self.WizardConfigInicialOnWizardCancel )
		self.Bind( wx.wizard.EVT_WIZARD_FINISHED, self.WizardConfigInicialOnWizardFinished )
		self.Bind( wx.wizard.EVT_WIZARD_PAGE_CHANGED, self.WizardConfigInicialOnWizardPageChanged )
		self.Bind( wx.wizard.EVT_WIZARD_PAGE_CHANGING, self.WizardConfigInicialOnWizardPageChanging )
		self.choiceEntFed.Bind( wx.EVT_CHOICE, self.choiceEntFedOnChoice )
	def add_page(self, page):
		if self.m_pages:
			previous_page = self.m_pages[-1]
			page.SetPrev(previous_page)
			previous_page.SetNext(page)
		self.m_pages.append(page)
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def WizardConfigInicialOnWizardCancel( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardFinished( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardPageChanged( self, event ):
		event.Skip()
	
	def WizardConfigInicialOnWizardPageChanging( self, event ):
		event.Skip()
	
	def choiceEntFedOnChoice( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameRecuerdaPass
###########################################################################

class FrameRecuerdaPass ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Olvidó su Contraseña?", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerFrameRecuerdaPass = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1RecuerdaPass = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1RecuerdaPass1 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1_1RecuerdaPass1 = wx.Panel( self.panel1RecuerdaPass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerpanel1_1RecuerdaPass = wx.BoxSizer( wx.VERTICAL )
		
		self.lblPreguntaSeg = wx.StaticText( self.panel1_1RecuerdaPass1, wx.ID_ANY, u"Escoja una Pregunta de Seguridad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblPreguntaSeg.Wrap( -1 )
		self.lblPreguntaSeg.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerpanel1_1RecuerdaPass.Add( self.lblPreguntaSeg, 0, wx.ALL, 5 )
		
		choicePreguntaSegChoices = [ u"Cual es mi segundo Nombre?", u"Cual es el apellido de soltera de mi madre?", u"Cual es el apellido de soltero de mi padre?", u"Cual es el nombre de mi mascota?" ]
		self.choicePreguntaSeg = wx.Choice( self.panel1_1RecuerdaPass1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choicePreguntaSegChoices, 0 )
		self.choicePreguntaSeg.SetSelection( 0 )
		sizerpanel1_1RecuerdaPass.Add( self.choicePreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel1_1RecuerdaPass1.SetSizer( sizerpanel1_1RecuerdaPass )
		self.panel1_1RecuerdaPass1.Layout()
		sizerpanel1_1RecuerdaPass.Fit( self.panel1_1RecuerdaPass1 )
		sizerPanel1RecuerdaPass1.Add( self.panel1_1RecuerdaPass1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel1_2RecuerdaPass = wx.Panel( self.panel1RecuerdaPass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1_2RecuerdaPass = wx.BoxSizer( wx.VERTICAL )
		
		self.lblRespPreguntaSeg = wx.StaticText( self.panel1_2RecuerdaPass, wx.ID_ANY, u"Ingrese una Respuesta a la pregunta Escojida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblRespPreguntaSeg.Wrap( -1 )
		self.lblRespPreguntaSeg.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanel1_2RecuerdaPass.Add( self.lblRespPreguntaSeg, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self.panel1_2RecuerdaPass, wx.ID_ANY, u"La respuesta es sensible a letras Mayúsculas/Minúsculas.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		self.m_staticText46.SetFont( wx.Font( 8, 74, 93, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanel1_2RecuerdaPass.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.txtRespPreguntaSeg = wx.TextCtrl( self.panel1_2RecuerdaPass, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		sizerPanel1_2RecuerdaPass.Add( self.txtRespPreguntaSeg, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panel1_2RecuerdaPass.SetSizer( sizerPanel1_2RecuerdaPass )
		self.panel1_2RecuerdaPass.Layout()
		sizerPanel1_2RecuerdaPass.Fit( self.panel1_2RecuerdaPass )
		sizerPanel1RecuerdaPass1.Add( self.panel1_2RecuerdaPass, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel1RecuerdaPass.SetSizer( sizerPanel1RecuerdaPass1 )
		self.panel1RecuerdaPass.Layout()
		sizerPanel1RecuerdaPass1.Fit( self.panel1RecuerdaPass )
		sizerFrameRecuerdaPass.Add( self.panel1RecuerdaPass, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.panel2RecuerdaPass = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1RecuerdaPass = wx.BoxSizer( wx.VERTICAL )
		
		self.panel1_1RecuerdaPass = wx.Panel( self.panel2RecuerdaPass, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanel1_1RecuerdaPass = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAcettarRecuerdaPass = wx.Button( self.panel1_1RecuerdaPass, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnAcettarRecuerdaPass.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanel1_1RecuerdaPass.Add( self.btnAcettarRecuerdaPass, 0, wx.ALL, 5 )
		
		self.btnCancelRecuerdaPass = wx.Button( self.panel1_1RecuerdaPass, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCancelRecuerdaPass.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		sizerPanel1_1RecuerdaPass.Add( self.btnCancelRecuerdaPass, 0, wx.ALL, 5 )
		
		
		self.panel1_1RecuerdaPass.SetSizer( sizerPanel1_1RecuerdaPass )
		self.panel1_1RecuerdaPass.Layout()
		sizerPanel1_1RecuerdaPass.Fit( self.panel1_1RecuerdaPass )
		sizerPanel1RecuerdaPass.Add( self.panel1_1RecuerdaPass, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.panel2RecuerdaPass.SetSizer( sizerPanel1RecuerdaPass )
		self.panel2RecuerdaPass.Layout()
		sizerPanel1RecuerdaPass.Fit( self.panel2RecuerdaPass )
		sizerFrameRecuerdaPass.Add( self.panel2RecuerdaPass, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( sizerFrameRecuerdaPass )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtRespPreguntaSeg.Bind( wx.EVT_TEXT_ENTER, self.txtRespPreguntaSegOnTextEnter )
		self.btnAcettarRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnAcettarRecuerdaPassOnButtonClick )
		self.btnCancelRecuerdaPass.Bind( wx.EVT_BUTTON, self.btnCancelRecuerdaPassOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtRespPreguntaSegOnTextEnter( self, event ):
		event.Skip()
	
	def btnAcettarRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelRecuerdaPassOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameProyeccion
###########################################################################

class FrameProyeccion ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Proyección de Profesor", pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerProyeccion = wx.BoxSizer( wx.VERTICAL )
		
		self.panelProyecion = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelProyeccion = wx.BoxSizer( wx.VERTICAL )
		
		self.panelEscojerProfesorProyeccion = wx.Panel( self.panelProyecion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelEscojerProfesorProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		sizerFechasProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel65 = wx.Panel( self.panelEscojerProfesorProyeccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer80 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText51 = wx.StaticText( self.m_panel65, wx.ID_ANY, u"Fecha de Inicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer80.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_datePickerFechaInicioProy = wx.DatePickerCtrl( self.m_panel65, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer80.Add( self.m_datePickerFechaInicioProy, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel65.SetSizer( bSizer80 )
		self.m_panel65.Layout()
		bSizer80.Fit( self.m_panel65 )
		sizerFechasProyeccion.Add( self.m_panel65, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panel66 = wx.Panel( self.panelEscojerProfesorProyeccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText52 = wx.StaticText( self.m_panel66, wx.ID_ANY, u"Fecha de Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		self.m_staticText52.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer81.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_datePickerFechaFinProy = wx.DatePickerCtrl( self.m_panel66, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer81.Add( self.m_datePickerFechaFinProy, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel66.SetSizer( bSizer81 )
		self.m_panel66.Layout()
		bSizer81.Fit( self.m_panel66 )
		sizerFechasProyeccion.Add( self.m_panel66, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer41.Add( sizerFechasProyeccion, 1, wx.EXPAND, 5 )
		
		self.lblProfesor = wx.StaticText( self.panelEscojerProfesorProyeccion, wx.ID_ANY, u"Escoja un Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblProfesor.Wrap( -1 )
		self.lblProfesor.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblProfesor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choiceProyeccionProfesorChoices = []
		self.m_choiceProyeccionProfesor = wx.Choice( self.panelEscojerProfesorProyeccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceProyeccionProfesorChoices, 0 )
		self.m_choiceProyeccionProfesor.SetSelection( 0 )
		bSizer41.Add( self.m_choiceProyeccionProfesor, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		sizerPenelEscojerProfesorProyeccion.Add( bSizer41, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelEscojerProfesorProyeccion.SetSizer( sizerPenelEscojerProfesorProyeccion )
		self.panelEscojerProfesorProyeccion.Layout()
		sizerPenelEscojerProfesorProyeccion.Fit( self.panelEscojerProfesorProyeccion )
		sizerPanelProyeccion.Add( self.panelEscojerProfesorProyeccion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.panelLeyendaEscojerProfesorProyeccion = wx.Panel( self.panelProyecion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerPanelLeyendaEscojerProfesorProyeccion = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.panelLeyendaEscojerProfesorProyeccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorProyeccion.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblLeyendaEscojerProfesorProyeccion = wx.StaticText( self.panelLeyendaEscojerProfesorProyeccion, wx.ID_ANY, u"Escoja un Lapso de Tiempo y un Profesor para generar su Proyeción de Asistencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaEscojerProfesorProyeccion.Wrap( -1 )
		SizerPanelLeyendaEscojerProfesorProyeccion.Add( self.lblLeyendaEscojerProfesorProyeccion, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.panelLeyendaEscojerProfesorProyeccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerPanelLeyendaEscojerProfesorProyeccion.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelLeyendaEscojerProfesorProyeccion.SetSizer( SizerPanelLeyendaEscojerProfesorProyeccion )
		self.panelLeyendaEscojerProfesorProyeccion.Layout()
		SizerPanelLeyendaEscojerProfesorProyeccion.Fit( self.panelLeyendaEscojerProfesorProyeccion )
		sizerPanelProyeccion.Add( self.panelLeyendaEscojerProfesorProyeccion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelBotonesEscojerProfesorProyeccion = wx.Panel( self.panelProyecion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesEscojerProfesorProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCrearProyeccionProfesor = wx.Button( self.panelBotonesEscojerProfesorProyeccion, wx.ID_ANY, u"Crear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorProyeccion.Add( self.btnCrearProyeccionProfesor, 0, wx.ALL, 5 )
		
		self.btnCancelarProyeccionProfesor = wx.Button( self.panelBotonesEscojerProfesorProyeccion, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorProyeccion.Add( self.btnCancelarProyeccionProfesor, 0, wx.ALL, 5 )
		
		
		self.panelBotonesEscojerProfesorProyeccion.SetSizer( sizerPanelBotonesEscojerProfesorProyeccion )
		self.panelBotonesEscojerProfesorProyeccion.Layout()
		sizerPanelBotonesEscojerProfesorProyeccion.Fit( self.panelBotonesEscojerProfesorProyeccion )
		sizerPanelProyeccion.Add( self.panelBotonesEscojerProfesorProyeccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelReportProy = wx.Panel( self.panelProyecion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanelProyeccion.Add( self.panelReportProy, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelProyecion.SetSizer( sizerPanelProyeccion )
		self.panelProyecion.Layout()
		sizerPanelProyeccion.Fit( self.panelProyecion )
		sizerProyeccion.Add( self.panelProyecion, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerProyeccion )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameProyeccionOnClose )
		self.m_choiceProyeccionProfesor.Bind( wx.EVT_CHOICE, self.m_choiceProyeccionProfesorOnChoice )
		self.btnCrearProyeccionProfesor.Bind( wx.EVT_BUTTON, self.btnCrearProyeccionProfesorOnButtonClick )
		self.btnCancelarProyeccionProfesor.Bind( wx.EVT_BUTTON, self.btnCancelarProyeccionProfesorOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameProyeccionOnClose( self, event ):
		event.Skip()
	
	def m_choiceProyeccionProfesorOnChoice( self, event ):
		event.Skip()
	
	def btnCrearProyeccionProfesorOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarProyeccionProfesorOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class FrameCoreccionAsistencia
###########################################################################

class FrameCoreccionAsistencia ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Corrección de Asistencia Docente", pos = wx.DefaultPosition, size = wx.Size( 1150,495 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sizerCorreccion = wx.BoxSizer( wx.VERTICAL )
		
		self.panelCorreccion = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelProyeccion = wx.BoxSizer( wx.VERTICAL )
		
		self.panelEscojerProfesorCorreccion = wx.Panel( self.panelCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPenelEscojerProfesorProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		sizerFechasProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel65 = wx.Panel( self.panelEscojerProfesorCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer80 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText51 = wx.StaticText( self.m_panel65, wx.ID_ANY, u"Fecha de Inicio", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		self.m_staticText51.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer80.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_datePickerFechaInicioCorreccion = wx.DatePickerCtrl( self.m_panel65, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer80.Add( self.m_datePickerFechaInicioCorreccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel65.SetSizer( bSizer80 )
		self.m_panel65.Layout()
		bSizer80.Fit( self.m_panel65 )
		sizerFechasProyeccion.Add( self.m_panel65, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panel66 = wx.Panel( self.panelEscojerProfesorCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText52 = wx.StaticText( self.m_panel66, wx.ID_ANY, u"Fecha de Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		self.m_staticText52.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer81.Add( self.m_staticText52, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_datePickerFechaFinCorreccion = wx.DatePickerCtrl( self.m_panel66, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		bSizer81.Add( self.m_datePickerFechaFinCorreccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel66.SetSizer( bSizer81 )
		self.m_panel66.Layout()
		bSizer81.Fit( self.m_panel66 )
		sizerFechasProyeccion.Add( self.m_panel66, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer41.Add( sizerFechasProyeccion, 1, wx.EXPAND, 5 )
		
		self.lblProfesor = wx.StaticText( self.panelEscojerProfesorCorreccion, wx.ID_ANY, u"Escoja un Profesor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblProfesor.Wrap( -1 )
		self.lblProfesor.SetFont( wx.Font( 8, 74, 90, 92, False, "MS Shell Dlg 2" ) )
		
		bSizer41.Add( self.lblProfesor, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		m_choiceCorreccionProfesorChoices = []
		self.m_choiceCorreccionProfesor = wx.Choice( self.panelEscojerProfesorCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceCorreccionProfesorChoices, 0 )
		self.m_choiceCorreccionProfesor.SetSelection( 0 )
		bSizer41.Add( self.m_choiceCorreccionProfesor, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		sizerPenelEscojerProfesorProyeccion.Add( bSizer41, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.panelEscojerProfesorCorreccion.SetSizer( sizerPenelEscojerProfesorProyeccion )
		self.panelEscojerProfesorCorreccion.Layout()
		sizerPenelEscojerProfesorProyeccion.Fit( self.panelEscojerProfesorCorreccion )
		sizerPanelProyeccion.Add( self.panelEscojerProfesorCorreccion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		self.panelLeyendaEscojerProfesorCorreccion = wx.Panel( self.panelCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		SizerpanelLeyendaEscojerProfesorCorreccion = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline3 = wx.StaticLine( self.panelLeyendaEscojerProfesorCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerpanelLeyendaEscojerProfesorCorreccion.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.lblLeyendaEscojerProfesorCorreccion = wx.StaticText( self.panelLeyendaEscojerProfesorCorreccion, wx.ID_ANY, u"Escoja un Lapso de Tiempo y un Profesor para Corregir su Asistencia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLeyendaEscojerProfesorCorreccion.Wrap( -1 )
		SizerpanelLeyendaEscojerProfesorCorreccion.Add( self.lblLeyendaEscojerProfesorCorreccion, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.panelLeyendaEscojerProfesorCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		SizerpanelLeyendaEscojerProfesorCorreccion.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panelLeyendaEscojerProfesorCorreccion.SetSizer( SizerpanelLeyendaEscojerProfesorCorreccion )
		self.panelLeyendaEscojerProfesorCorreccion.Layout()
		SizerpanelLeyendaEscojerProfesorCorreccion.Fit( self.panelLeyendaEscojerProfesorCorreccion )
		sizerPanelProyeccion.Add( self.panelLeyendaEscojerProfesorCorreccion, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.panelBotonesEscojerProfesorProyeccion = wx.Panel( self.panelCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPanelBotonesEscojerProfesorProyeccion = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnMostrarAsistenciaProfesor = wx.Button( self.panelBotonesEscojerProfesorProyeccion, wx.ID_ANY, u"Ver", wx.DefaultPosition, wx.DefaultSize, 0 )
		sizerPanelBotonesEscojerProfesorProyeccion.Add( self.btnMostrarAsistenciaProfesor, 0, wx.ALL, 5 )
		
		
		self.panelBotonesEscojerProfesorProyeccion.SetSizer( sizerPanelBotonesEscojerProfesorProyeccion )
		self.panelBotonesEscojerProfesorProyeccion.Layout()
		sizerPanelBotonesEscojerProfesorProyeccion.Fit( self.panelBotonesEscojerProfesorProyeccion )
		sizerPanelProyeccion.Add( self.panelBotonesEscojerProfesorProyeccion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.panelFechasCorregir = wx.Panel( self.panelCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		sizerPanelProyeccion.Add( self.panelFechasCorregir, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel92 = wx.Panel( self.panelCorreccion, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer108 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCorregirAsistencia = wx.Button( self.m_panel92, wx.ID_ANY, u"Corregir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer108.Add( self.btnCorregirAsistencia, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnCancelarCorreccionProfesor = wx.Button( self.m_panel92, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer108.Add( self.btnCancelarCorreccionProfesor, 0, wx.ALL, 5 )
		
		
		self.m_panel92.SetSizer( bSizer108 )
		self.m_panel92.Layout()
		bSizer108.Fit( self.m_panel92 )
		sizerPanelProyeccion.Add( self.m_panel92, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.panelCorreccion.SetSizer( sizerPanelProyeccion )
		self.panelCorreccion.Layout()
		sizerPanelProyeccion.Fit( self.panelCorreccion )
		sizerCorreccion.Add( self.panelCorreccion, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerCorreccion )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.FrameCoreccionAsistenciaOnClose )
		self.m_choiceCorreccionProfesor.Bind( wx.EVT_CHOICE, self.m_choiceCorreccionProfesorOnChoice )
		self.btnMostrarAsistenciaProfesor.Bind( wx.EVT_BUTTON, self.btnMostrarAsistenciaProfesorOnButtonClick )
		self.btnCorregirAsistencia.Bind( wx.EVT_BUTTON, self.btnCorregirAsistenciaOnButtonClick )
		self.btnCancelarCorreccionProfesor.Bind( wx.EVT_BUTTON, self.btnCancelarCorreccionProfesorOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FrameCoreccionAsistenciaOnClose( self, event ):
		event.Skip()
	
	def m_choiceCorreccionProfesorOnChoice( self, event ):
		event.Skip()
	
	def btnMostrarAsistenciaProfesorOnButtonClick( self, event ):
		event.Skip()
	
	def btnCorregirAsistenciaOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelarCorreccionProfesorOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class Frame_CambioContrasena
###########################################################################

class Frame_CambioContrasena ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cambio de Contraseña Usuario Actual", pos = wx.DefaultPosition, size = wx.Size( 500,273 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel95 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer114 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel95, wx.ID_ANY, u"Contraseña Actual" ), wx.VERTICAL )
		
		self.txt_contrasenaActual_Cambio = wx.TextCtrl( self.m_panel95, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer10.Add( self.txt_contrasenaActual_Cambio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer114.Add( sbSizer10, 0, wx.EXPAND, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel95, wx.ID_ANY, u"Nueva Contraseña" ), wx.VERTICAL )
		
		self.txt_contrasenaNueva_Cambio = wx.TextCtrl( self.m_panel95, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		sbSizer11.Add( self.txt_contrasenaNueva_Cambio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer114.Add( sbSizer11, 0, wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel95, wx.ID_ANY, u"Confirme su Nueva Contraseña" ), wx.VERTICAL )
		
		self.txt_ConfirmaContrasenaNueva_Cambio = wx.TextCtrl( self.m_panel95, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		sbSizer12.Add( self.txt_ConfirmaContrasenaNueva_Cambio, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer114.Add( sbSizer12, 1, wx.EXPAND, 5 )
		
		bSizer115 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel96 = wx.Panel( self.m_panel95, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer116 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnCambioContrasena = wx.Button( self.m_panel96, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer116.Add( self.btnCambioContrasena, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelaCambioContrasena = wx.Button( self.m_panel96, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer116.Add( self.btnCancelaCambioContrasena, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.m_panel96.SetSizer( bSizer116 )
		self.m_panel96.Layout()
		bSizer116.Fit( self.m_panel96 )
		bSizer115.Add( self.m_panel96, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer114.Add( bSizer115, 1, wx.EXPAND, 5 )
		
		
		self.m_panel95.SetSizer( bSizer114 )
		self.m_panel95.Layout()
		bSizer114.Fit( self.m_panel95 )
		bSizer113.Add( self.m_panel95, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer113 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_CambioContrasenaOnClose )
		self.txt_ConfirmaContrasenaNueva_Cambio.Bind( wx.EVT_TEXT_ENTER, self.txt_ConfirmaContrasenaNueva_CambioOnTextEnter )
		self.btnCambioContrasena.Bind( wx.EVT_BUTTON, self.btnCambioContrasenaOnButtonClick )
		self.btnCancelaCambioContrasena.Bind( wx.EVT_BUTTON, self.btnCancelaCambioContrasenaOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Frame_CambioContrasenaOnClose( self, event ):
		event.Skip()
	
	def txt_ConfirmaContrasenaNueva_CambioOnTextEnter( self, event ):
		event.Skip()
	
	def btnCambioContrasenaOnButtonClick( self, event ):
		event.Skip()
	
	def btnCancelaCambioContrasenaOnButtonClick( self, event ):
		event.Skip()
	

