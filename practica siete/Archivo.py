class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta

    def abrir(self):
        if self.ruta:
            archivo = open(self.ruta, "r")
            self.contenido = archivo.read()

            listaSplit = str(self.ruta).split("/")
            self.nombreArchivo = listaSplit[len(listaSplit) - 1]

            archivo.close()
            return {"contenido": self.contenido, "nombre": self.nombreArchivo}

    def obtenerReglasDeProduccion(self, contenidoArchivo):
        numerosYReglasDeProduccion = contenidoArchivo.toPlainText().split("\n")
        print(numerosYReglasDeProduccion)

        self.reglasDeProduccion = []
        i = 0
        for linea in numerosYReglasDeProduccion:
            reglaDeProduccionTexto = linea.split(".")[1]  # obtenemos la regla
            reglaDeProduccion = reglaDeProduccionTexto.split("->")
            self.reglasDeProduccion.append(
                {"terminal": reglaDeProduccion[0], "valor": reglaDeProduccion[1]}
            )
        print(self.reglasDeProduccion)
        return reglaDeProduccion