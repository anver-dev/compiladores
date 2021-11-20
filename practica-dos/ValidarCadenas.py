'''
Creado el: 12/11/2021
@author: Ana Karina Vergara Guzmán
@desciption: Programa que cuenta el total de tokens de tipo entero, flotante, booleanos, char y string
            en un archivo de texto.

'''
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from AutomataFD import AutomataFD

class Ventana(QMainWindow):
    scriptDir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):

        super(Ventana, self).__init__()
        self.setGeometry(50, 50, 777, 600)
        self.setWindowTitle(
            "Practica 2: Implementación de un automata finito determinista - AFD")
        self.setWindowIcon(QIcon(
            self.scriptDir + os.path.sep + "img/icon.png"))

        EventoSalir = QAction(QIcon(
            self.scriptDir + os.path.sep + 'img/salir.png'), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip("Salir de la aplicaión")
        EventoSalir.triggered.connect(self.cierraAplicacion)

        MenuPrincipal = self.menuBar()

        MenuArchivo = MenuPrincipal.addMenu("&Archivo")
        MenuArchivo.addAction(EventoSalir)

        self.home()

    def home(self):
        # Título
        self.titulo_lbl = QLabel(self)
        self.titulo_lbl.setText('Automata Finito Determinista - AFD')
        self.titulo_lbl.setFont(QFont("Arial", 14, QFont.Black))
        self.titulo_lbl.move(250, 80)
        self.titulo_lbl.adjustSize()

        # Imagen
        self.label = QLabel(self)
        self.pixmap = QPixmap(
            self.scriptDir + os.path.sep + 'img/automata.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        self.label.move(150, 120)

        # Lenguaje
        self.sigma_lbl = QLabel(self)
        self.sigma_lbl.setText('Lenguaje Sigma = { 1, 0 }')
        self.sigma_lbl.setFont(QFont("Arial", 12, QFont.Black))
        self.sigma_lbl.move(130, 320)
        self.sigma_lbl.adjustSize()

        # Cadena a evaluar
        self.cadena_a_evaluar_lbl = QLabel(self)
        self.cadena_a_evaluar_lbl.setText('Proporcione una cadena a evaluar: ')
        self.cadena_a_evaluar_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.cadena_a_evaluar_lbl.move(130, 360)
        self.cadena_a_evaluar_lbl.adjustSize()

        self.cadena_a_evaluar = QLineEdit(self)
        self.cadena_a_evaluar.resize(300, 25)
        self.cadena_a_evaluar.move(390, 360)

        # Comprobar cadena
        self.btn_comprobar_cadena = QPushButton("Comprobar", self)
        self.btn_comprobar_cadena.clicked.connect(self.comprobarCadena)
        self.btn_comprobar_cadena.resize(160, 30)
        self.btn_comprobar_cadena.move(130, 400)

        # Resultado de la evaluación
        self.resultado_evaluacion_lbl = QLabel(self)
        self.resultado_evaluacion_lbl.setText('Resultado de la evaluación: ')
        self.resultado_evaluacion_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.resultado_evaluacion_lbl.move(130, 460)
        self.resultado_evaluacion_lbl.adjustSize()

        self.resultado_evaluacion = QLineEdit(self)
        self.resultado_evaluacion.resize(355, 25)
        self.resultado_evaluacion.move(335, 460)

        # Salida de la aplicación
        self.EventoSalirLocal = QAction(
            QIcon(
                self.scriptDir + os.path.sep + 'img/exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierraAplicacion)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(self.EventoSalirLocal)

        self.show()

    def comprobarCadena(self):
        cadena = self.cadena_a_evaluar.text()
        objAutomata = AutomataFD()

        if self.validarLenguaje(cadena):
            if objAutomata.estadoCero(cadena, 0):
                self.imprimirMensajeDeExito(cadena)
            else:
                self.imprimirMensajeDeError(cadena)
        else:
            self.cadenaInvalida(cadena)

    def validarLenguaje(self, cadena):
        for caracter in cadena:
            if caracter != '0' and caracter != '1':
                return False
        return True

    def cadenaInvalida(self, cadena):
        msgError = "La cadena '" + cadena + "' es invalida. Intentalo nuevamente"
        
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(msgError)
        msg.setInformativeText('El lenguaje Sigma es: { 1, 0 } ')
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QIcon(
            self.scriptDir + os.path.sep + 'img/warning.png'))
        msg.exec_()
    
    def imprimirMensajeDeExito(self, cadena):
        self.resultado_evaluacion.setText("La cadena '" + cadena + "' SÍ pertenece al lenguaje")
        self.resultado_evaluacion.setStyleSheet("border: 1px solid green;")

    
    def imprimirMensajeDeError(self, cadena):
        self.resultado_evaluacion.setText("La cadena '" + cadena + "' NO pertenece al lenguaje")
        self.resultado_evaluacion.setStyleSheet("border: 2px solid red;")
    
    def cierraAplicacion(self):
        msgbox = QMessageBox(
            QMessageBox.Question, "Salir de aplicación", "Estás seguro de salir de la aplicación?")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)

        msgbox.setWindowIcon(QIcon(
            self.scriptDir + os.path.sep + 'img/warning.png'))
        reply = msgbox.exec()

        if(reply == QMessageBox.Yes):
            sys.exit()
        else:
            pass

def main():
    app = QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())


main()
