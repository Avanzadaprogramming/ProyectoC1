from io import open
import random
class Agencia:
    def __init__(self,Automatico,iD):
        if Automatico == True:
            ## Nombre y apellido
            baseNom = open("ArchivosTxT/NomPersonasF.txt","r")
            ListaNombres = baseNom.readline().strip().split()
            baseNom.close()
            baseApe = open("ArchivosTxT/ApellidosPersonas.txt","r")
            ListaApellido = baseApe.readline().strip().split(",")
            baseApe.close()

            #Paises 
            lista = open("ArchivosTxT/basePais.txt","r")
            paises = []
            while True:
                lectura = lista.readline().strip().lower()
                if lectura=="*":
                    break
                paises.append(lectura)

            self.id = iD
            self.pais = paises[random.randint(0,len(paises)-1)]
            self.anoCreacion = str(random.randint(1850,2020))
            self.correo = str(f"Agencia{str(self.id)}{self.pais}@agencias.com")
            self.dueno= str(f"{ListaNombres[random.randint(0,len(ListaNombres)-1)]} {ListaApellido[random.randint(0,len(ListaApellido)-1)]}")

        else:
            print("---Para Generar Agencia Ingrese los siguientes datos---")
            self.id = iD
            self.pais = input("Ingrese el pais de origen: ")
            self.anoCreacion = input("Ingrese el año de creacion: ")
            self.correo = ("Ingrese el correo de la agencia: ")
            self.dueno= ("Ingrese el nombre del dueño: ")

    def __str__(self):
        return(f"----Agencia #{self.id}----\nID: {self.id}\nNombre de la Agencia: {self.pais}\nAño Creacion: {self.anoCreacion}\nCorreo: {self.correo}\
\nDueño: {self.dueno}")

#agencia1= Agencia(True,54)
#print(agencia1)

            
