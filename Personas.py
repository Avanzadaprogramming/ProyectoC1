from  io import open
import random

class Persona :
    def __init__(self,Automatico,Genero="None" ):
        ## Generacion Automatica de personas
        if Automatico == True :
            
            if Genero.lower() == "m":
                baseNom = open("ArchivosTxT/NomPersonasM.txt","r")

            elif Genero.lower() == "f" :
                baseNom = open("ArchivosTxT/NomPersonasF.txt","r")

            else:
                a = random.randint(1,2)
                if a == 1 :
                    baseNom = open("ArchivosTxT/NomPersonasM.txt","r")
                else:
                    baseNom = open("ArchivosTxT/NomPersonasF.txt","r")

            #Lista de nombres
            ListaNombres = baseNom.readline().strip().split()
            baseNom.close()

            #Lista apellidos
            baseApe = open("ArchivosTxT/ApellidosPersonas.txt","r")
            ListaApellido = baseApe.readline().strip().split(",")
            baseApe.close()

            #Datos
            self.nombre = ListaNombres[random.randint(0,len(ListaNombres)-1)]
            self.apellido = ListaApellido[random.randint(0,len(ListaApellido)-1)]
            self.numero = str(random.randint(1000000000,9999999999))
            self.direccion = str((f"Calle {random.randint(1,300)} #{random.randint(1,300)}-{random.randint(1,100)}"))

        else:
            
            self.nombre= input("Nombre: ")
            self.apellido = input("Apellido: ")
            self.numero = input("Numero: ")
            self.direccion = input("Direccion: ")

    def __str__(self):
        return(f"----Persona----\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\nDireccion: {self.direccion}\n--------------------------------")

    def getNombre(self):
        return self.nombre

    def getApellido (self):
        return self.apellido
    
    def getNumero(self):
        return self.numero
    
    def getDireccion (self):
        return self.direccion

"""juana = Persona(True)
print(juana)"""
