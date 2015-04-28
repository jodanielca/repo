# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

import gettext
_ = gettext.gettext

###########################################################################
## Class contenido
###########################################################################

class contenido ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Sistema de Creditos"), pos = wx.DefaultPosition, size = wx.Size( 1015,755 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.menuBar = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuBar.Append( self.m_menu1, _(u"Usuario:") ) 
		
		self.SetMenuBar( self.menuBar )
		
		sizerPrincipal = wx.BoxSizer( wx.VERTICAL )
		
		self.nb = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelPrestamos = wx.Panel( self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPrincipalPrestamos = wx.BoxSizer( wx.VERTICAL )
		
		self.herramientasPrestamos = wx.ToolBar( self.panelPrestamos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.herramientasPrestamos.Realize() 
		
		sizerPrincipalPrestamos.Add( self.herramientasPrestamos, 0, wx.EXPAND, 5 )
		
		sizerContenidosPrestamos = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerListadoPrestamos = wx.BoxSizer( wx.VERTICAL )
		
		self.listControlPrestamos = wx.dataview.DataViewListCtrl( self.panelPrestamos, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sizerListadoPrestamos.Add( self.listControlPrestamos, 1, wx.EXPAND, 5 )
		
		
		sizerContenidosPrestamos.Add( sizerListadoPrestamos, 1, wx.EXPAND, 5 )
		
		sizerDetallesPrestamos = wx.BoxSizer( wx.VERTICAL )
		
		self.nbDetalles = wx.Notebook( self.panelPrestamos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelDetallesCreditos = wx.Panel( self.nbDetalles, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbDetalles.AddPage( self.panelDetallesCreditos, _(u"Credito"), False )
		self.panelDetallesCliente = wx.Panel( self.nbDetalles, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbDetalles.AddPage( self.panelDetallesCliente, _(u"Cliente"), False )
		
		sizerDetallesPrestamos.Add( self.nbDetalles, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.herramientasDetalles = wx.ToolBar( self.panelPrestamos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.herramientasDetalles.Realize() 
		
		sizerDetallesPrestamos.Add( self.herramientasDetalles, 0, wx.EXPAND, 5 )
		
		self.nbCuotas = wx.Notebook( self.panelPrestamos, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelCuotasCreditos = wx.Panel( self.nbCuotas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbCuotas.AddPage( self.panelCuotasCreditos, _(u"Cuotas"), False )
		self.panelPagosCreditos = wx.Panel( self.nbCuotas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbCuotas.AddPage( self.panelPagosCreditos, _(u"Pagos"), False )
		
		sizerDetallesPrestamos.Add( self.nbCuotas, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerContenidosPrestamos.Add( sizerDetallesPrestamos, 1, wx.EXPAND, 5 )
		
		
		sizerPrincipalPrestamos.Add( sizerContenidosPrestamos, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelPrestamos.SetSizer( sizerPrincipalPrestamos )
		self.panelPrestamos.Layout()
		sizerPrincipalPrestamos.Fit( self.panelPrestamos )
		self.nb.AddPage( self.panelPrestamos, _(u"Prestamos"), False )
		self.panelClientes = wx.Panel( self.nb, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizerPrincipalClientes = wx.BoxSizer( wx.VERTICAL )
		
		self.herramientasClientes = wx.ToolBar( self.panelClientes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.herramientasClientes.Realize() 
		
		sizerPrincipalClientes.Add( self.herramientasClientes, 0, wx.EXPAND, 5 )
		
		sizerContenidosClientes = wx.BoxSizer( wx.HORIZONTAL )
		
		sizerListadoClientes = wx.BoxSizer( wx.VERTICAL )
		
		self.listControlPrestamos1 = wx.dataview.DataViewListCtrl( self.panelClientes, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		sizerListadoClientes.Add( self.listControlPrestamos1, 1, wx.EXPAND, 5 )
		
		
		sizerContenidosClientes.Add( sizerListadoClientes, 1, wx.EXPAND, 5 )
		
		sizerDetallesClientes = wx.BoxSizer( wx.VERTICAL )
		
		self.nbDetalles1 = wx.Notebook( self.panelClientes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelDetallesCreditos1 = wx.Panel( self.nbDetalles1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbDetalles1.AddPage( self.panelDetallesCreditos1, _(u"Credito"), False )
		self.panelDetallesCliente1 = wx.Panel( self.nbDetalles1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbDetalles1.AddPage( self.panelDetallesCliente1, _(u"Cliente"), False )
		
		sizerDetallesClientes.Add( self.nbDetalles1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.herramientasDetalles1 = wx.ToolBar( self.panelClientes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.herramientasDetalles1.Realize() 
		
		sizerDetallesClientes.Add( self.herramientasDetalles1, 0, wx.EXPAND, 5 )
		
		self.nbCuotas1 = wx.Notebook( self.panelClientes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelCuotasCreditos1 = wx.Panel( self.nbCuotas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbCuotas1.AddPage( self.panelCuotasCreditos1, _(u"Cuotas"), False )
		self.panelPagosCreditos1 = wx.Panel( self.nbCuotas1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbCuotas1.AddPage( self.panelPagosCreditos1, _(u"Pagos"), False )
		
		sizerDetallesClientes.Add( self.nbCuotas1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		sizerContenidosClientes.Add( sizerDetallesClientes, 1, wx.EXPAND, 5 )
		
		
		sizerPrincipalClientes.Add( sizerContenidosClientes, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.panelClientes.SetSizer( sizerPrincipalClientes )
		self.panelClientes.Layout()
		sizerPrincipalClientes.Fit( self.panelClientes )
		self.nb.AddPage( self.panelClientes, _(u"Clientes"), False )
		
		sizerPrincipal.Add( self.nb, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( sizerPrincipal )
		self.Layout()
		self.barraDeEstado = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.ver_detalles_creditos, id = wx.ID_ANY )
		self.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.ver_detalles_creditos, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ver_detalles_creditos( self, event ):
		event.Skip()
	
	

