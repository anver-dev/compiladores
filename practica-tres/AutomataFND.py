'''
    Creado el 28/11/2021
    @author: Ana Karina Vergara Guzmán
    @description: Modelando un automata (FND)
'''


class AutomataFND:

    def __init__(self):
        self.CaminosEncontrados = []

    def inicio(self, cadena):

        contador = 0
        caminoActual = []

        respuestaEstadoCero = self.estadoCeroACero(
            cadena, contador, caminoActual)

        contador = respuestaEstadoCero[1]
        caminoActual = respuestaEstadoCero[0][0:contador]
        print(caminoActual)

        while(len(caminoActual) > 0):

            if(caminoActual[contador - 1] == "(0,Q0)"):

                if(caminoActual[contador - 2] == "(0,Q0)"):
                    contador = contador - 1
                    caminoActual = caminoActual[0:contador]
                    self.estadoCeroAUno(cadena, contador, caminoActual)

                else:
                    contador = contador - 1
                    caminoActual = caminoActual[0:contador]

                    if(len(caminoActual) == 1 and caminoActual[0] == "(1,Q0)"):
                        self.estadoCeroAUno(cadena, contador, caminoActual)
            else:
                contador = contador - 1
                caminoActual = caminoActual[0:contador]

    def estadoCeroACero(self, cadena, contador, caminoActual):
        if len(cadena) == contador:
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return caminoActual, contador

        if cadena[contador] == "0":
            caminoActual.append("( 0, Q0 )|")
            contador = contador + 1
            return self.estadoCeroACero(cadena, contador, caminoActual)

        elif cadena[contador] == "1":
            caminoActual.append("( 1, Q0 )|")
            contador = contador + 1
            return self.estadoCeroACero(cadena, contador, caminoActual)


    def estadoCeroAUno(self, cadena, contador, caminoActual):
        if len(cadena) == contador:
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return False, caminoActual, contador

        if cadena[contador] == "1":
            caminoActual.append("( 1, Q0 )|")
            contador = contador + 1
            return self.estadoCeroACero(cadena, contador, caminoActual)

        elif cadena[contador] == "0":
            caminoActual.append("( 0, Q1 )|")
            contador = contador + 1
            return self.estadoUno(cadena, contador, caminoActual)


    def estadoUno(self, cadena, contador, caminoActual):

        if len(cadena) == contador:
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return False, caminoActual, contador

        elif cadena[contador] == "1":
            caminoActual.append("( 1, Q2 )|")
            contador = contador + 1
            self.estadoDos(cadena, contador, caminoActual)

        elif cadena[contador] == "0":
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return False

    def estadoDos(self, cadena, contador, caminoActual):

        if len(cadena) == contador:
            caminoActual.append("Camino Valido")
            self.CaminosEncontrados.append(caminoActual)
            return True, caminoActual, contador

        elif cadena[contador] == "1":
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return False

        elif cadena[contador] == "0":
            caminoActual.append("Camino Invalido")
            self.CaminosEncontrados.append(caminoActual)
            return False
