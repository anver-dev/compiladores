'''
Creado el: 01/12/2021
@author: Ana Karina Vergara Guzmán
@desciption: clase encargada del manejo de archivo fuente asi como invocacion
             del Analizador Lexicografico. 
'''


class PalabrasReservadas:

    def __init__(self) -> None:
        self.palabrasReservadas = {
            "NUM_ENT": "ENTERO",
            "SUMA": "SUMA",
            "PRODUCTO": "PRODUCTO",
            "INCREMENTO": "INCREMENTO",
            "ERROR": "Error de Compilación",
            "HECHO": "FINAL DEL ARCHIVO",
        }
