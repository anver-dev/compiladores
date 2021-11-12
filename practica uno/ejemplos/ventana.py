import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ventana(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ventana, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Ejemplo ventana")
        self.setWindowIcon(QtGui.QIcon("icon-comp.jpg"))

        scriptDir = os.path.dirname(os.path.realpath(__file__))

        EventoSalir = QtWidgets.QAction(QtGui.QIcon(scriptDir + os.path.sep + 'salir.png'), "Salir", self)
        EventoSalir.setShortcut("Ctrl+Q")
        # Agrega un tooltip
        EventoSalir.setStatusTip("Salir de la aplicaión")
        EventoSalir.triggered.connect(self.cierra_aplicacion)

        MenuPrincipal = self.menuBar()

        MenuArchivo = MenuPrincipal.addMenu("&Archivo")
        MenuArchivo.addAction(EventoSalir)

        self.home()
    
    def home(self):
        self.btn_Salir = QtWidgets.QPushButton("Salir", self)
        self.btn_Saludo = QtWidgets.QPushButton("Despliega Nombre", self)

        self.entrada_texto = QtWidgets.QLineEdit(self)
        self.salida_texto = QtWidgets.QLineEdit(self)
        self.solicita_lbl = QtWidgets.QLabel("Ingresa tu nombre:", self)
        self.resultado_lbl = QtWidgets.QLabel("Resultado:", self)

        self.entrada_texto.resize(200, 30)
        self.entrada_texto.move(200, 50)

        self.solicita_lbl.move(105, 50)

        self.resultado_lbl.move(145, 145)

        self.salida_texto.resize(200, 30)
        self.salida_texto.move(200, 150)

        self.btn_Salir.clicked.connect(self.cierra_aplicacion)
        self.btn_Saludo.clicked.connect(self.despliega)

        self.btn_Saludo.resize(100, 40)
        self.btn_Saludo.move(200, 100)

        self.btn_Salir.resize(100, 40)
        self.btn_Salir.move(200, 200)

        self.show()

    def despliega(self):
        mensaje = "Hola bienvenido a python Gráfico: " + self.entrada_texto.text()

        self.salida_texto.setText(mensaje)

    def cierra_aplicacion(self):
        sys.exit()
        
def main():
    app = QtWidgets.QApplication(sys.argv)

    GUI = Ventana()
    sys.exit(app.exec_())

main()