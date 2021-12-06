'''
Creado el: 01/12/2021
@author: Ana Karina Vergara Guzmán
@desciption: clase encargada del manejo de archivo fuente asi como invocacion
             del Analizador Lexicografico.
'''
from Alex import Alex
from PalabrasReservadas import PalabrasReservadas


class Uami(object):

    def __init__(self):
        self.pathArchivoTupla = ""
        self.pathArchivoError = ""
        self.archivoTupla = ""
        self.archivoError = ""
        self.contadorLineas = 0

    def crear_archivos(self, pathArchivo):
        self.pathArchivoTupla = pathArchivo.replace(".fte", ".tpl")
        self.pathArchivoError = pathArchivo.replace(".fte", ".err")

        msgTupla = [
            "En este archivo se encuentran los lexemas reconocidos por el analizador lexicografico\n",
            "\n"
        ]

        msgError = [
            "* Archivo Error *\n",
            "En esta etapa del desarrollo del compilador este archivo solo contiene una copia del archivo fuente",
            "\n\n"
        ]

        self.archivoTupla = open(self.pathArchivoTupla, "w+")
        self.archivoTupla.writelines(msgTupla)

        self.archivoError = open(self.pathArchivoError, "w+")
        self.archivoError.writelines(msgError)

        self.cierra_archivos()

    def cierra_archivos(self):
        self.archivoTupla.close()
        self.archivoError.close()

    def inicia_compilacion(self, pathArchivo, Contenido_Area):
        objAlex = Alex(Contenido_Area)
        objPR = PalabrasReservadas()

        self.crear_archivos(pathArchivo)

        self.archivoTupla = open(self.pathArchivoTupla, "a")
        self.archivoError = open(self.pathArchivoError, "a")

        self.archivoTupla.write("\n")
        headerTabla = [
            "LINEA",
            "\t\t",
            "TOKEN",
            "\t\t",
            "LEXEMA",
            "\n"
        ]
        self.archivoTupla.writelines(headerTabla)
        self.archivoTupla.write("===================================================\n")

        self.archivoError.writelines(
            (Contenido_Area.toPlainText()).split("\n"))

        diccionario = objAlex.a_lexico(self)

        while diccionario["token"] != objPR.palabrasReservadas["HECHO"] and diccionario["token"] != objPR.palabrasReservadas["ERROR"]:
            if diccionario["token"] == "VACIO":
                pass

            else:
                texto = [
                    str(self.contadorLineas),
                    "\t\t",
                    diccionario["token"],
                    "\t\t",
                    diccionario["lexema"],
                    "\n"
                ]
                self.archivoTupla.writelines(texto)

            diccionario = objAlex.a_lexico(self)

        if diccionario["token"] == objPR.palabrasReservadas["ERROR"]:
            texto = [
                "--------------------------------------------------------------------------------------------------------\n",
                "--------------------------------- ERROR: Caracter no permitido ---------------------------------",
                "\n"
            ]
            self.archivoTupla.writelines(texto)

        elif diccionario["token"] == objPR.palabrasReservadas["HECHO"]:
            self.archivoTupla.write("-------------------------------------------------------------------------------------------------------\n")
            texto = [
                str(self.contadorLineas),
                "\t\t",
                diccionario["token"],
                "\t\t",
                diccionario["lexema"],
                "\n"
            ]
            self.archivoTupla.writelines(texto)

        self.cierra_archivos()
