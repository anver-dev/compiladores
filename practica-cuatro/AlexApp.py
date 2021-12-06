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
    pathArchivo = ""

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
        #
        self.lblNombreArchivo = QLabel(self)
        self.lblNombreArchivo.setText('Nombre archivo:')
        self.lblNombreArchivo.setFont(QFont("Arial", 10, QFont.Black))
        self.lblNombreArchivo.move(10, 70)
        self.lblNombreArchivo.adjustSize()

        self.inputNombreArchivo = QLineEdit(self)
        self.inputNombreArchivo.resize(450, 25)
        self.inputNombreArchivo.move(150, 70)
        self.inputNombreArchivo.setReadOnly(True)

        self.lblContenidoAF = QLabel(self)
        self.lblContenidoAF.setText('Contenido del \narchivo fuente:')
        self.lblContenidoAF.setFont(QFont("Arial", 10, QFont.Black))
        self.lblContenidoAF.move(10, 100)
        self.lblContenidoAF.adjustSize()

        self.txtContenidoAF = QTextEdit(self)
        self.txtContenidoAF.resize(450, 250)
        self.txtContenidoAF.move(150, 110)
        self.txtContenidoAF.setReadOnly(True)

        self.lblResultadosCompilacion = QLabel(self)
        self.lblResultadosCompilacion.setText(
            'Resultados de \nla compilación:')
        self.lblResultadosCompilacion.setFont(
            QFont("Arial", 10, QFont.Black))
        self.lblResultadosCompilacion.move(10, 390)
        self.lblResultadosCompilacion.adjustSize()

        self.txtResultadosCompilacion = QTextEdit(self)
        self.txtResultadosCompilacion.resize(450, 200)
        self.txtResultadosCompilacion.move(150, 390)
        self.txtResultadosCompilacion.setReadOnly(True)

        self.lblLineasAnalizadas = QLabel(self)
        self.lblLineasAnalizadas.setText(
            'Lineas analizadas:')
        self.lblLineasAnalizadas.setFont(
            QFont("Arial", 10, QFont.Black))
        self.lblLineasAnalizadas.move(10, 610)
        self.lblLineasAnalizadas.adjustSize()

        self.inputLineasAnalizadas = QLineEdit(self)
        self.inputLineasAnalizadas.resize(50, 25)
        self.inputLineasAnalizadas.move(150, 610)
        self.inputLineasAnalizadas.setReadOnly(True)

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

        if self.pathArchivo != "":
            objUAMI.inicia_compilacion(self.pathArchivo, self.txtContenidoAF)
            self.mostrar_resultados(objUAMI)
        else:
            self.mostrar_alerta_archivo()

    def abrir_archivo(self):
        self.pathArchivo = QFileDialog.getOpenFileName(
            self, "Open File", filter="*.fte")[0]

        if(self.pathArchivo):
            self.archivo = open(self.pathArchivo, "r")
            self.txtContenidoAF.setText(self.archivo.read())

            listaSplit = str(self.pathArchivo).split("/")
            nombreArchivo = listaSplit[len(listaSplit) - 1]
            
            self.inputNombreArchivo.setText(str(nombreArchivo))
            self.archivo.close()

    def mostrar_resultados(self, objUAMI):
        archivoTupla = open(objUAMI.pathArchivoTupla, "r")
        contenidoTupla = archivoTupla.read()

        objUAMI.cierra_archivos()
        self.txtResultadosCompilacion.setText(contenidoTupla)
        self.inputLineasAnalizadas.setText(str(objUAMI.contadorLineas))

        if objUAMI.banderaError:
            self.txtResultadosCompilacion.setStyleSheet("border: 2px solid red;")
        else:
            self.txtResultadosCompilacion.setStyleSheet("border: 2px solid green;")

    def mostrar_alerta_archivo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ningún archivo para compilar")
        msg.setInformativeText(
            'Favor de seleccionar un archivo, seleccionando el icono o con Ctr+O')
        msg.setWindowTitle("Selecciona un archivo")
        msg.setWindowIcon(QIcon(
            self.scriptDir + os.path.sep + 'img/warning.png'))
        msg.exec_()

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
