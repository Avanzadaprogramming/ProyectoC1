from  io import open
from os import DirEntry
import random

class Persona :
    def __init__(self,cedula,nombre,apellido,numero,direccion ):    
        self.cedula = cedula
        self.nombre= nombre
        self.apellido = apellido
        self.numero = numero
        self.direccion = direccion
        ##importar los datos desde 

        
    def __str__(self):
        return(f"----Persona----\nNombre: {self.nombre}\nCedula: {self.cedula}\nApellido: {self.apellido}\nNumero: {self.numero}\nDireccion: {self.direccion}\n--------------------------------")

    def getNombre(self):
        return self.nombre

    def getApellido (self):
        return self.apellido
    
    def getNumero(self):
        return self.numero
    
    def getDireccion (self):
        return self.direccion

#juana = Persona("asdf","asdf","564654","asdfad")
#print(juana)

##