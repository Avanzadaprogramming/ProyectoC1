class Desfile:
    def __init__(self,iD,nombre,fecha,hora,pabellon,disenador,modelos,artista):
        self.id = iD
        self.nombre = nombre
        self.fecha= fecha
        self.hora= hora
        self.pabellon = pabellon
        self.disenador = disenador
        self.modelos = modelos

    def __str__(self):
        return f"------------Desfile #{self.id}------------\nNombre: {self.nombre}\nFecha: {self.fecha}\nHora: {self.hora}\
\nPabellon: #{self.pabellon.id}\nCarnet Diseñador: {self.disenador.id}\nNombre Diseñador: {self.disenador.nombre} {self.disenador.apellido}\
\nNumero de Modelos: {len(self.modelos)-1}"

    def verModelos(self):
        for i in self.modelos:
            print(i)