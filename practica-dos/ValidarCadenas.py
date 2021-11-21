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
        self.Titulo_lbl = QLabel(self)
        self.Titulo_lbl.setText('Automata Finito Determinista - AFD')
        self.Titulo_lbl.setFont(QFont("Arial", 14, QFont.Black))
        self.Titulo_lbl.move(250, 80)
        self.Titulo_lbl.adjustSize()

        # Imagen
        self.Img_lbl = QLabel(self)
        self.Pixmap = QPixmap(
            self.scriptDir + os.path.sep + 'img/automata.png')
        self.Img_lbl.setPixmap(self.Pixmap)
        self.Img_lbl.resize(self.Pixmap.width(), self.Pixmap.height())
        self.Img_lbl.move(150, 120)

        # Lenguaje
        self.Sigma_lbl = QLabel(self)
        self.Sigma_lbl.setText('Lenguaje Sigma = { 1, 0 }')
        self.Sigma_lbl.setFont(QFont("Arial", 12, QFont.Black))
        self.Sigma_lbl.move(130, 320)
        self.Sigma_lbl.adjustSize()

        # Cadena a evaluar
        self.CadenaAEvaluar_lbl = QLabel(self)
        self.CadenaAEvaluar_lbl.setText('Proporcione una cadena a evaluar: ')
        self.CadenaAEvaluar_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.CadenaAEvaluar_lbl.move(130, 360)
        self.CadenaAEvaluar_lbl.adjustSize()

        self.CadenaAEvaluar_input = QLineEdit(self)
        self.CadenaAEvaluar_input.resize(300, 25)
        self.CadenaAEvaluar_input.move(390, 360)

        # Comprobar cadena
        self.ComprobarCadena_btn = QPushButton("Comprobar", self)
        self.ComprobarCadena_btn.clicked.connect(self.comprobarCadena)
        self.ComprobarCadena_btn.resize(160, 30)
        self.ComprobarCadena_btn.move(130, 400)

        # Resultado de la evaluación
        self.ResultadoEvaluacion_lbl = QLabel(self)
        self.ResultadoEvaluacion_lbl.setText('Resultado de la evaluación: ')
        self.ResultadoEvaluacion_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.ResultadoEvaluacion_lbl.move(130, 460)
        self.ResultadoEvaluacion_lbl.adjustSize()

        self.ResultadoEvaluacion_output = QLineEdit(self)
        self.ResultadoEvaluacion_output.resize(355, 25)
        self.ResultadoEvaluacion_output.move(335, 460)

        # Salida de la aplicación
        self.EventoSalirLocal = QAction(
            QIcon(
                self.scriptDir + os.path.sep + 'img/exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierraAplicacion)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(self.EventoSalirLocal)

        self.show()

    def comprobarCadena(self):
        cadena = self.CadenaAEvaluar_input.text()
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
        self.ResultadoEvaluacion_output.setText("La cadena '" + cadena + "' SÍ pertenece al lenguaje")
        self.ResultadoEvaluacion_output.setStyleSheet("border: 1px solid green;")

    
    def imprimirMensajeDeError(self, cadena):
        self.ResultadoEvaluacion_output.setText("La cadena '" + cadena + "' NO pertenece al lenguaje")
        self.ResultadoEvaluacion_output.setStyleSheet("border: 2px solid red;")
    
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
