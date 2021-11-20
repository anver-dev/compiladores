'''
    Creado el 16/11/2021
    @author: Ana Karina Vergara Guzmán
    @description: Modelando un automata (FND)
'''
import sys


class AutomataFD:
    def estadoCero(self, cadena, cont):
        if cont < len(cadena) and cadena[cont] == "1":
            cont += 1
            return self.estadoCero(cadena, cont)
        elif cont < len(cadena) and cadena[cont] == "0":
            cont += 1
            return self.estadoUno(cadena, cont)
        else:
            False

    def estadoUno(self, cadena, cont):
        if cont < len(cadena) and cadena[cont] == "1":
            cont += 1
            return self.estadoCero(cadena, cont)
        elif cont < len(cadena) and cadena[cont] == "0":
            cont += 1
            return self.estadoDos(cadena, cont)
        else:
            False

    def estadoDos(self, cadena, cont):
        if cont < len(cadena) and cadena[cont] == "1":
            cont += 1
            return self.estadoDos(cadena, cont)
        elif cont < len(cadena) and cadena[cont] == "0":
            cont += 1
            return self.estadoCero(cadena, cont)
        elif cont == len(cadena):
            return True
        else:
            return False
