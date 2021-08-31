from Personas import Persona
from io import open
import random
class Empleado(Persona):
    def __init__(self,Automatico,Genero="None",IdEmpleado=0):

            print("---Ingrese la siguiente informacion del Empleado---") ##CAMBIO 2021
            Persona.__init__(self,Automatico, Genero="None")
            ##Pedir en el main todos los datos de la persona y enviarlos aqui tambien
            self.id = IdEmpleado
            
            self.salario = input("Ingrese salario: ")
            while True:
                self.tipo = (input("Ingrese Directivo o Raso: ")).lower()
                if (self.tipo == "directivo") or (self.tipo == "raso"):
                    break
                else:
                    print("---Tipo invalido intentelo de nuevo---")
            self.ocupado = "Disponible"
            if self.tipo == "directivo":
                self.universidad = input("Nombre Universidad: ")
            else:
                self.univeri = "No Aplica"

            
    def __str__(self):
        return (f"----Empleado #{self.id}----\nID: {self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\
\nDireccion: {self.direccion}\nEgresado De {self.universidad}\nEs un Empleado: {self.tipo}\nSalario: {self.salario}\
\nActualmente se encuentra: {self.ocupado}")
        
#juanito= Empleado(False,"f",0)
#print(juanito)