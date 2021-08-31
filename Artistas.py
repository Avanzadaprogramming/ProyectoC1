from Personas import Persona
import random
class Artista (Persona):
    def __init__(self,Automatico,Genero="None",ID=0):
        if Automatico == True:
                
            Persona.__init__(self,Automatico, Genero)

            ##Nom Artistico
            baseNomArt = open("ArchivosTxT/NomArtisticos.txt","r")
            NomArt= baseNomArt.readline().strip().split(",")

            ##Generos
            lista = open("ArchivosTxT/Generos.txt","r")
            Generos = []
            while True:
                lectura = lista.readline().strip()
                if lectura=="*":
                    break
                Generos.append(lectura)

            self.id = ID
            self.nomArtistico = NomArt[random.randint(0,len(NomArt)-1)]
            self.genero= Generos[random.randint(0,len(Generos)-1)]
            self.cobro = random.randint(0,10000)

        else:

            print("---Ingrese la siguiente informacion del Artista---")
            Persona.__init__(self,Automatico, Genero)

            self.id= ID
            self.nomArtistico = input("Ingrese el Nombre Artistico: ")
            self.genero= input("Ingrese el genero del artista: ")
            self.cobro = input("Ingrese el cobro del artista")


    def __str__(self):
        return (f"------------Artista #{self.id}------------\nID: {self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\
\nDireccion: {self.getDireccion()}\nNombre Artistico: {self.nomArtistico}\nGenero: {self.genero}\nCobro: {self.cobro}")

##pepe= Artista(False,"f",0)
##print (pepe)