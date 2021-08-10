from Personas import Persona
import random
class Disenador(Persona):
    def __init__(self,Automatico,Genero="m",Id=0):
        if Automatico == True:

            Persona.__init__(self,Automatico,Genero)
            

            #Paises
            lista = open("ArchivosTxT/basePais.txt","r")
            paises = []
            while True:
                lectura = lista.readline().strip().lower()
                if lectura=="*":
                    break
                paises.append(lectura)

            ##Asignaciones
            self.id = Id
            self.pasaporte = random.randint(1000000,9999999)                
            self.pais = paises[random.randint(0,len(paises)-1)]

        else:
            print("---Ingrese la siguiente informacion del Diseñador---")
            Persona.__init__(self,Automatico,Genero)

            self.id= Id
            self.pasaporte = input("Ingrese el Pasaporte: ")
            self.pais = input("Ingrese el Pais: ")

    def __str__(self):
        return (f"----------Diseñador #{self.id}----------\nID: {self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\
\nDireccion: {self.getDireccion()}\nPasaporte: {self.pasaporte}\nPais de Origen: {self.pais}")


##juanito = Disenador(False,"f",0)
##print(juanito)