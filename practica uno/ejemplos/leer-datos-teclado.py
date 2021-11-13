'''
    Creado el 10/11/2021

    @author: Ana Karina Vergara Guzmán
    @description: Sumar dos enteros ingresador por un usuario
'''

def main():
    while True:
        try:
           a = int(input("Variable a: "))
           b = int(input("Variable b: "))
           break
        except:
            print("Ingresa variables de tipo entero")

    c = suma(a, b)
    print("La suma de a:", a, " y b:", b, " es:", c)

    a = "Hola mundo: en Python"
    print(a)

def suma(par1, par2):
    resultado = par1 + par2
    return resultado

main()