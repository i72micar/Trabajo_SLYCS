# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 09:37:17 2021

@author: i72micar
"""

import sys
import random
from PyQt4 import QtCore
from PyQt4 import QtGui
from functools import partial

class SalaDlg(QtGui.QWidget):
    def __init__(self):
        super(SalaDlg, self).__init__()
        
        
        
        
        #Creamos los botones de la aplicación
        self.sumar=QtGui.QPushButton('Sumar')
     
        
        self.restar=QtGui.QPushButton('Restar')
            
        
        self.Multiplicar=QtGui.QPushButton('Multiplicar')
      
        self.Division=QtGui.QPushButton('Division')
        
        self.derivadas=QtGui.QPushButton('Derivar')
        
        self.integrales=QtGui.QPushButton('Integrar')
        
        self.det2x2=QtGui.QPushButton('Determinante2x2')
        
        self.det3x3=QtGui.QPushButton('Determinante 3x3')
        
        self.inv2x2=QtGui.QPushButton('Inversa 2x2')

        self.inv3x3=QtGui.QPushButton('Inversa 3x3')
        
        self.Examen=QtGui.QPushButton('Pregunta')
        
        self.botonSi = QtGui.QPushButton('Si')
        self.botonNo = QtGui.QPushButton('No')
        self.salir=QtGui.QPushButton('Salir')
        #Creación de ranuras para rellenar con numeros
        self.dato1 = QtGui.QLineEdit()
        self.dato2 = QtGui.QLineEdit()
        self.dato3 = QtGui.QLineEdit()
        self.dato4 = QtGui.QLineEdit()
        
        self.dato5 = QtGui.QLineEdit()
        self.dato6 = QtGui.QLineEdit()
        self.dato7 = QtGui.QLineEdit()
        self.dato8 = QtGui.QLineEdit()
        self.dato9 = QtGui.QLineEdit()
        self.dato10 = QtGui.QLineEdit()
        self.dato11 = QtGui.QLineEdit()
        self.dato12 = QtGui.QLineEdit()
        self.dato13 = QtGui.QLineEdit()
        self.dato14 = QtGui.QLineEdit()
        self.dato15 = QtGui.QLineEdit()
        self.dato16 = QtGui.QLineEdit()
        self.dato17 = QtGui.QLineEdit()
        self.dato18 = QtGui.QLineEdit()
        #Ranuras de explicación
        self.resultado = QtGui.QPlainTextEdit()
        self.resultado.setReadOnly(True)
        self.explicacion= QtGui.QPlainTextEdit()
        self.explicacion.setReadOnly(True)
        self.explicacion1 = QtGui.QPlainTextEdit()
        self.explicacion1.setReadOnly(True)
        self.grid = QtGui.QGridLayout();
        #Añadir a la ventana
        self.grid.addWidget(self.sumar,15,9)
        self.sumar.clicked.connect(self.mostrarBotonesSuma)
        self.grid.addWidget(self.restar,15,10)
        self.restar.clicked.connect(self.mostrarBotonesResta)
        self.grid.addWidget(self.Multiplicar,15,11)
        self.Multiplicar.clicked.connect(self.mostrarBotonesMultiplicar)
        self.grid.addWidget(self.Division,15,12)
        self.Division.clicked.connect(self.mostrarBotonesDivision)
        self.grid.addWidget(self.salir,15,13)
        self.salir.clicked.connect(self.Salir)
        self.grid.addWidget(self.derivadas,15,14)
        self.derivadas.clicked.connect(self.getDatosDerivadas)
        self.grid.addWidget(self.integrales,15,15)
        self.integrales.clicked.connect(self.getDatosIntegrales)
        self.grid.addWidget(self.det2x2,15,16)
        self.det2x2.clicked.connect(self.getDatosDMatriz2)
        self.grid.addWidget(self.det3x3,15,17)
        self.det3x3.clicked.connect(self.getDatosDMatriz3)
        self.grid.addWidget(self.inv2x2,15,18)
        self.inv2x2.clicked.connect(self.getDatosInversaMatriz2)
        self.grid.addWidget(self.inv3x3,15,19)
        self.inv3x3.clicked.connect(self.getDatosInversaMatriz3)
        self.grid.addWidget(self.Examen,15,20)
        self.Examen.clicked.connect(self.opciones)
        
        self.setWindowTitle('Calculadora')
        self.setLayout(self.grid);
        self.setGeometry(500,500,250,250)
        
        self.show();
        
    def mostrarBotonesSuma(self):
        #Creación de botones
        self.sumarR=QtGui.QPushButton('Sumar reales')
        self.sumarF=QtGui.QPushButton('Sumar fracciones')
        self.sumarM2=QtGui.QPushButton('Sumar matrices 2x2')
        self.sumarM3=QtGui.QPushButton('Sumar matrices 3x3') 
        
        
        self.grid.addWidget(self.sumarR,15,9)
        self.sumarR.clicked.connect(self.getDatosSR)
        self.grid.addWidget(self.sumarF,15,10)
        self.sumarF.clicked.connect(self.getDatosSF)
        self.grid.addWidget(self.sumarM2,15,11)
        self.sumarM2.clicked.connect(self.getDatosSM2)
        self.grid.addWidget(self.sumarM3,15,12)
        self.sumarM3.clicked.connect(self.getDatosSM3)
        self.Examen.hide()
        self.restar.hide()
        self.Division.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()
        self.show
        
    def mostrarBotonesResta(self):
        #Creación de botones
        self.restarR=QtGui.QPushButton('Restar reales')
        self.restarF=QtGui.QPushButton('Restar fracciones')
        self.restarM2=QtGui.QPushButton('Restar matrices 2x2')
        self.restarM3=QtGui.QPushButton('Restar matrices 3x3')
       
        self.grid.addWidget(self.restarR,15,9)
        self.restarR.clicked.connect(self.getDatosRR)
        self.grid.addWidget(self.restarF,15,10)
        self.restarF.clicked.connect(self.getDatosRF)
        self.grid.addWidget(self.restarM2,15,11)
        self.restarM2.clicked.connect(self.getDatosRM2)
        self.grid.addWidget(self.restarM3,15,12)
        self.restarM3.clicked.connect(self.getDatosRM3)
        self.Examen.hide()
        self.sumar.hide()
        self.Division.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()        
        self.show
        
    def mostrarBotonesMultiplicar(self):
        #Creación de botones
        self.MultiplicarR=QtGui.QPushButton('Multiplicar reales')
        self.MultiplicarF=QtGui.QPushButton('Multiplicar fracciones')
        self.MultiplicarM2=QtGui.QPushButton('Multiplicar matrices 2x2')
        self.MultiplicarM3=QtGui.QPushButton('Multiplicar matrices 3x3')   
       
        self.grid.addWidget(self.MultiplicarR,15,9)
        self.MultiplicarR.clicked.connect(self.getDatosMR)
        self.grid.addWidget(self.MultiplicarF,15,10)
        self.MultiplicarF.clicked.connect(self.getDatosMF)
        self.grid.addWidget(self.MultiplicarM2,15,11)
        self.MultiplicarM2.clicked.connect(self.getDatosMM2)
        self.grid.addWidget(self.MultiplicarM3,15,12)
        self.MultiplicarM3.clicked.connect(self.getDatosMM3)
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()  
        self.show
        
    def mostrarBotonesDivision(self):
        #Creación de botones
       self.DividirR=QtGui.QPushButton('Dividir reales')
       self.DividirF=QtGui.QPushButton('Dividir fracciones')
       self.DividirM2=QtGui.QPushButton('Dividir matrices 2x2')
       self.DividirM3=QtGui.QPushButton('Dividir matrices 3x3')     
       
       self.grid.addWidget(self.DividirR,15,9)
       self.DividirR.clicked.connect(self.getDatosDR)
       self.grid.addWidget(self.DividirF,15,10)
       self.DividirF.clicked.connect(self.getDatosDF)
       self.grid.addWidget(self.DividirM2,15,11)
       self.DividirM2.clicked.connect(self.getDatosDM2)
       self.grid.addWidget(self.DividirM3,15,12)
       self.DividirM3.clicked.connect(self.getDatosDM3)
       self.Examen.hide()
       self.sumar.hide()
       self.restar.hide()
       self.Multiplicar.hide()
       self.inv3x3.hide()
       self.det3x3.hide()
       self.derivadas.hide()
       self.integrales.hide()
       self.det2x2.hide()
       self.inv2x2.hide()  
       self.show
    def getDatosSR(self):
        #Obtención de datos para sumar 2 reales
        self.grid.addWidget(self.dato1,15,4)#Ranuras para el primer numero
        self.grid.addWidget(self.dato2,16,5)#Ranuras para el segundo numero
        
        self.Resultado=QtGui.QPushButton('Resultado')#Botón para llamar a la función que hace el cálculo    
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.sumarReales)
        self.show()
        
    def getDatosSF(self):
        #Obtención de datos para sumar 2 fracciones
        #Ranuras de la primera fracción
        self.grid.addWidget(self.dato1,16,4)#Numerador
        self.grid.addWidget(self.dato2,16,5)#Denominador
        #Ranuras de la segunda fracción
        self.grid.addWidget(self.dato3,17,4)#Numerador
        self.grid.addWidget(self.dato4,17,5)#Denominador
        self.Resultado=QtGui.QPushButton('Resultado')#Botón para llamar a la función que hace el cálculo     
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.sumarFracciones)
        self.show()
        
    def getDatosSM2(self):
        #Obtención de datos para sumar 2 matrices de 2x2
        #Ranuras de la Matriz 1   
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        #Ranuras de la Matriz 2
        self.grid.addWidget(self.dato5,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato6,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato7,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato8,17,9)#Fila2Columna2
        
        self.Resultado=QtGui.QPushButton('Resultado')#Botón para llamar a la función que hace el cálculo    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.sumarMatriz2)
        self.show()
        
    def getDatosSM3(self):
        #Ranuras de la Matriz1
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#Fila1Columna3
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato5,17,5)#Fila2Columna2
        self.grid.addWidget(self.dato6,17,6)#Fila2Columna3
        self.grid.addWidget(self.dato7,18,4)#Fila3Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila3Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila3Columna3
        #Ranuras de la Matriz2
        self.grid.addWidget(self.dato10,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato11,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato12,16,10)#Fila1Columna3   
        self.grid.addWidget(self.dato13,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato14,17,9)#Fila2Columna2
        self.grid.addWidget(self.dato15,17,10)#Fila2Columna3
        self.grid.addWidget(self.dato16,18,8)#Fila3Columna1
        self.grid.addWidget(self.dato17,18,9)#Fila3Columna2
        self.grid.addWidget(self.dato18,18,10)#Fila3Columna3
        
        self.Resultado=QtGui.QPushButton('Resultado')#Botón para llamar a la función que hace el cálculo     
        self.grid.addWidget(self.Resultado,15,9)
        
       
       
        self.Resultado.clicked.connect(self.sumarMatriz3)
        self.show()
        
    def sumarReales(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()
        a2=self.dato2.text()
        #Conversión a reales
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        #Operación de suma
        res= n1+n2
        #Conversión a string
        result=str(res)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,5)
        self.resultado.appendPlainText(result)
       #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write(a1 + ' + ' + a2 + ' = ' + result + '\n')
        self.show()
    def sumarFracciones(self):
        #Obtener datos de las ranuras        
        a1=self.dato1.text()  
        a2=self.dato2.text()  
        a3=self.dato3.text()  
        a4=self.dato4.text()   
        #Conversión a float
        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 1
            a2 = '1'

        else:
            
            n2=float(a2)
            
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 1
            a4 = '1'

        else:
            
            n4=float(a4)
            
       
        if(n2 == 0 or n4 == 0):#Control de errores
            result = 'Error division por 0 '
            f1 = a1+'/'+a2
            f2 = a3+'/'+a4
            res = f1 + f2
        else:
            #Operación de suma
            f1 = n1/n2
            f2 = n3/n4
            res= f1+f2
            result=str(res)
        #Conversión a string
        f1 = str(f1)
        f2 = str(f2)
        
        #Mostrar resultado
        self.grid.addWidget(self.resultado,18,5)
        self.resultado.appendPlainText(result)
        #Almacenar operación en ficher
        f = open('./operaciones', 'a')
        f.write(f1 + ' + ' + f2 + ' = ' + result + '\n')
        self.show()
   
    
    def sumarMatriz2(self):
        #Obtener valores de las ranuras
        #Matriz1        
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        #Matriz2
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
            
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
        #Conversión a float
        
        #Operación de suma
        M31= n1 +n5
        M32= n2 +n6
        M33= n3 +n7
        M34= n4 +n8
        #Conversióna string
        r1=str(M31)
        r2=str(M32)
        r3=str(M33)
        r4=str(M34)
        
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '
        linea3=' Matriz2_fila1 ['+ a5 + ' | ' + a6 + '] '
        linea4=' Matriz2_fila2 ['+ a7 + ' | ' + a8 + '] '
        result='['+ r1 + ' | ' + r2 +' ]'
        result1='['+ r3 + ' | ' + r4 +' ]'
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,10)
        self.resultado.appendPlainText(result)
        self.resultado.appendPlainText(result1)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write('Suma de Matrices2x2 ' + linea1 + linea2 + linea3 + linea4 + 'Resultado' + result + result1 + '\n')
        self.show()
    
    def sumarMatriz3(self):
        #Obtener datos de las ranuras
        #Matriz1
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()  
        #Matriz2
        a10=self.dato10.text()
        a11=self.dato11.text()  
        a12=self.dato12.text()  
        a13=self.dato13.text()  
        a14=self.dato14.text()
        a15=self.dato15.text()  
        a16=self.dato16.text() 
        a17=self.dato17.text()  
        a18=self.dato18.text() 
        #Conversión a float
        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        if (a10 == ''):
            n10 = 0
            a10 = '0'

        else:
            
            n10=float(a10)
        
        
        if (a11 == ''):
            n11 = 0
            a11 = '0'
        else:
            
            n11=float(a11)
        if (a12 == ''):
            n12 = 0
            a12 = '0'

        else:
            
            n12=float(a12)
            
            
        if (a13 == ''):
            n13 = 0
            a13 = '0'
        else:
            
            n13=float(a13)
        if (a14 == ''):
            n14 = 0
            a14 = '0'

        else:
            
            n14=float(a14)
            
            
            
        if (a15 == ''):
            n15 = 0
            a15 = '0'
        else:
            
            n15=float(a15)
        if (a16 == ''):
            n16= 0
            a16 = '0'

        else:
            
            n16=float(a16)
            
        if (a17 == ''):
            n17 = 0
            a17 = '0'
        else:
            
            n17=float(a17)
        if (a18 == ''):
            n18= 0 
            a18 = '0'
            

        else:
            
            n18=float(a18)
      
        #Operación de suma
        M31= n1 +n10
        M32= n2 +n11
        M33= n3 +n12
        M34= n4 +n13
        M35= n5 +n14
        M36= n6 +n15
        M37= n7 +n16
        M38= n8 +n17
        M39= n9 +n18
        
        M31= str(M31)
        M32= str(M32)
        M33= str(M33)
        M34= str(M34)
        M35= str(M35)
        M36= str(M36)
        M37= str(M37)
        M38= str(M38)
        M39= str(M39)
        
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        linea4=' Matriz2_fila1 ['+ a10 + ' | ' + a11 + ' | '+ a12 + ']'
        linea5=' Matriz2_fila2 ['+ a13 + ' | ' + a14 + ' | '+ a15 + ']'
        linea6=' Matriz2_fila3 ['+ a16 + ' | ' + a17 + ' | '+ a18 + ']'
        result='['+ M31 + ' | ' + M32 + ' | '+ M33 + ']'
        result1='['+ M34 + ' | ' + M35 + ' | '+ M36 + ']'
        result2='['+ M37 + ' | ' + M38 + ' | '+ M39 + ']'
        #Mostrar Resultado        
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        self.resultado.appendPlainText(result1)
        self.resultado.appendPlainText(result2)
        #Almacenar operación        
        f = open('./operaciones', 'a')
        f.write( 'Suma de Matrices3x3' + linea1 + linea2 + linea3 + linea4 + linea5 + linea6  +  'Resultado: ' + result + result1 + result2 + '\n')
        self.show()
        
        
        
    def getDatosRR(self):
        #Ranuras que representan los reales a restar
        self.grid.addWidget(self.dato1,15,4)
        self.grid.addWidget(self.dato2,16,5)
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.restarReales)#Función para restar reales
        self.show()
        
    def getDatosRF(self):
        #Ranuras que representan las fracciones
        #Fracción 1
        self.grid.addWidget(self.dato1,16,4)#Numerador
        self.grid.addWidget(self.dato2,16,5)#Denominador
        #Fracción 2
        self.grid.addWidget(self.dato3,17,4)#Numerador
        self.grid.addWidget(self.dato4,17,5)#Denominador
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.restarFracciones)#Función para restar fracciones
        self.show()
        
    def getDatosRM2(self):
        #Ranuras que representan las matrices2x2 a restar
        #Matriz1
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        #Matriz2
        self.grid.addWidget(self.dato5,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato6,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato7,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato8,17,9)#Fila2Columna2
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.restarMatriz2)#Función para restar matrices2x2
        self.show()
        
    def getDatosRM3(self):
        #Ranuras que represnetan las matrices3x3 a restar
        #Matriz1
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#Fila1Columna3
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato5,17,5)#Fila2Columna2
        self.grid.addWidget(self.dato6,17,6)#Fila2Columna3
        self.grid.addWidget(self.dato7,18,4)#Fila3Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila3Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila3Columna3
        #Matriz2
        self.grid.addWidget(self.dato10,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato11,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato12,16,10)#Fila1Columna3
        self.grid.addWidget(self.dato13,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato14,17,9)#Fila2Columna2
        self.grid.addWidget(self.dato15,17,10)#Fila2Columna3
        self.grid.addWidget(self.dato16,18,8)#Fila3Columna1
        self.grid.addWidget(self.dato17,18,9)#Fila3Columna2
        self.grid.addWidget(self.dato18,18,10)#Fila3Columna3
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)                   
        self.Resultado.clicked.connect(self.restarMatriz3)#Función para restar matrices3x3
        self.show()
        
    def restarReales(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()        
        #Conversioón a float        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        #Operación de resta
        res= n1-n2
        #Conversión a string
        result=str(res)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,5)
        self.resultado.appendPlainText(result)
        self.show()
        #Almacenar en fichero        
        f = open('./operaciones', 'a')
        f.write(a1 + ' - ' + a2 + ' = ' + result + '\n')
    def restarFracciones(self):
        #Obtener datos de las ranuras        
        a1=self.dato1.text()  
        a2=self.dato2.text()      
        a3=self.dato3.text()  
        a4=self.dato4.text()
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 1
            a2 = '1'

        else:
            
            n2=float(a2)
            
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 1
            a4 = '1'

        else:
            
            n4=float(a4)
        if(n2 == 0 or n4 == 0):#control de errores
            result = 'Error division por 0'
            f1 = a1+'/'+a2
            f2 = a3+'/'+a4
            res = f1 + f2
        else:            
            f1 = n1/n2
            f2 = n3/n4
            #Operación de resta
            res= f1-f2
            #Conversión a string
            result=str(res)
        f1 = str(f1)
        f2 = str(f2)
        
        #Mostrar resultado
        self.grid.addWidget(self.resultado,18,5)
        self.resultado.appendPlainText(result)
        #Almacenar en fichero
        f = open('./operaciones', 'a')
        f.write(f1 + ' - ' + f2 + ' = ' + result + '\n')
        self.show()
   
    
    def restarMatriz2(self):
        #Obtener datos de las ranuras
        #Matriz1        
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        #Matriz2
        a5=self.dato5.text()        
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text() 
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
            
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
        #Realizar operación
        M31= n1 -n5
        M32= n2 -n6
        M33= n3 -n7
        M34= n4 -n8
        #Conversión a string
        r1=str(M31)
        r2=str(M32)
        r3=str(M33)
        r4=str(M34)
        
        
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '
        linea3=' Matriz2_fila1 ['+ a5 + ' | ' + a6 + '] '
        linea4=' Matriz2_fila2 ['+ a7 + ' | ' + a8 + '] '
        result='['+ r1 + ' | ' + r2 +' ]'
        result1='['+ r3 + ' | ' + r4 +' ]'
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,18,10)
        self.resultado.appendPlainText(result1)
        #Alamacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write('Resta de Matrices2x2 ' + linea1 + linea2 + linea3 + linea4 + 'Resultado' + result + result1 + '\n')
        self.show()
    
    def restarMatriz3(self):
        #Obtener datos de las ranurass
        #Matriz1
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text() 
        #Matriz2
        a10=self.dato10.text()
        a11=self.dato11.text()  
        a12=self.dato12.text()  
        a13=self.dato13.text()  
        a14=self.dato14.text()
        a15=self.dato15.text()  
        a16=self.dato16.text() 
        a17=self.dato17.text()  
        a18=self.dato18.text() 
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        if (a10 == ''):
            n10 = 0
            a10 = '0'

        else:
            
            n10=float(a10)
        
        
        if (a11 == ''):
            n11 = 0
            a11 = '0'
        else:
            
            n11=float(a11)
        if (a12 == ''):
            n12 = 0
            a12 = '0'

        else:
            
            n12=float(a12)
            
            
        if (a13 == ''):
            n13 = 0
            a13 = '0'
        else:
            
            n13=float(a13)
        if (a14 == ''):
            n14 = 0
            a14 = '0'

        else:
            
            n14=float(a14)
            
            
            
        if (a15 == ''):
            n15 = 0
            a15 = '0'
        else:
            
            n15=float(a15)
        if (a16 == ''):
            n16= 0
            a16 = '0'

        else:
            
            n16=float(a16)
            
        if (a17 == ''):
            n17 = 0
            a17 = '0'
        else:
            
            n17=float(a17)
        if (a18 == ''):
            n18= 0 
            a18 = '0'
            

        else:
            
            n18=float(a18)
        #Operación de resta
        M31= n1 -n10
        M32= n2 -n11
        M33= n3 -n12
        M34= n4 -n13
        M35= n5 -n14
        M36= n6 -n15
        M37= n7 -n16
        M38= n8 -n17
        M39= n9 -n18
        #Conversión a string
        r1=str(M31)
        r2=str(M32)
        r3=str(M33)
        r4=str(M34)
        r5=str(M35)
        r6=str(M36)
        r7=str(M37)
        r8=str(M38)
        r9=str(M39)
        
       
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        linea4=' Matriz2_fila1 ['+ a10 + ' | ' + a11 + ' | '+ a12 + ']'
        linea5=' Matriz2_fila2 ['+ a13 + ' | ' + a14 + ' | '+ a15 + ']'
        linea6=' Matriz2_fila3 ['+ a16 + ' | ' + a17 + ' | '+ a18 + ']'
        
        result='['+ r1 + ' | ' + r2 + ' | '+ r3 + ']'
        result1='['+ r4 + ' | ' + r5 + ' | '+ r6 + ']'
        result2='['+ r7 + ' | ' + r8 + ' | '+ r9 + ']'
        #MostrarResultado
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,21,10)
        self.resultado.appendPlainText(result1)
        self.grid.addWidget(self.resultado,22,10)
        self.resultado.appendPlainText(result2)
        #Almacenar operación en fichero        
        f = open('./operaciones', 'a')
        f.write( 'Resta de matrices 3x3' + linea1 + linea2 + linea3 + linea4 + linea5 + linea6  +  'Resultado: ' + result + result1 + result2 + '\n')
        self.show()
        
        
    def getDatosMR(self):
        #Ranuras que representan los reales a multiplicar
        self.grid.addWidget(self.dato1,15,4)
        self.grid.addWidget(self.dato2,16,5)
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.MultiplicarReales)#Función que realiza la operación de multiplicación
        self.show()
        
    def getDatosMF(self):
        #Ranuras que representan las fracciones a multiplicar
        #Fracción 1        
        self.grid.addWidget(self.dato1,16,4)#Numerador
        self.grid.addWidget(self.dato2,16,5)#Denominador
        #Fracción 2
        self.grid.addWidget(self.dato3,17,4)#Numerador
        self.grid.addWidget(self.dato4,17,5)#Denominador
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.MultiplicarFracciones)#Función que realiza la operación de multiplicación
        self.show()
        
    def getDatosMM2(self):
        #Ranuras que representan las matrices2x2 a multiplicar
        #Matriz1
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        #Matriz2
        self.grid.addWidget(self.dato5,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato6,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato7,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato8,17,9)#Fila2Columna2
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        
       
       
        self.Resultado.clicked.connect(self.MultiplicarMatriz2)#Función que realiza la operación de multiplicación
        self.show()
        
    def getDatosMM3(self):
        #Ranuras que representan las matrices3x3 a multiplicar
        #Matriz1
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#Fila1Columna3
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato5,17,5)#Fila2Columna2
        self.grid.addWidget(self.dato6,17,6)#fila2Columna3
        self.grid.addWidget(self.dato7,18,4)#Fila3Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila3Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila3Columna3
        #Matriz2
        self.grid.addWidget(self.dato10,16,8)#Fila1Columna1
        self.grid.addWidget(self.dato11,16,9)#Fila1Columna2
        self.grid.addWidget(self.dato12,16,10)#Fila1columna3
        self.grid.addWidget(self.dato13,17,8)#Fila2Columna1
        self.grid.addWidget(self.dato14,17,9)#Fila2Columna2
        self.grid.addWidget(self.dato15,17,10)#Fila2Columna3
        self.grid.addWidget(self.dato16,18,8)#Fila3Columna1
        self.grid.addWidget(self.dato17,18,9)#Fila3Columna2
        self.grid.addWidget(self.dato18,18,10)#Fila3Columna3
        
        self.Resultado=QtGui.QPushButton('Resultado')
        self.show()    
        self.grid.addWidget(self.Resultado,15,9)
        
       
       
        self.Resultado.clicked.connect(self.MultiplicarMatriz3)#Función que realiza la operación de multiplicación
        self.show()
        
    def MultiplicarReales(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()        
        #Conversión a float        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        #Operación de multiplicación
        res= n1*n2
        #Conversión a string
        result=str(res)
        #Conversión a string        
        self.grid.addWidget(self.resultado,17,5)
        self.resultado.appendPlainText(result)
        #Alamacenar operación en fichero        
        f = open('./operaciones', 'a')
        f.write(a1 + ' x ' + a2 + ' = ' + result + '\n')
        self.show()
    def MultiplicarFracciones(self):
        #Obtener datos de las ranuras        
        a1=self.dato1.text()  
        a2=self.dato2.text() 
        a3=self.dato3.text()  
        a4=self.dato4.text() 
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 1
            a2 = '1'

        else:
            
            n2=float(a2)
            
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 1
            a4 = '1'

        else:
            
            n4=float(a4)
        if(n2 == 0 or n4 == 0):#Control de errores
            result = 'Error division por 0 '
            f1 = a1+'/'+a2
            f2 = a3+'/'+a4
            res = f1 + f2
        else:
            
            f1 = n1/n2
            f2 = n3/n4
            #operación de multiplicación
            res = f1*f2
            #Conversión a string
            result=str(res)
        f1 = str(f1)
        f2 = str(f2)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,18,5)
        self.resultado.appendPlainText(result)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write(f1 + ' / ' + f2 + ' = ' + result + '\n')
        self.show()
   
    
    def MultiplicarMatriz2(self):
        #Obtener datos de las ranuras 
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text() 
        #Conversión a float         
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
            
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
        #Operación de multiplicación
        M31= n1*n5 + n2*n7
        M32= n1*n6 + n2*n8 
        M33= n3*n5 + n4*n7
        M34= n3*n6 + n4*n8
        #Conversión a string
        r1=str(M31)
        r2=str(M32)
        r3=str(M33)
        r4=str(M34)
        
       
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '
        linea3=' Matriz2_fila1 ['+ a5 + ' | ' + a6 + '] '
        linea4=' Matriz2_fila2 ['+ a7 + ' | ' + a8 + '] '
        result='['+ r1 + ' | ' + r2 +' ]'
        result1='['+ r3 + ' | ' + r4 +' ]'
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,18,10)
        self.resultado.appendPlainText(result1)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write('Multiplicacion de Matrices2x2 ' + linea1 + linea2 + linea3 + linea4 + 'Resultado' + result + result1 + '\n')
        self.show()
    
    def MultiplicarMatriz3(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()  
        a10=self.dato10.text()
        a11=self.dato11.text()  
        a12=self.dato12.text()  
        a13=self.dato13.text()  
        a14=self.dato14.text()
        a15=self.dato15.text()  
        a16=self.dato16.text() 
        a17=self.dato17.text()  
        a18=self.dato18.text() 
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        if (a10 == ''):
            n10 = 0
            a10 = '0'

        else:
            
            n10=float(a10)
        
        
        if (a11 == ''):
            n11 = 0
            a11 = '0'
        else:
            
            n11=float(a11)
        if (a12 == ''):
            n12 = 0
            a12 = '0'

        else:
            
            n12=float(a12)
            
            
        if (a13 == ''):
            n13 = 0
            a13 = '0'
        else:
            
            n13=float(a13)
        if (a14 == ''):
            n14 = 0
            a14 = '0'

        else:
            
            n14=float(a14)
            
            
            
        if (a15 == ''):
            n15 = 0
            a15 = '0'
        else:
            
            n15=float(a15)
        if (a16 == ''):
            n16= 0
            a16 = '0'

        else:
            
            n16=float(a16)
            
        if (a17 == ''):
            n17 = 0
            a17 = '0'
        else:
            
            n17=float(a17)
        if (a18 == ''):
            n18= 0 
            a18 = '0'
            

        else:
            
            n18=float(a18)
        #Operación de multiplicación
        M31= n1 * n10 + n2 * n13 + n3 * n16
        M32= n1 * n11 + n2 * n14 + n3 * n17
        M33= n1 * n12 + n2 * n15 + n3 * n18
        M34= n4 * n10 + n5 * n13 + n6 * n16
        M35= n4 * n11 + n5 * n14 + n6 * n17
        M36= n4 * n12 + n5 * n15 + n6 * n18
        M37= n7 * n10 + n8 * n13 + n9 * n16
        M38= n7 * n11 + n8 * n14 + n9 * n17
        M39= n7 * n12 + n8 * n15 + n9 * n18
        #Convertir a string
        r1=str(M31)
        r2=str(M32)
        r3=str(M33)
        r4=str(M34)
        r5=str(M35)
        r6=str(M36)
        r7=str(M37)
        r8=str(M38)
        r9=str(M39)
        
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        linea4=' Matriz2_fila1 ['+ a10 + ' | ' + a11 + ' | '+ a12 + ']'
        linea5=' Matriz2_fila2 ['+ a13 + ' | ' + a14 + ' | '+ a15 + ']'
        linea6=' Matriz2_fila3 ['+ a16 + ' | ' + a17 + ' | '+ a18 + ']'
        result='['+ r1 + ' | ' + r2 + ' | '+ r3 + ']'
        result1='['+ r4 + ' | ' + r5 + ' | '+ r6 + ']'
        result2='['+ r7 + ' | ' + r8 + ' | '+ r9 + ']'
        #Mostrar resultado
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,21,10)
        self.resultado.appendPlainText(result1)
        self.grid.addWidget(self.resultado,22,10)
        self.resultado.appendPlainText(result2)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write( 'Multiplicacion de matrices 3x3' + linea1 + linea2 + linea3 + linea4 + linea5 + linea6  +  'Resultado: ' + result + result1 + result2 + '\n')

        self.show()
   
    def getDatosDR(self):
        #Ranuras que representan los reales a dividir
        self.grid.addWidget(self.dato1,15,4)
        self.grid.addWidget(self.dato2,16,5)
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.dividirReales)#Función que realiza la operación de división
        self.show()
        
    def getDatosDF(self):
        #Ranuras que representan las fracciones a dividir
        #Fracción 1
        self.grid.addWidget(self.dato1,16,4)#Numerador
        self.grid.addWidget(self.dato2,16,5)#Denominador
        #Fracción 2
        self.grid.addWidget(self.dato3,17,4)#Numerador
        self.grid.addWidget(self.dato4,17,5)#Denominador
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
       
       
        self.Resultado.clicked.connect(self.dividirFracciones)#Función que realiza la operación de división
        self.show()
        
    def getDatosDM2(self):
        #Ranuras que representan la matriz 2x2 y el denominador
        #Matriz
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        
        self.grid.addWidget(self.dato5,16,8)
      
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        
       
       
        self.Resultado.clicked.connect(self.dividirMatriz2)#Función que realiza la operación de división
        self.show()
        
    def getDatosDM3(self):
        #Ranuras que representan la matriz 3x3 y el denominador
        #Matriz
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#fila1Columna3
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato5,17,5)#Fila2Columna2
        self.grid.addWidget(self.dato6,17,6)#Fila2Columna3
        self.grid.addWidget(self.dato7,18,4)#Fila3Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila3Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila3Columna3
        
        self.grid.addWidget(self.dato10,16,8)
      
        
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        
       
       
        self.Resultado.clicked.connect(self.dividirMatriz3)#Función que realiza la operación de división
        self.show()
        
    def dividirReales(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()    
        #Conversión a float
    
        if (a1 == ''):
            n1 = 1
            a1 = '1'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 1
            a2 = '1'

        else:
            
            n2=float(a2)
        if(n2 == 0):#control de errores
            result = ' Error division por 0 '
            
        
        else:
            #Operación de división
            res= n1/n2
            result=str(res)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,5)
        self.resultado.appendPlainText(result)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write(a1 + ' / ' + a2 + ' = ' + result + '\n')
        self.show()
    def dividirFracciones(self):
        #Obtener datos de las ranuras        
        a1=self.dato1.text()  
        a2=self.dato2.text()   
        a3=self.dato3.text()  
        a4=self.dato4.text()   
             
        if (a1 == ''):
            n1 = 0
            a1 = '1'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 1
            a2 = '1'

        else:
            
            n2=float(a2)
            
        if (a3 == ''):
            n3 = 1
            a3 = '1'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 1
            a4 = '1'

        else:
            
            n4=float(a4)
        
        if(n2 == 0 or n4 == 0 or n3 == 0):
            result = ' Error division por 0 '
            f1 = a1+'/'+a2
            f2 = a3+'/'+a4
            res = f1 + f2
        else:
            f1 = n1/n2
            f2 = n3/n4
            #Operación de división    
            res= f1/f2
            #Conversión a string
            result=str(res)
        f1 = str(f1)
        f2 = str(f2)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,18,5)
        self.resultado.appendPlainText(result)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write(f1 + ' / ' + f2 + ' = ' + result + '\n')
        self.show()
   
    
    def dividirMatriz2(self):
        #Obtener  datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        #convertir a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 1
            a5 = '1'
            
        else:
            
            n5=float(a5)
        if(n5 == 0):#Control de errores
            result = 'Error division por 0 '
            result1 = '' 
        else:
            #Operación de división
            M31= n1 / n5
            M32= n2 / n5
            M33= n3 / n5
            M34= n4 / n5
            #Conversión a string
            r1=str(M31)
            r2=str(M32)
            r3=str(M33)
            r4=str(M34)
            
            
           
            result='['+ r1 + ' | ' + r2 +' ]'
            result1='['+ r3 + ' | ' + r4 +' ]'
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '    
        #Mostrar resultado        
        self.grid.addWidget(self.resultado,17,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,18,10)
        self.resultado.appendPlainText(result1)
        #Almacenar resultado en fichero
        f = open('./operaciones', 'a')
        f.write('Multiplicacion de Matrices2x2 ' + linea1 + linea2 + ' / '  + a5 + ' Resultado:' + result + result1 + '\n')
        self.show()
    
    def dividirMatriz3(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()  
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()  
        a10=self.dato10.text()
       
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        if (a10 == ''):
            n10 = 1
            a10 = '1'

        else:
            
            n10=float(a10)
       
        if(n10 == 0):#Control de errores
           result = ' Error division por 0 '
           result1 = ' '
           result2 = ' '
        else:   
        
            #Operación de división
            M31= n1/n10
            M32= n2/n10
            M33= n3/n10
            M34= n4/n10
            M35= n5/n10
            M36= n6/n10
            M37= n7/n10
            M38= n8/n10
            M39= n9/n10
            #Conversión a string
            r1=str(M31)
            r2=str(M32)
            r3=str(M33)
            r4=str(M34)
            r5=str(M35)
            r6=str(M36)
            r7=str(M37)
            r8=str(M38)
            r9=str(M39)
            
            
            
            
            result='['+ r1 + ' | ' + r2 + ' | '+ r3 + ']'
            result1='['+ r4 + ' | ' + r5 + ' | '+ r6 + ']'
            result2='['+ r7 + ' | ' + r8 + ' | '+ r9 + ']'
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        #Mostrar resultados        
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,21,10)
        self.resultado.appendPlainText(result1)
        self.grid.addWidget(self.resultado,22,10)
        self.resultado.appendPlainText(result2)
        #Almacenar operación en fichero
        f = open('./operaciones', 'a')
        f.write( 'Multiplicacion de matrices 3x3' + linea1 + linea2 + linea3 + ' / ' + a10  +  ' Resultado: ' + result + result1 + result2 + '\n')

        self.show()
        
    def getDatosDerivadas(self):
        #Ranurad que representan el coeficiente y la potencia
        self.grid.addWidget(self.dato1,16,4)#Coeficiente
        self.grid.addWidget(self.dato2,16,5)#Potencia
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,11)
        self.Resultado.clicked.connect(self.derivar)#Función que realiza la derivada
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.Division.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()  
        
        
    def derivar(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        #Conversión a float
        if (a1 == ''):
            r1 = 1
            a1 = '1'
        else:
            
            r1=float(a1)
        if (a2 == ''):
            r2 = 1
            a2 = '1'

        else:
            
            r2=float(a2)
        if(r2 == 0 or r1 == 0):
            #Derivada caso base
            result = '0'
        else :
            #Derivada
            r1=r1*r2
            r2=r2-1
            #Convertur a string
            coe=str(r1)
            exp=str(r2)
            
            result = coe + 'x ^ ' +exp
        #Mostrar resultado
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        #Almacenar operación en fichero        
        f = open('./operaciones', 'a')
        f.write( 'Derivada de ' + a1 + 'x' + '^' + a2  +  ' Resultado: ' +  result + '\n')

        
    def getDatosIntegrales(self):
        #Ranuras que representan el coeficiente y la potencia 
        self.grid.addWidget(self.dato1,16,4)
        self.grid.addWidget(self.dato2,16,5)
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,11)
        self.Resultado.clicked.connect(self.Integrar)
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.Division.hide()
        self.det2x2.hide()
        self.inv2x2.hide()  
        
        
    def Integrar(self):
        #Datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        #Convertir a float
        if (a1 == ''):
            r1 = 0
            a1 = '1'
        else:
            
            r1=float(a1)
        if (a2 == ''):
            r2 = 0
            a2 = '1'

        else:
            
            r2=float(a2)
        #Caso base
        if(r2 == 0) :
            result = a1 + 'x + C'
            result1=''
            result2=''
            self.grid.addWidget(self.resultado,20,10)
            self.resultado.appendPlainText(result)
        else :
            
            pot=r2 + 1#Integral
            
            coe=str(r1)
            exp=str(pot)
            #Mostrar resultado
            result = coe + '^' + exp 
            self.grid.addWidget(self.resultado,20,10)
            self.resultado.appendPlainText(result)
            result1 = '----------'
            self.grid.addWidget(self.resultado,21,10)
            self.resultado.appendPlainText(result1)
            
            result2 = exp
            self.grid.addWidget(self.resultado,21,10)
            self.resultado.appendPlainText(result2)
            #Almacenar operaciones 
        f = open('./operaciones', 'a')
        f.write( 'Integral de ' + a1 + 'x' + '^' + a2  +  'Resultado: ' + result + 'dividido' + result2 +' +C '+' \n')

            
    def getDatosDMatriz2(self):            
        
        #Ranuras que representan los elementos de la matriz
        self.grid.addWidget(self.dato1,16,4)
        self.grid.addWidget(self.dato2,16,5)
        self.grid.addWidget(self.dato3,17,4)
        self.grid.addWidget(self.dato4,17,5)
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.detM2)
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.Division.hide()
        self.inv2x2.hide()  
        
        
    def detM2(self):
        #Obtener datos
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        #Convertir a float        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '
        
        #Operación para calcular el determinante de una matriz2x2
        resultado = (n1*n4) - (n2 * n3)
        result= str(resultado)
        #Mostrar resultado
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        #Guardar operación
        f = open('./operaciones', 'a')
        f.write( 'Determinante de  ' + linea1  + linea2  +  'Resultado: ' + result + ' \n')

        
    def getDatosDMatriz3(self):
        #Ranuras que representan los datos de la matriz
        self.grid.addWidget(self.dato1,16,4)
        self.grid.addWidget(self.dato2,16,5)
        self.grid.addWidget(self.dato3,16,6)
        self.grid.addWidget(self.dato4,17,4)
        self.grid.addWidget(self.dato5,17,5)
        self.grid.addWidget(self.dato6,17,6)
        self.grid.addWidget(self.dato7,18,4)
        self.grid.addWidget(self.dato8,18,5)
        self.grid.addWidget(self.dato9,18,6)
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.detM3)#Función que calcula el determinante de una matriz 3x3
        self.show()
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.Division.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()  
        
    def detM3(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()
        #Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        #Calculo del determinante de una matriz 3x3
        resultado = ((n1 * n5 * n9) + (n2 *n6 * n7) + (n3 * n4 * n8)) - ((n2 * n4 * n9) + (n1 * n6 * n8) + (n3 * n5 * n7))
        #conversión a string
        result = str(resultado)
        #Mostrar resultado
        self.resultado.appendPlainText(result)
        #guardar operación
        f = open('./operaciones', 'a')
        f.write( 'Determinante de  ' + linea1  + linea2  + linea3 + 'Resultado: ' + result + ' \n')
        
        
    def getDatosInversaMatriz2(self): 
        #Ranuras que representan la matriz           
        self.grid.addWidget(self.dato1,16,4)
        self.grid.addWidget(self.dato2,16,5)
        self.grid.addWidget(self.dato3,17,4)
        self.grid.addWidget(self.dato4,17,5)
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.inversaM2)#Función que calcula la matriz inversa
        self.show()    
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.inv3x3.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.Division.hide()  
    
    def inversaM2(self):
        #Obtener datos 
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        #Conversión a float        
        if (a1 == ''):
            r1 = 0
            a1 = '0'
            
        else:
            
            r1=float(a1)
        if (a2 == ''):
            r2 = 0
            a2 = '0'

        else:
            
            r2=float(a2)
        
        
        if (a3 == ''):
            r3 = 0
            a3 = '0'
        else:
            
            r3=float(a3)
        if (a4 == ''):
            r4 = 0
            a4 = '0'

        else:
            
            r4=float(a4)
        #Claculo del determinante
        determinante = (r1*r4) - (r2 * r3)
        #Evitar error división por 0
        if(determinante == 0):
            result=' Error division por 0'
            result1=''
        else :
            #Cálculo de matriz adjunta traspuesta
            r2 = r2 * -1
            r3 = r3 * -1
            
            aux = r1
            r1 = r4
            r4 = aux
            #Calculo de la matriz inversa
            r1 = r1 / determinante
            r2 = r2 / determinante
            r3 = r3 / determinante
            r4 = r4 / determinante
            
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            result='['+ r1 + ' | ' + r2 +' ]'
            result1='['+ r3 + ' | ' + r4 +' ]'
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + '] '
        linea2=' Matriz1_fila2 ['+ a3 + ' | ' + a4 + '] '
        
        
        #Mostrar resultado
        self.grid.addWidget(self.resultado,17,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,18,10)
        self.resultado.appendPlainText(result1)
        #Guardar operación en fichero
        f = open('./operaciones', 'a')
        f.write( 'Inversa de  ' + linea1  + linea2  + 'Resultado: ' + result + result1 +' \n')
        
    
    def getDatosInversaMatriz3(self):      
        #Ranuras que represnetan los elementos de la matriz
        self.grid.addWidget(self.dato1,16,4)
        self.grid.addWidget(self.dato2,16,5)
        self.grid.addWidget(self.dato3,16,6)
        self.grid.addWidget(self.dato4,17,4)
        self.grid.addWidget(self.dato5,17,5)
        self.grid.addWidget(self.dato6,17,6)
        self.grid.addWidget(self.dato7,18,4)
        self.grid.addWidget(self.dato8,18,5)
        self.grid.addWidget(self.dato9,18,6)
        self.Resultado=QtGui.QPushButton('Resultado')    
        self.grid.addWidget(self.Resultado,15,9)
        self.Resultado.clicked.connect(self.inversaM3)#Función que calcula la inversa de una matriz 3x3
        self.Examen.hide()
        self.sumar.hide()
        self.restar.hide()
        self.Multiplicar.hide()
        self.Division.hide()
        self.det3x3.hide()
        self.derivadas.hide()
        self.integrales.hide()
        self.det2x2.hide()
        self.inv2x2.hide()          
        self.show()
    
    def inversaM3(self):
        #Obtener datos de las ranuras
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()
        ##Conversión a float
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        #Cálculo del determinante 
        determinante = ((n1 * n5 * n9) + (n2 *n6 * n7) + (n3 * n4 * n8)) - ((n2 * n4 * n9) + (n1 * n6 * n8) + (n3 * n5 * n7))
        
        if(determinante == 0):
            #Caso de división por 0
            result=' Error division por 0'
            result1=''
            result2=''
        else :   
            #Calculo de la matriz adjunta
            a11 = (n5 * n9) - (n6 * n8)
            a12 = ((n4 * n9) - (n6 * n7)) * -1
            a13 = (n4 * n8) - (n5 * n7)
            a21 = ((n2 * n9) - (n3 * n8)) * -1
            a22 = (n1 * n9) - (n3 * n7)
            a23 = ((n1 * n8) - (n2 * n7)) * -1
            a31 = (n2 * n6) - (n3 * n5)
            a32 = ((n1 * n6) - (n3 * n4)) * -1
            a33 = (n1 * n5) - (n2 * n4)
            #Cálculo de la matriz adjunta traspuesta
            #Cálculo de la inversa
            r11 = a11 / determinante
            r12 = a21 / determinante
            r13 = a31 / determinante
            r21 = a12 / determinante
            r22 = a22 / determinante
            r23 = a32 / determinante
            r31 = a13 / determinante
            r32 = a23 / determinante
            r33 = a33 / determinante
            #Conversión a string
            r11 = str(r11)
            r12 = str(r12)
            r13 = str(r13)
            r21 = str(r21)
            r22 = str(r22)
            r23 = str(r23)
            r31 = str(r31)
            r32 = str(r32)
            r33 = str(r33)
            
            result= '['+ r11 +  ' | ' + r12 + ' | '+ r13 + ']'
            result1='['+ r21 + ' | ' + r22 + ' | '+ r23 + ']'
            result2='['+ r31 + ' | ' + r32 + ' | '+ r33 + ']'
        
        linea1=' Matriz1_fila1 ['+ a1 + ' | ' + a2 + ' | '+ a3 + '] '
        linea2=' Matriz1_fila2 ['+ a4 + ' | ' + a5 + ' | '+ a6 + '] '
        linea3=' Matriz1_fila3 ['+ a7 + ' | ' + a8 + ' | '+ a9 + '] '
        #Mostrar resultado
        self.grid.addWidget(self.resultado,20,10)
        self.resultado.appendPlainText(result)
        self.grid.addWidget(self.resultado,21,10)
        self.resultado.appendPlainText(result1)
        self.grid.addWidget(self.resultado,22,10)
        self.resultado.appendPlainText(result2)
        #guardar operación
        f = open('./operaciones', 'a')
        f.write( 'Inversa de  ' + linea1  + linea2  + linea3 +'Resultado: ' + result + result1 + result2 +' \n')
        
    def opciones(self):
       self.Pregunta1=QtGui.QPushButton('Multiplicar matrices 2x2')
       self.Pregunta2=QtGui.QPushButton('Multiplicar matrices 3x3')
       self.Pregunta3=QtGui.QPushButton('Determinante y adjunta traspuesta 2x2')
       self.Pregunta4=QtGui.QPushButton('Determinante y adjunta traspuesta 3x3')     
       
       self.grid.addWidget(self.Pregunta1,15,9)
       self.Pregunta1.clicked.connect(self.propuestaM2x2)
       self.grid.addWidget(self.Pregunta2,15,10)
       self.Pregunta2.clicked.connect(self.propuestaM3x3)
       self.grid.addWidget(self.Pregunta3,15,11)
       self.Pregunta3.clicked.connect(self.propuestaD2x2)
       self.grid.addWidget(self.Pregunta4,15,12)
       self.Pregunta4.clicked.connect(self.propuestaD3x3)
       
       self.Examen.hide()
       self.sumar.hide()
       self.restar.hide()
       self.Multiplicar.hide()
       self.inv3x3.hide()
       self.det3x3.hide()
       self.derivadas.hide()
       self.integrales.hide()
       self.det2x2.hide()
       self.inv2x2.hide()  
       
       
    def propuestaM2x2(self):
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        n3=random.randint(1,9)
        n4=random.randint(1,9)
        n5=random.randint(1,9)
        n6=random.randint(1,9)
        n7=random.randint(1,9)
        n8=random.randint(1,9)
        
        a1=str(n1)
        a2=str(n2)
        a3=str(n3)
        a4=str(n4)
        a5=str(n5)
        a6=str(n6)
        a7=str(n7)
        a8=str(n8)
        
        enunciado='['+a1 +'|'+ a2+']    ['+a5+'|'+ a6+'] '
        enunciado1='            *                 ?'
        enunciado2='['+a3 +'|'+ a4+']    ['+a7+'|'+ a8+'] '
        self.grid.addWidget(self.explicacion,20,10)
        self.explicacion.appendPlainText(enunciado)
        self.explicacion.appendPlainText(enunciado1)
        self.explicacion.appendPlainText(enunciado2)
       
       
        M31= n1*n5 + n2*n7
        M32= n1*n6 + n2*n8 
        M33= n3*n5 + n4*n7
        M34= n3*n6 + n4*n8
        
        self.check=QtGui.QPushButton('Comprobar resultado')
        self.grid.addWidget(self.check,20,9)
        self.check.clicked.connect(partial(self.checkM2x2,M31,M32,M33,M34))
        self.Pregunta1.hide()
        self.Pregunta2.hide()
        self.Pregunta3.hide()
        self.Pregunta4.hide()
        self.Division.hide()
        
    def checkM2x2(self,M31,M32,M33,M34):
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        
        
        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
       
        
        
        if(n1 == M31 and n2 == M32 and n3 == M33 and n4 == M34):
            mensaje = ' Correcto'
            
        else :
            mensaje = ' Incorrecto'
        
        self.explicacion.appendPlainText(mensaje)
        
    def propuestaM3x3(self):
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna2
        self.grid.addWidget(self.dato5,17,5)#Fila1Columna1
        self.grid.addWidget(self.dato6,17,6)#Fila1Columna2
        self.grid.addWidget(self.dato7,18,4)#Fila2Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila2Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila2Columna2
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        n3=random.randint(1,9)
        n4=random.randint(1,9)
        n5=random.randint(1,9)
        n6=random.randint(1,9)
        n7=random.randint(1,9)
        n8=random.randint(1,9)
        n9=random.randint(1,9)
        n10=random.randint(1,9)
        n11=random.randint(1,9)
        n12=random.randint(1,9)
        n13=random.randint(1,9)
        n14=random.randint(1,9)
        n15=random.randint(1,9)
        n16=random.randint(1,9)
        n17=random.randint(1,9)
        n18=random.randint(1,9)
        
        a1=str(n1)
        a2=str(n2)
        a3=str(n3)
        a4=str(n4)
        a5=str(n5)
        a6=str(n6)
        a7=str(n7)
        a8=str(n8)
        
        a9=str(n9)
        a10=str(n10)
        a11=str(n11)
        a12=str(n12)
        a13=str(n13)
        a14=str(n14)
        a15=str(n15)
        a16=str(n16)
        a17=str(n17)
        a18=str(n18)
        enunciado='['+a1 +'|'+ a2+ '|'+ a3+']    ['+a10+'|'+ a11+'|'+a12 +'] '
        enunciado1='['+a4 +'|'+ a5+ '|'+ a6+'] *  ['+a13+'|'+ a14+'|'+a15 +'] ?'
        enunciado2='['+a7 +'|'+ a8+ '|'+ a9+']    ['+a16+'|'+ a17+'|'+a18 +']'
        self.grid.addWidget(self.explicacion,20,10)
        self.explicacion.appendPlainText(enunciado)
        self.explicacion.appendPlainText(enunciado1)
        self.explicacion.appendPlainText(enunciado2)
       
       
        M31= n1 * n10 + n2 * n13 + n3 * n16
        M32= n1 * n11 + n2 * n14 + n3 * n17
        M33= n1 * n12 + n2 * n15 + n3 * n18
        M34= n4 * n10 + n5 * n13 + n6 * n16
        M35= n4 * n11 + n5 * n14 + n6 * n17
        M36= n4 * n12 + n5 * n15 + n6 * n18
        M37= n7 * n10 + n8 * n13 + n9 * n16
        M38= n7 * n11 + n8 * n14 + n9 * n17
        M39= n7 * n12 + n8 * n15 + n9 * n18
        self.Pregunta1.hide()
        self.Pregunta2.hide()
        self.Pregunta3.hide()
        self.Pregunta4.hide()
        self.Division.hide()
        self.check=QtGui.QPushButton('Comprobar resultado')
        self.grid.addWidget(self.check,20,9)
        self.check.clicked.connect(partial(self.checkM3x3,M31,M32,M33,M34,M35,M36,M37,M38,M39))
        
        
    def checkM3x3(self,M31,M32,M33,M34,M35,M36,M37,M38,M39):
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()
        
        
        
        if (a1 == ''):
            n1 = 0
            a1 = '0'
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            a2 = '0'

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            a3 = '0'
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            a4 = '0'

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            a5 = '0'
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            a6 = '0'

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            a7 = '0'
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            a8 = '0'

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
            a9 = '0'
        else:
            
            n9=float(a9)
        
        
        if(n1 == M31 and n2 == M32 and n3 == M33 and n4 == M34 and n5 == M35 and n6 == M36 and n7 == M37 and n8 == M38 and n9 == M39):
            mensaje = ' Correcto'
            
        else :
            mensaje = ' Incorrecto'
        
        self.explicacion.appendPlainText(mensaje)
        
        
        
        
       
    def propuestaD2x2(self):
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,17,4)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,5)#Fila2Columna2
        self.grid.addWidget(self.dato5,18,6)#Fila2Columna2
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        n3=random.randint(1,9)
        n4=random.randint(1,9)
        
        
        a1=str(n1)
        a2=str(n2)
        a3=str(n3)
        a4=str(n4)
        
        
        enunciado='['+a1 +'|'+ a2+']     '
        enunciado1='Determinante y adjunta traspuesta de:                      ?'
        enunciado2='['+a3 +'|'+ a4+'] '
        self.grid.addWidget(self.explicacion,20,10)
        self.explicacion.appendPlainText(enunciado1)
        self.explicacion.appendPlainText(enunciado)
        self.explicacion.appendPlainText(enunciado2)
       
        determinante = (n1*n4) - (n2 * n3)
       #Cálculo de matriz adjunta traspuesta
        n2 = n2 * -1
        n3 = n3 * -1
        
        aux = n1
        n1 = n4
        n4 = aux
        self.Pregunta1.hide()
        self.Pregunta2.hide()
        self.Pregunta3.hide()
        self.Pregunta4.hide()
        self.Division.hide()
        self.check=QtGui.QPushButton('Comprobar resultado')
        self.grid.addWidget(self.check,20,9)
        self.check.clicked.connect(partial(self.checkD2x2,n1,n2,n3,n4,determinante))
        
        
    def checkD2x2(self,M31,M32,M33,M34,determinante):
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        a5=self.dato5.text()
        
        
        if (a1 == ''):
            r1 = 0
            a1 = '0'
            
        else:
            
            r1=float(a1)
        if (a2 == ''):
            r2 = 0
            a2 = '0'

        else:
            
            r2=float(a2)
        
        
        if (a3 == ''):
            r3 = 0
            a3 = '0'
        else:
            
            r3=float(a3)
        if (a4 == ''):
            r4 = 0
            a4 = '0'

        else:
            
            r4=float(a4)
        if (a5 == ''):
            r5 = 0
            a5 = '0'

        else:
            
            r5=float(a5)
        
        if(r1 == M31 and r2 == M32 and r3 == M33 and r4 == M34):
            mensaje = 'Adjunta traspuesta  Correcto'
            self.explicacion.appendPlainText(mensaje)
            
        else :
            mensaje = 'Adjunta traspuesta  Incorrecto'
            self.explicacion.appendPlainText(mensaje)
        
        if(r5 ==  determinante):
            mensaje = 'Determinante  Correcto'
            self.explicacion.appendPlainText(mensaje)
            
        else :
            mensaje = 'Determinante  Incorrecto'
            self.explicacion.appendPlainText(mensaje)
    def propuestaD3x3(self):
        self.grid.addWidget(self.dato1,16,4)#Fila1Columna1
        self.grid.addWidget(self.dato2,16,5)#Fila1Columna2
        self.grid.addWidget(self.dato3,16,6)#Fila2Columna1
        self.grid.addWidget(self.dato4,17,4)#Fila2Columna2
        self.grid.addWidget(self.dato5,17,5)#Fila1Columna1
        self.grid.addWidget(self.dato6,17,6)#Fila1Columna2
        self.grid.addWidget(self.dato7,18,4)#Fila2Columna1
        self.grid.addWidget(self.dato8,18,5)#Fila2Columna2
        self.grid.addWidget(self.dato9,18,6)#Fila2Columna2
        self.grid.addWidget(self.dato10,19,5)#Fila2Columna2
        n1=random.randint(1,9)
        n2=random.randint(1,9)
        n3=random.randint(1,9)
        n4=random.randint(1,9)
        n5=random.randint(1,9)
        n6=random.randint(1,9)
        n7=random.randint(1,9)
        n8=random.randint(1,9)
        n9=random.randint(1,9)
        
        
        a1=str(n1)
        a2=str(n2)
        a3=str(n3)
        a4=str(n4)
        a5=str(n5)
        a6=str(n6)
        a7=str(n7)
        a8=str(n8)
        a9=str(n9)
        
        enunciado4='Determinante y adjunta traspuesta de:'
        enunciado='['+a1 +'|'+ a2+ '|'+ a3+']'
        enunciado1='['+a4 +'|'+ a5+ '|'+ a6+']'
        enunciado2='['+a7 +'|'+ a8+ '|'+ a9+']'    
        self.grid.addWidget(self.explicacion,20,10)
        self.explicacion.appendPlainText(enunciado)
        self.explicacion.appendPlainText(enunciado1)
        self.explicacion.appendPlainText(enunciado2)
       
        #Cálculo del determinante 
        determinante = ((n1 * n5 * n9) + (n2 *n6 * n7) + (n3 * n4 * n8)) - ((n2 * n4 * n9) + (n1 * n6 * n8) + (n3 * n5 * n7))
        
        #Calculo de la matriz adjunta
        a11 = (n5 * n9) - (n6 * n8)
        a12 = ((n4 * n9) - (n6 * n7)) * -1
        a13 = (n4 * n8) - (n5 * n7)
        a21 = ((n2 * n9) - (n3 * n8)) * -1
        a22 = (n1 * n9) - (n3 * n7)
        a23 = ((n1 * n8) - (n2 * n7)) * -1
        a31 = (n2 * n6) - (n3 * n5)
        a32 = ((n1 * n6) - (n3 * n4)) * -1
        a33 = (n1 * n5) - (n2 * n4)
        
        r11 = a11 
        r12 = a21
        r13 = a31 
        r21 = a12 
        r22 = a22 
        r23 = a32 
        r31 = a13 
        r32 = a23 
        r33 = a33 
        self.Pregunta1.hide()
        self.Pregunta2.hide()
        self.Pregunta3.hide()
        self.Pregunta4.hide()
        self.Division.hide()
        self.check=QtGui.QPushButton('Comprobar resultado')
        self.grid.addWidget(self.check,20,9)
        self.check.clicked.connect(partial(self.checkD3x3,r11,r12,r13,r21,r22,r23,r31,r32,r33,determinante))
        
        
    def checkD3x3(self,M31,M32,M33,M34,M35,M36,M37,M38,M39,determinante):
        a1=self.dato1.text()  
        a2=self.dato2.text()
        a3=self.dato3.text()  
        a4=self.dato4.text()
        a5=self.dato5.text()  
        a6=self.dato6.text()
        a7=self.dato7.text()  
        a8=self.dato8.text()
        a9=self.dato9.text()
        a10=self.dato10.text()
        
        
        
        
        
        
        if (a1 == ''):
            n1 = 0
            
        else:
            
            n1=float(a1)
        if (a2 == ''):
            n2 = 0
            

        else:
            
            n2=float(a2)
        
        
        if (a3 == ''):
            n3 = 0
            
        else:
            
            n3=float(a3)
        if (a4 == ''):
            n4 = 0
            

        else:
            
            n4=float(a4)
            
            
        if (a5 == ''):
            n5 = 0
            
        else:
            
            n5=float(a5)
        if (a6 == ''):
            n6 = 0
            

        else:
            
            n6=float(a6)
            
            
            
        if (a7 == ''):
            n7 = 0
            
        else:
            
            n7=float(a7)
        if (a8 == ''):
            n8 = 0
            

        else:
            
            n8=float(a8)
            
        if (a9 == ''):
            n9 = 0
           
        else:
            
            n9=float(a9)
            
        if (a10 == ''):
            n10 = 0
            
        else:
            
            n10=float(a10)
        
        
        
  
        if(n1 == M31 and n2 == M32 and n3 == M33 and n4 == M34 and n5 == M35 and n6 == M36 and n7 == M37 and n8 == M38 and n9 == M39):
            mensaje = 'Adjunta traspuesta correcta'
            self.explicacion.appendPlainText(mensaje)
            
        else :
            mensaje = 'Adjunta traspuesta incorrecta'
            self.explicacion.appendPlainText(mensaje)
        
        if(n10 == determinante):
            mensaje = 'determinante correcto'
            self.explicacion.appendPlainText(mensaje)
        else :
            mensaje = 'Determinante incorrecto'
            self.explicacion.appendPlainText(mensaje)
    def Salir(self):
        sys.exit(0)
if __name__ == "__main__":
   
    app = QtGui.QApplication(sys.argv)
    form = SalaDlg()
    sys.exit(app.exec_())