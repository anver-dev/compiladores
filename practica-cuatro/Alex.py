'''
Creado el: 01/12/2021
@author: Ana Karina Vergara Guzmán
@desciption: clase encargada de la lógica del Analizador Lexicografico.

'''
from PalabrasReservadas import PalabrasReservadas


class Alex:
    SUMA = "+"
    PRODUCTO = "*"
    HECHO = "\0"
    VACIO = " "
    DIGITO = "d"

    def __init__(self, txtContenidoAF):
        self.contenidoDelArchivo = (txtContenidoAF.toPlainText()).split(
            "\n")  # arreglo de lineas del AF
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

        if self.valida_digito(lexema):
            return self.es_digito(lexema)
        elif lexema == self.SUMA:
            return self.es_suma_o_incremento(lexema)
        elif lexema == self.PRODUCTO:
            return self.es_producto(lexema)
        elif lexema == self.VACIO:
            return self.vacio(lexema)
        elif lexema == self.HECHO:
            return self.hecho(lexema)
        else:
            return self.error(lexema)

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

    def es_digito(self, lexema):
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

    def es_suma_o_incremento(self, lexema):
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

    def es_producto(self, lexema):
        return {
            "token": self.objPR.palabrasReservadas["PRODUCTO"],
            "lexema": lexema
        }

    def hecho(self, lexema):
        return {
            "token": self.objPR.palabrasReservadas["HECHO"],
            "lexema": lexema
        }

    def vacio(self, lexema):
        return{
            "token": "VACIO",
            "lexema": lexema
        }

    def error(self, lexema):
        return {
            "token": self.objPR.palabrasReservadas["ERROR"],
            "lexema": lexema
        }

    def valida_digito(self, cadena):
        try:
            int(cadena)
            return True
        except ValueError:
            return False
