# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:34:08 2021

@author: i72micar
"""

import sys
from PyQt4 import QtGui
import funciones as f


app = QtGui.QApplication(sys.argv) #Crea una aplicación
form = f.SalaDlg()   #Crea una instancia del formulario
sys.exit(app.exec_())   #Se inicia la aplicación y se espera eventos