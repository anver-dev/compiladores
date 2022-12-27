"""
Creado el: 12/11/2021
@author: Ana Karina Vergara Guzmán
@desciption: Programa que permite realizar la reducción por la izquierda y
derecha para determinar si una gramática G2 es ambigua o no.

"""
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Archivo import *
from Gramatica import *


class Ventana(QMainWindow):
    scriptDir = os.path.dirname(os.path.realpath(__file__)) + os.path.sep
    ruta = ""

    def __init__(self):

        super(Ventana, self).__init__()
        self.setGeometry(600, 30, 650, 500)
        self.setWindowTitle("GRAMATICAS")
        self.setWindowIcon(QIcon(self.scriptDir + "img/icon.png"))

        EventoAbrirArchivo = QAction(
            QIcon(self.scriptDir + "img/open.png"), "&Abrir Archivo", self
        )
        EventoAbrirArchivo.setShortcut("Ctrl+O")
        EventoAbrirArchivo.setStatusTip("Abrir Archivo")
        EventoAbrirArchivo.triggered.connect(self.abrir_archivo)

        EventoSalir = QAction(QIcon(self.scriptDir + "img/salir.png"), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        EventoSalir.setStatusTip("Salir de la aplicación")
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        EventoCompilar = QAction(
            QIcon(self.scriptDir + "img/compilar.png"), "Dervivar", self
        )
        EventoCompilar.setShortcut("Ctrl+A")
        EventoCompilar.setStatusTip("Dervivar aplicación")
        EventoCompilar.triggered.connect(self.derivar)

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
        self.lblNombreArchivo.setText("Nombre archivo:")
        self.lblNombreArchivo.setFont(QFont("Arial", 9, QFont.Black))
        self.lblNombreArchivo.move(10, 70)
        self.lblNombreArchivo.adjustSize()

        self.inputNombreArchivo = QLineEdit(self)
        self.inputNombreArchivo.resize(400, 25)
        self.inputNombreArchivo.move(10, 90)
        self.inputNombreArchivo.setReadOnly(True)

        self.lblContenidoAF = QLabel(self)
        self.lblContenidoAF.setText("Reglas presentes en la gramática:")
        self.lblContenidoAF.setFont(QFont("Arial", 9, QFont.Black))
        self.lblContenidoAF.move(10, 130)
        self.lblContenidoAF.adjustSize()

        self.txtContenidoAF = QTextEdit(self)
        self.txtContenidoAF.resize(400, 150)
        self.txtContenidoAF.move(10, 150)

        self.lblResultadosDerivacion = QLabel(self)
        self.lblResultadosDerivacion.setText("Resultados de la derivación:")
        self.lblResultadosDerivacion.setFont(QFont("Arial", 9, QFont.Black))
        self.lblResultadosDerivacion.move(10, 310)
        self.lblResultadosDerivacion.adjustSize()

        self.txtResultadosCompilacion = QTextEdit(self)
        self.txtResultadosCompilacion.resize(400, 150)
        self.txtResultadosCompilacion.move(10, 330)
        self.txtResultadosCompilacion.setReadOnly(True)

        self.lblCadenaADerivar = QLabel(self)
        self.lblCadenaADerivar.setText("Cadena a derivar:")
        self.lblCadenaADerivar.setFont(QFont("Arial", 9, QFont.Black))
        self.lblCadenaADerivar.move(420, 150)
        self.lblCadenaADerivar.adjustSize()

        self.inputCadenaADerivar = QLineEdit(self)
        self.inputCadenaADerivar.resize(220, 25)
        self.inputCadenaADerivar.move(420, 170)

        self.lblSeleccion = QLabel(self)
        self.lblSeleccion.setText("Selecciona el tipo de \nderivación:")
        self.lblSeleccion.setFont(QFont("Arial", 9, QFont.Black))
        self.lblSeleccion.move(420, 205)

        self.rbtnDerivacionDerecha = QRadioButton(self)
        self.rbtnDerivacionDerecha.setText("Derecha")
        self.rbtnDerivacionDerecha.setFont(QFont("Arial", 9, QFont.Black))
        self.rbtnDerivacionDerecha.move(440, 245)

        self.rbtnDerivacionIzquierda = QRadioButton(self)
        self.rbtnDerivacionIzquierda.setText("Izquierda")
        self.rbtnDerivacionIzquierda.setFont(QFont("Arial", 9, QFont.Black))
        self.rbtnDerivacionIzquierda.move(440, 265)

        self.btnDerivar = QPushButton(self)
        self.btnDerivar.setText("Derivar")
        self.btnDerivar.setGeometry(420, 330, 220, 35)
        self.btnDerivar.clicked.connect(self.derivar)

        self.EventoAbrirLocal = QAction(
            QIcon(self.scriptDir + "img/open.png"), "Abrir un Archivo", self
        )
        self.EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        self.EventoCompilar = QAction(
            QIcon(self.scriptDir + "img/compilar.png"), "Derivar aplicación", self
        )
        self.EventoCompilar.triggered.connect(self.derivar)

        self.EventoSalirLocal = QAction(
            QIcon(self.scriptDir + "img/exit.png"), "Salir del programa", self
        )
        self.EventoSalirLocal.triggered.connect(self.cierra_aplicacion)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(self.EventoAbrirLocal)
        self.BarraOpciones.addAction(self.EventoSalirLocal)
        self.BarraOpciones.addSeparator()
        self.BarraOpciones.addAction(self.EventoCompilar)

        self.show()
    def validarCampos(self):
        if(self.txtContenidoAF.toPlainText() == ""):
            return False
        return True

    def selectionchange(self, i):
        print("Items in the list are :")

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

    def derivar(self):
        if(self.validarCampos()):
            reglasDeProduccion = self.objArchivo.obtenerReglasDeProduccion(self.txtContenidoAF)
            self.objGramatica = Gramatica(reglasDeProduccion)

    def abrir_archivo(self):
        self.ruta = QFileDialog.getOpenFileName(
            self, "Open File", filter="*.txt"
        )[0]
        self.objArchivo = Archivo(self.ruta)
        archivo = self.objArchivo.abrir()
        
        self.mostrar_datos_archivo(archivo)
    def mostrar_datos_archivo(self, archivo):
        self.inputNombreArchivo.setText(archivo['nombre'])
        self.txtContenidoAF.setText(archivo['contenido'])
        
    def mostrar_resultados(self, objUAMI):
        pass

    def mostrar_alerta_archivo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Ningún archivo para compilar")
        msg.setInformativeText(
            "Favor de seleccionar un archivo, seleccionando el icono o con Ctr+O"
        )
        msg.setWindowTitle("Selecciona un archivo")
        msg.setWindowIcon(QIcon(self.scriptDir + os.path.sep + "img/warning.png"))
        msg.exec_()

    def cierra_aplicacion(self):
        msgbox = QMessageBox(
            QMessageBox.Question,
            "Salir de aplicación",
            "Estás seguro de salir de la aplicación?",
        )
        msgbox.addButton(QMessageBox.Yes)
        msgbox.addButton(QMessageBox.No)
        msgbox.setDefaultButton(QMessageBox.No)

        msgbox.setWindowIcon(QIcon(self.scriptDir + "img/warning.png"))
        reply = msgbox.exec()

        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass


def main():
    app = QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())


main()
