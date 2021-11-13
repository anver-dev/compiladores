import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ventana(QtWidgets.QMainWindow):

    def __init__(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        
        super(Ventana, self).__init__()

        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Contador de tokens")
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + "icon.png"))


        self.openFile = QtWidgets.QAction(QtGui.QIcon(
            scriptDir + os.path.sep + 'open.png'), '&Abrir Archivo', self)
        self.openFile.setShortcut("Ctrl+O")
        self.openFile.setStatusTip("Abrir Archivo")
        self.openFile.triggered.connect(self.abrir_archivo)

        EventoSalir = QtWidgets.QAction(QtGui.QIcon(
            scriptDir + os.path.sep + 'salir.png'), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        # Agrega un tooltip
        EventoSalir.setStatusTip("Salir de la aplicaión")
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        MenuPrincipal = self.menuBar()

        MenuArchivo = MenuPrincipal.addMenu("&Archivo")
        MenuArchivo.addAction(self.openFile)
        MenuArchivo.addSeparator()
        MenuArchivo.addAction(EventoSalir)

        self.home()

    def home(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        
        self.bandera_abrir = False
        self.Resultados = QtWidgets.QTextEdit(self)

        EventoAbrirLocal = QtWidgets.QAction(
            QtGui.QIcon(
            scriptDir + os.path.sep + 'open.png'), 'Abrir un Archivo', self)
        EventoAbrirLocal.triggered.connect(self.abrir_archivo)

        self.BarraOpciones = self.addToolBar("Archivo")
        self.BarraOpciones.addAction(EventoAbrirLocal)
        

        self.EventoSalirLocal = QtWidgets.QAction(
            QtGui.QIcon(
            scriptDir + os.path.sep + 'exit.png'), 'Salir del programa', self)
        self.EventoSalirLocal.triggered.connect(self.cierra_aplicacion)

        self.BarraOpciones.addAction(self.EventoSalirLocal)

        self.Resultados.resize(500, 420)
        self.Resultados.move(10, 65)

        self.show()

    def abrir_archivo(self):
        vOpenFileName = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open File", filter="*.txt")[0]

        if(vOpenFileName == ""):
            return

        f = open(vOpenFileName, "r")
        vTextString = f.read()
        self.Resultados.setText(vTextString)

        f.close()
        self.bandera_abrir = True

    def cierra_aplicacion(self):
        opcion = QtWidgets.QMessageBox.question(
            self, "Salir de la Aplicación", "Estas seguro de salir?", QtWidgets.QMessageBox.question.Yes | QtWidgets.QMessageBox.question.No)

        if(opcion == QtWidgets.QMessageBox.question.Yes):
            sys.exit()
        else:
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())


main()
