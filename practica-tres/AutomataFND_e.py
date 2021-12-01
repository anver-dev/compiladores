class AutomataFND_e(object):

    def __init__( self ):
      self.CaminosEncontrados = []

    def estadoCero( self, cadena ):

      mensaje = ""
      
      resultado = self.estadoUno( cadena, 0, ["( e, Q1 )|"] )
      boleano = resultado[0]

      if boleano == True:
        mensaje = "Valida: La cadena es un impar de ceros"
        return mensaje

      else:
        resultado = self.estadoTres( cadena, 0, ["( e, Q3 )|"] )
        boleano = resultado[0]

        if boleano == True:
          mensaje = "Valida: La cadena NO es multiplo de 3"
          return mensaje

        else:
          mensaje = "CADENA NO ACEPTADA"
          return mensaje

    
    def estadoUno( self, cadena, contador, caminoActual ):

        if len(cadena) == contador:
          caminoActual.append("Camino invalido")
          self.CaminosEncontrados.append(caminoActual)
          return False, caminoActual

        elif cadena[ contador ] == "0":
          caminoActual.append("( 0, Q2 )|")
          contador = contador + 1
          return self.estadoDos( cadena, contador, caminoActual )

        elif cadena[ contador ] == "1":
          caminoActual.append("( 1, Q1 )|")
          contador = contador + 1
          return self.estadoUno( cadena, contador, caminoActual )

    def estadoDos( self, cadena, contador, caminoActual ):

        if len(cadena) == contador:
          caminoActual.append("Camino valido")
          self.CaminosEncontrados.append(caminoActual)
          return True, caminoActual
        
        elif cadena[ contador ] == "0":
          caminoActual.append("( 0, Q1 )|")
          contador = contador + 1
          return self.estadoUno( cadena, contador, caminoActual )

        elif cadena[ contador ] == "1":
          caminoActual.append("( 1, Q2 )")
          contador = contador + 1
          return  self.estadoDos( cadena, contador, caminoActual )

    
    def estadoTres( self, cadena, contador, caminoActual ):

        if len(cadena) == contador:
          caminoActual.append("Camino invalido")
          self.CaminosEncontrados.append(caminoActual)
          return False, caminoActual

        elif cadena[ contador ] == "0":
          caminoActual.append("( 0, Q3 )|")
          contador = contador + 1
          return self.estadoTres( cadena, contador, caminoActual )

        elif cadena[ contador ] == "1":
          caminoActual.append("( 1, Q4 )|")
          contador = contador + 1
          return self.estadoCuatro( cadena, contador, caminoActual )

    def estadoCuatro( self, cadena, contador, caminoActual ):

        if len(cadena) == contador:
          caminoActual.append("Camino valido")
          self.CaminosEncontrados.append(caminoActual)
          return True, caminoActual

        elif cadena[ contador ] == "0":
          caminoActual.append("( 0, Q4 )|")
          contador = contador + 1
          return self.estadoCuatro( cadena, contador, caminoActual )

        elif cadena[ contador ] == "1":
          caminoActual.append("( 1, Q5 )|")
          contador = contador + 1
          return self.estadoCinco( cadena, contador, caminoActual )

    def estadoCinco( self, cadena, contador, caminoActual ):

        if len(cadena) == contador:
          caminoActual.append("Camino valido")
          self.CaminosEncontrados.append(caminoActual)
          return True, caminoActual

        elif cadena[ contador ] == "0":
          caminoActual.append("( 0, Q5 )|")
          contador = contador + 1
          return self.estadoCinco( cadena, contador, caminoActual )

        elif cadena[ contador ] == "1":
          caminoActual.append("( 1, Q3 )|")
          contador = contador + 1
          return self.estadoTres( cadena, contador, caminoActual )