from Artistas import Artista
from Artistas import Artista
import random
class Banda (Artista):
    def __init__(self,Automatico,Genero="None",ID=0):
        if Automatico == True:
            integrantes = []
            for i in range(4):
                Artista.__init__(self,Automatico, Genero)
                integrantes.append(Artista.__init__(self,Automatico, Genero))

            ##Nom Banda
            baseNomBan = open("ArchivosTxT/NomBandas.txt","r")
            NomBan= baseNomBan.readline().strip().split(",")

            ##Generos
            lista = open("ArchivosTxT/Generos.txt","r")
            Generos = []
            while True:
                lectura = lista.readline().strip()
                if lectura=="*":
                    break
                Generos.append(lectura)

            self.id = ID
            self.nomBanda = NomBan[random.randint(0,len(NomBan)-1)]
            self.integrantes= integrantes
            self.genero= Generos[random.randint(0,len(Generos)-1)]
            self.cobro = random.randint(0,10000)
            self.creacion = str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(1990,2021))

        else:
            integrantes = []
            cantInte = int(input("Ingrese la cantidad de integrantes en numero: "))
            print("---Ingrese la siguiente informacion del Artista---")
            for i in range(cantInte):
                Artista.__init__(self,Automatico, Genero)
                integrantes.append(Artista.__init__(self,Automatico, Genero))
            
            self.id= ID
            self.nomBanda = input("Ingrese el Nombre de la banda: ")
            self.integrantes = integrantes
            self.genero= input("Ingrese el genero de la banda: ")
            self.cobro = input("Ingrese el cobro de la banda: ")
            self.creacion = input("Ingrese la fecha de creacion")

def __str__(self):
        return (f"------------Banda #{self.id}------------\nID: {self.id}\nNombre: {self.baseNomBa}\nFecha Creacion: {self.creacion}\nIntegrantes: {self.integrantes}\nGenero: {self.genero}\
\nCosto: {self.cobro}")
