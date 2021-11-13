'''
Creado el: 12/11/2021
@author: Ana Karina Vergara Guzmán
@desciption: Programa que cuenta el total de tokens de tipo entero, flotante, booleanos, char y string
            en un archivo de texto.

'''
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ventana(QtWidgets.QMainWindow):
    scriptDir = os.path.dirname(os.path.realpath(__file__))

    def __init__(self):

        super(Ventana, self).__init__()
        self.setGeometry(50, 50, 650, 450)
        self.setWindowTitle("Ejemplo ventana")
        self.setWindowIcon(QtGui.QIcon(
            self.scriptDir + os.path.sep + "icon.png"))

        self.openFile = QtWidgets.QAction(QtGui.QIcon(
            self.scriptDir + os.path.sep + 'open.png'), '&Abrir Archivo', self)
        self.openFile.setShortcut("Ctrl+O")
        self.openFile.setStatusTip("Abrir Archivo")
        self.openFile.triggered.connect(self.abrirArchivo)

        EventoSalir = QtWidgets.QAction(QtGui.QIcon(
            self.scriptDir + os.path.sep + 'salir.png'), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip("Salir de la aplicaión")
        EventoSalir.triggered.connect(self.cierraAplicacion)

        MenuPrincipal = self.menuBar()

        MenuArchivo = MenuPrincipal.addMenu("&Archivo")
        MenuArchivo.addAction(self.openFile)
        MenuArchivo.addSeparator()
        MenuArchivo.addAction(EventoSalir)

        self.home()

    def home(self):
        self.bandera_abrir = False

        self.btn_ContarTokens = QtWidgets.QPushButton("Contar tokens", self)

        self.Resultados = QtWidgets.QTextEdit(self)

        self.total_int = QtWidgets.QLineEdit(self)
        self.int_lbl = QtWidgets.QLabel("Numero de tokens de tipo int:", self)

        self.total_float = QtWidgets.QLineEdit(self)
        self.float_lbl = QtWidgets.QLabel(
            "Numero de tokens de tipo float:", self)

        self.total_boolean = QtWidgets.QLineEdit(self)
        self.boolean_lbl = QtWidgets.QLabel(
            "Numero de tokens de tipo boolean:", self)

        self.total_chars = QtWidgets.QLineEdit(self)
        self.chars_lbl = QtWidgets.QLabel(
            "Numero de tokens de tipo chars:", self)

        self.total_strings = QtWidgets.QLineEdit(self)
        self.strings_lbl = QtWidgets.QLabel(
            "Numero de tokens de tipo strings:", self)

        EventoAbrirLocal = QtWidgets.QAction(
            QtGui.QIcon(
                self.scriptDir + os.path.sep + 'open.png'), 'Abrir un Archivo', self)
        EventoAbrirLocal.triggered.connect(self.abrirArchivo)

        self.btn_ContarTokens.clicked.connect(self.contarTokens)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(EventoAbrirLocal)

        self.EventoSalirLocal = QtWidgets.QAction(
            QtGui.QIcon(
                self.scriptDir + os.path.sep + 'exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierraAplicacion)

        self.BarraOpciones.addAction(self.EventoSalirLocal)

        self.Resultados.resize(400, 370)
        self.Resultados.move(10, 65)

        self.btn_ContarTokens.resize(160, 30)
        self.btn_ContarTokens.move(450, 65)

        self.int_lbl.move(450, 105)
        self.int_lbl.adjustSize()
        self.total_int.resize(200, 30)
        self.total_int.move(430, 120)

        self.float_lbl.move(445, 160)
        self.float_lbl.adjustSize()
        self.total_float.resize(200, 30)
        self.total_float.move(430, 175)

        self.boolean_lbl.move(445, 215)
        self.boolean_lbl.adjustSize()
        self.total_boolean.resize(200, 30)
        self.total_boolean.move(430, 230)

        self.chars_lbl.move(445, 270)
        self.chars_lbl.adjustSize()
        self.total_chars.resize(200, 30)
        self.total_chars.move(430, 285)

        self.strings_lbl.move(445, 325)
        self.strings_lbl.adjustSize()
        self.total_strings.resize(200, 30)
        self.total_strings.move(430, 340)

        self.show()

    def abrirArchivo(self):
        vOpenFileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", filter="*.txt")[0]

        if(vOpenFileName == ""):
            return

        f = open(vOpenFileName, "r")
        vTextString = f.read()
        self.Resultados.setText(vTextString)

        f.close()
        self.bandera_abrir = True

    def esInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    def esFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def esBoolean(self, value):
        if(value == "True" or value == "False"):
            return True
        else:
            return False

    def esChar(self, value):
        if(len(value) == 1):
            return True
        else:
            return False

    def esString(self, value):
        try:
            str(value)
            return True
        except ValueError:
            return False

    def obtenerTokens(self):
        contenidoArchivo = self.Resultados.toPlainText()
        lineas = contenidoArchivo.split('\n')
        tokens = []

        for linea in lineas:
            tokensEnLinea = linea.split(" ")
            for token in tokensEnLinea:
                tokens.append(token)
        return tokens

    def contarTokens(self):
        resultados = {
            "contInt": 0,
            "contFloat": 0,
            "contBoolean": 0,
            "contChar": 0,
            "contString": 0,
        }

        tokens = self.obtenerTokens()

        for token in tokens:
            if(self.esInt(token)):
                resultados["contInt"] += 1
            elif(self.esFloat(token)):
                resultados["contFloat"] += 1
            elif(self.esBoolean(token)):
                resultados["contBoolean"] += 1
            elif(self.esChar(token)):
                resultados["contChar"] += 1              
            elif(self.esString(token)):
                resultados["contString"] += 1

        self.mostrarResultados(resultados)

    def mostrarResultados(self, resultados):
        self.total_int.setText(str(resultados["contInt"]))
        self.total_float.setText(str(resultados["contFloat"]))
        self.total_boolean.setText(str(resultados["contBoolean"]))
        self.total_chars.setText(str(resultados["contChar"]))
        self.total_strings.setText(str(resultados["contString"]))

    def cierraAplicacion(self):
        msgbox = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Question, "Salir de aplicación", "Estás seguro de salir de la aplicación?")
        msgbox.addButton(QtWidgets.QMessageBox.Yes)
        msgbox.addButton(QtWidgets.QMessageBox.No)
        msgbox.setDefaultButton(QtWidgets.QMessageBox.No)

        msgbox.setWindowIcon(QtGui.QIcon(
            self.scriptDir + os.path.sep + 'warning.png'))
        reply = msgbox.exec()

        if(reply == QtWidgets.QMessageBox.Yes):
            sys.exit()
        else:
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())


main()