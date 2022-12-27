class Gramatica: 
    def __init__(self, reglasDeProduccion):
        self.reglasDeProduccion = reglasDeProduccion
    
    def derivarPorLaIzquierda(self, cadena):
        derivadaActual = self.reglasDeProduccion[0]['valor']
        
        longitudCadena = len(cadena)

        if(longitudCadena > len(derivadaActual)):
            i = 0
            while(i < longitudCadena):
                for reglaDeProduccion in self.reglasDeProduccion:
                    reglaDeProduccion['valor']
