'''
Creado el: 21/11/2021
@author: Ana Karina Vergara Guzmán
@desciption: Programa que valida si una cadena pertenece a un autómata dado.

'''
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from AutomataFND import AutomataFND
from AutomataFND_e import AutomataFND_e


class Ventana(QMainWindow):
    scriptDir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):

        super(Ventana, self).__init__()
        self.setGeometry(50, 50, 777, 800)
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
        self.Titulo_lbl.setText('Automata Finito No Determinista - AFND')
        self.Titulo_lbl.setFont(QFont("Arial", 14, QFont.Black))
        self.Titulo_lbl.move(250, 80)
        self.Titulo_lbl.adjustSize()

        # Imagen
        self.Img_lbl = QLabel(self)
        self.Pixmap = QPixmap(
            self.scriptDir + os.path.sep + 'img/automata.png')
        self.Img_lbl.setPixmap(self.Pixmap)
        self.Img_lbl.resize(self.Pixmap.width(), self.Pixmap.height())
        self.Img_lbl.move(150, 150)

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

        # Combo box
        self.Combo_lbl = QLabel(self)
        self.Combo_lbl.setText('Selecciona el tipo de Automata: ')
        self.Combo_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.Combo_lbl.move(130, 400)
        self.Combo_lbl.adjustSize()

        self.Combo = QComboBox(self)
        self.Combo.addItem("Selecciona una opción")
        self.Combo.addItem("Automata Finito No Determinista")
        self.Combo.addItem("Automata Finito No Determinista - épsilon")
        self.Combo.move(380, 400)
        self.Combo.adjustSize()
        self.Combo.currentIndexChanged.connect(self.cambiaImagen)

        # Comprobar cadena
        self.ComprobarCadena_btn = QPushButton("Comprobar", self)
        self.ComprobarCadena_btn.clicked.connect(self.comprobarCadena)
        self.ComprobarCadena_btn.resize(160, 30)
        self.ComprobarCadena_btn.move(130, 440)

        # Resultado de la evaluación
        self.ResultadoEvaluacion_lbl = QLabel(self)
        self.ResultadoEvaluacion_lbl.setText('Resultado de la evaluación: ')
        self.ResultadoEvaluacion_lbl.setFont(QFont("Arial", 11, QFont.Bold))
        self.ResultadoEvaluacion_lbl.move(130, 480)
        self.ResultadoEvaluacion_lbl.adjustSize()

        self.ResultadoEvaluacion_output = QTextEdit(self)
        self.ResultadoEvaluacion_output.resize(355, 200)
        self.ResultadoEvaluacion_output.move(335, 480)

        # Salida de la aplicación
        self.EventoSalirLocal = QAction(
            QIcon(
                self.scriptDir + os.path.sep + 'img/exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierraAplicacion)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(self.EventoSalirLocal)

        self.show()

    def cambiaImagen(self):

        tipoAutomataSeleccionado = self.Combo.currentText()

        if tipoAutomataSeleccionado == 'Selecciona una opción':
            self.Img_lbl.setPixmap(QPixmap(""))

        elif tipoAutomataSeleccionado == "Automata Finito No Determinista":
            self.Img_lbl.setPixmap(
                QPixmap(self.scriptDir + os.path.sep + 'img/afnd.png'))
            self.Img_lbl.setGeometry(120, 90, 500, 190)
            self.Img_lbl.move(190, 120)


        elif tipoAutomataSeleccionado == "Automata Finito No Determinista - épsilon":
            self.Img_lbl.setPixmap(
                QPixmap(self.scriptDir + os.path.sep + 'img/afnd-e.png'))
            self.Img_lbl.move(310, 120)

    def comprobarCadena(self):
        cadena = self.CadenaAEvaluar_input.text()
        tipoAutomataSeleccionado = self.Combo.currentText()

        if self.validarLenguaje(cadena):
            if tipoAutomataSeleccionado == 'Selecciona una opción':
                self.imprimirAlertaDeSeleccion()

            elif tipoAutomataSeleccionado == "Automata Finito No Determinista":
                self.validaAFND(cadena)

            elif tipoAutomataSeleccionado == "Automata Finito No Determinista - épsilon":
                self.validaAFNDe(cadena)
        else:
            self.cadenaInvalida(cadena)

    def validaAFND(self, cadena):
        AFND = AutomataFND()
        camino = []
        mensaje = ""

        AFND.inicio(cadena)

        for camino in AFND.CaminosEncontrados:
            mensaje = mensaje + " ".join(camino).replace("|", "->").replace(
                "Camino->Invalido", "Camino Invalido").replace("Camino->Valido", "Camino Valido") + "\n\n"
            self.ResultadoEvaluacion_output.setText(str(mensaje))
    
    def validaAFNDe(self, cadena):
        AFNDe = AutomataFND_e()
        camino = []
        mensaje = ""

        AFNDe.estadoCero(cadena)

        for camino in AFNDe.CaminosEncontrados:
            mensaje = mensaje + " ".join(camino).replace("|", "->").replace(
                "Camino->Invalido", "Camino Invalido").replace("Camino->Valido", "Camino Valido") + "\n\n"
            self.ResultadoEvaluacion_output.setText(str(mensaje))

    def imprimirAlertaDeSeleccion(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Seleccione el tipo de automata")
        msg.setInformativeText('')
        msg.setWindowTitle("Error")
        msg.setWindowIcon(QIcon(
            self.scriptDir + os.path.sep + 'img/warning.png'))
        msg.exec_()

    def validarLenguaje(self, cadena):
        if not cadena:
            return False
        for caracter in cadena:
            if caracter != '0' and caracter != '1':
                return False
        return True

    def cadenaInvalida(self, cadena):
        self.CadenaAEvaluar_input.setText("")
        self.ResultadoEvaluacion_output.setText("")

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
        self.ResultadoEvaluacion_output.setText(
            "La cadena '" + cadena + "' SÍ pertenece al lenguaje")
        self.ResultadoEvaluacion_output.setStyleSheet(
            "border: 1px solid green;")

    def imprimirMensajeDeError(self, cadena):
        self.ResultadoEvaluacion_output.setText(
            "La cadena '" + cadena + "' NO pertenece al lenguaje")
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
