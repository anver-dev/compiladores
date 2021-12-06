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
from UAMI import Uami


class Ventana(QMainWindow):
    scriptDir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep

    def __init__(self):

        super(Ventana, self).__init__()
        self.setGeometry(50, 30, 650, 700)
        self.setWindowTitle("ALEX")
        self.setWindowIcon(QIcon(
            self.scriptDir + "img/icon.png"))

        EventoAbrirArchivo = QAction(QIcon(
            self.scriptDir + 'img/open.png'), '&Abrir Archivo', self)
        EventoAbrirArchivo.setShortcut("Ctrl+O")
        EventoAbrirArchivo.setStatusTip("Abrir Archivo")
        EventoAbrirArchivo.triggered.connect(self.abrir_archivo)

        EventoSalir = QAction(QIcon(
            self.scriptDir + 'img/salir.png'), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip("Salir de la aplicación")
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        EventoCompilar = QAction(QIcon(
            self.scriptDir + 'img/compilar.png'), "Compilar", self)
        EventoCompilar.setShortcut("Ctrl+A")
        EventoCompilar.setStatusTip("Compilar aplicación")
        EventoCompilar.triggered.connect(self.compilar_aplicacion)

        MenuPrincipal = self.menuBar()

        MenuArchivo = MenuPrincipal.addMenu("&Archivo")
        MenuArchivo.addAction(EventoAbrirArchivo)
        MenuArchivo.addAction(EventoCompilar)
        MenuArchivo.addSeparator()
        MenuArchivo.addAction(EventoSalir)

        self.home()

    def home(self):
        self.Contenido_fuente_lbl = QLabel(self)
        self.Contenido_fuente_lbl.setText('CONTENIDO DEL \nARCHIVO FUENTE:')
        self.Contenido_fuente_lbl.setFont(QFont("Arial", 10, QFont.Black))
        self.Contenido_fuente_lbl.move(10, 70)
        self.Contenido_fuente_lbl.adjustSize()

        self.Contenido_area = QTextEdit(self)
        self.Contenido_area.resize(450, 250)
        self.Contenido_area.move(150, 70)
        #self.ContenidoArchivo = QTextEdit(self)

        self.Resultados_compilacion_lbl = QLabel(self)
        self.Resultados_compilacion_lbl.setText(
            'RESULTADOS DE \nLA COMPILACIÓN:')
        self.Resultados_compilacion_lbl.setFont(
            QFont("Arial", 10, QFont.Black))
        self.Resultados_compilacion_lbl.move(10, 350)
        self.Resultados_compilacion_lbl.adjustSize()

        self.Resultados_area = QTextEdit(self)
        self.Resultados_area.resize(450, 200)
        self.Resultados_area.move(150, 350)
        self.Resultados_area.setReadOnly(True)

        self.Lineas_lbl = QLabel(self)
        self.Lineas_lbl.setText(
            'LINEAS \nANALIZADAS:')
        self.Lineas_lbl.setFont(
            QFont("Arial", 10, QFont.Black))
        self.Lineas_lbl.move(10, 570)
        self.Lineas_lbl.adjustSize()

        self.Lineas_input = QLineEdit(self)
        self.Lineas_input.resize(50, 25)
        self.Lineas_input.move(150, 570)
        self.Lineas_input.setReadOnly(True)

        self.EventoAbrirLocal = QAction(
            QIcon(
                self.scriptDir + 'img/open.png'), 'Abrir un Archivo', self)
        self.EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        self.EventoCompilar = QAction(
            QIcon(
                self.scriptDir + 'img/compilar.png'), 'Compilar aplicación', self)
        self.EventoCompilar.triggered.connect(self.compilar_aplicacion)

        self.EventoSalirLocal = QAction(
            QIcon(
                self.scriptDir + 'img/exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierra_aplicacion)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(self.EventoAbrirLocal)
        self.BarraOpciones.addAction(self.EventoSalirLocal)
        self.BarraOpciones.addSeparator()
        self.BarraOpciones.addAction(self.EventoCompilar)

        self.show()

    def compilar_aplicacion(self):
        objUAMI = Uami()
        objUAMI.inicia_compilacion(self.pathArchivo, self.Contenido_area)

        self.mostrar_resultados(objUAMI)
        

    def abrir_archivo(self):
        self.pathArchivo = QFileDialog.getOpenFileName(
            self, "Open File", filter="*.fte")[0]

        if(self.pathArchivo):
            self.archivo = open(self.pathArchivo, "r")
            self.Contenido_area.setText(self.archivo.read())
            self.archivo.close()

    def mostrar_resultados(self, objUAMI):
        archivoTupla = open(objUAMI.pathArchivoTupla, "r")
        contenidoTupla = archivoTupla.read()

        objUAMI.cierra_archivos()
        self.Resultados_area.setText(contenidoTupla)
        self.Lineas_input.setText(str(objUAMI.contadorLineas))
    def cierra_aplicacion(self):
        msgbox = QMessageBox(
            QMessageBox.Question, "Salir de aplicación", "Estás seguro de salir de la aplicación?")
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)

        msgbox.setWindowIcon(QIcon(
            self.scriptDir + 'img/warning.png'))
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
