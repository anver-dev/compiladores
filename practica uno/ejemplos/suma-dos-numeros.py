'''
    @author: Anver
    @description: Sumar dos enteros
'''

def main():
    a = 20
    b = 30

    c = suma(a, b)
    print(c)

    a = "Hola mundo: en Python"
    print(a)

def suma(par1, par2):
    resultado = par1 + par2
    return resultado

main()