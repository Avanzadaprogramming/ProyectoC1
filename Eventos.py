class Evento: 
    def __init__(self,iD,FechaIni,FechaFin,Desfiles,Directivos,Rasos,PagoDirectivos,PagoRasos):
        self.id = iD
        self.fechaIni= FechaIni
        self.fechaFin= FechaFin
        self.desfiles= Desfiles
        self.directivos = Directivos
        self.rasos= Rasos
        self.pagoDirectivos= PagoDirectivos
        self.pagoRasos=PagoRasos
    def __str__(self):
        return f"------------Evento #{self.id}------------\nFecha Inicio: {self.fechaIni}\nFecha Fin: {self.fechaFin}\nNumero de desfiles: {len(self.desfiles)}\
\nNumero de Directivos: {len(self.directivos)}\nNumero de Rasos: {len(self.rasos)}\nPago Directivos: {self.pagoDirectivos} c/u\nPago Rasos {self.pagoRasos} c/u"