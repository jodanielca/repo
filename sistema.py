#!/usr/bin/python
#-*- coding: latin-1 -*-
import wx
import sys
import wx.xrc
import wx.dataview
import wx.calendar
import time
import mysql_lib
from form import contenido

mysql = mysql_lib.mysql()
db 		= ["127.0.0.1","daniel","clave","cash"]
hoy			= time.strftime("%Y-%m-%d")


class main(contenido) :
	def __init__(self):
		# Llamamos al constructor de la clase frame_principal.
		contenido.__init__(self, None)
		
		#Esto puesto en __init__ funciona
		listaCreditos = self.listControlPrestamos
		listaCreditos.AppendTextColumn("Venta",width=45)
	#pero puesto fuera de la funcion me da error
	listaCreditos = self.listControlPrestamos
	listaCreditos.AppendTextColumn("Venta",width=45)

# Creamos la aplicación
app	= wx.App(False)
frame = main()
frame.Show()
app.MainLoop()
