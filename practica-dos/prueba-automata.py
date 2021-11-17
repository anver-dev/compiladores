'''
    Creado el 16/11/2021
    @author: Ana Karina Vergara Guzmán
    @description: Modelando un automata (FND)
'''
import sys


def estadoCero(cadena, cont):
    if cont < len(cadena) and cadena[cont] == "1":
        cont += 1
        return estadoCero(cadena, cont)
    elif cont < len(cadena) and cadena[cont] == "0":
        cont += 1
        return estadoUno(cadena, cont)
    else:
        False


def estadoUno(cadena, cont):
    if cont < len(cadena) and cadena[cont] == "1":
        cont += 1
        return estadoCero(cadena, cont)
    elif cont < len(cadena) and cadena[cont] == "0":
        cont += 1
        return estadoDos(cadena, cont)
    else:
        False


def estadoDos(cadena, cont):
    if cont < len(cadena) and cadena[cont] == "1":
        cont += 1
        return estadoDos(cadena, cont)
    elif cont < len(cadena) and cadena[cont] == "0":
        cont += 1
        return estadoCero(cadena, cont)
    elif cont == len(cadena):
        return True
    else:
        return False


def main():
    print("Automata")
    w = input("ingresa la cadena a reconocer:\n")

    cont = 0
    if estadoCero(w, cont):
        print("la cadena ", w, " es reconocida")
    else:
        print("la cadena ", w, " NO es reconocida")


main()
