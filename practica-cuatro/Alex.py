'''
Creado el: 01/12/2021
@author: Ana Karina Vergara Guzmán
@desciption: clase encargada del manejo de archivo fuente asi como invocacion
             del Analizador Lexicografico.
'''

from PalabrasReservadas import PalabrasReservadas


class Alex:
    SUMA = "+"
    PRODUCTO = "*"
    HECHO = "\0"
    VACIO = " "

    def __init__(self, Contenido_Area):
        self.contenidoDelArchivo = (Contenido_Area.toPlainText()).split("\n")
        self.objPR = PalabrasReservadas()
        self.contador = 0
        self.Buffer = {
            "pos_leida": 0,
            "tamaño": 0,
            "cadena": ""
        }

    def a_lexico(self, objUAMI):
        lexema = self.leer_caracter()
        objUAMI.contadorLineas = self.contador

        if lexema == self.PRODUCTO:
            return {
                "token": self.objPR.palabrasReservadas["PRODUCTO"],
                "lexema": lexema
            }

        elif lexema == self.SUMA:
            lexema = lexema + self.leer_caracter()

            if lexema[1] == self.SUMA:
                return {
                    "token": self.objPR.palabrasReservadas["INCREMENTO"],
                    "lexema": lexema
                }

            else:
                self.desleer()
                return {
                    "token": self.objPR.palabrasReservadas["SUMA"],
                    "lexema": lexema[0]
                }

        elif self.valida_digito(lexema):
            digito = lexema

            while self.valida_digito(digito):
                digito = self.leer_caracter()
                lexema = lexema + digito

            lexema = lexema[:-1]
            self.desleer()
            return {
                "token": self.objPR.palabrasReservadas["NUM_ENT"],
                "lexema": lexema
            }

        elif lexema == self.HECHO:
            return {
                "token": self.objPR.palabrasReservadas["HECHO"],
                "lexema": lexema
            }

        elif lexema == self.VACIO:
            return{
                "token": "VACIO",
                "lexema": lexema
            }

        else:

            return {
                "token": self.objPR.palabrasReservadas["ERROR"],
                "lexema": lexema
            }

    def leer_caracter(self):
        if (self.Buffer["pos_leida"] == self.Buffer["tamaño"]):
            self.llena_buffer()
            self.contador += 1

        if self.Buffer["tamaño"] != 0:
            cadena = self.Buffer["cadena"][self.Buffer["pos_leida"]]
            self.Buffer["pos_leida"] += 1
            print("entro en tamaño, cadena: ",
                  self.Buffer["cadena"], " pos", self.Buffer["tamaño"])
            return cadena

        else:
            return "\0"

    def llena_buffer(self):
        if self.contador < len(self.contenidoDelArchivo[:]):
            Cadena = self.contenidoDelArchivo[self.contador] + " "
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = Cadena
            self.Buffer["tamaño"] = len(Cadena)
        else:
            self.Buffer["pos_leida"] = 0
            self.Buffer["cadena"] = "null"
            self.Buffer["tamaño"] = 0

    def desleer(self):
        self.Buffer["pos_leida"] = self.Buffer["pos_leida"] - 1

    def valida_digito(self, cadena):
        try:
            int(cadena)
            return True
        except ValueError:
            return False
