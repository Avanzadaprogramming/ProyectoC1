from Personas import Persona
from io import open
import random
class Empleado(Persona):
    def __init__(self,Automatico,Genero="None",IdEmpleado=0):
        if Automatico == True:
            Persona.__init__(self,Automatico,Genero)
            #BaseUniversidad
            baseUnis = open("ArchivosTxT/Universidades.txt","r")
            Unis = baseUnis.readline().strip().split(",")

            self.id = IdEmpleado
            self.universidad = Unis[random.randint(0,len(Unis)-1)]
            self.salario= random.randint(877802,5000000)

            if self.salario> 1500000:
                tipo = "Directivo"
            else:
                tipo = "Raso"
            self.salario = str(self.salario)
            self.tipo = tipo.lower()
            self.ocupado = "Disponible"

        else:
            print("---Ingrese la siguiente informacion del Empleado---")
            Persona.__init__(self,Automatico, Genero="None")
            self.id = IdEmpleado
            self.universidad = input("Nombre Universidad: ")
            self.salario = input("Ingrese salario: ")
            while True:
                self.tipo = (input("Ingrese Directivo o Raso: ")).lower()
                if (self.tipo == "directivo") or (self.tipo == "raso"):
                    break
                else:
                    print("---Tipo invalido intentelo de nuevo---")
            self.ocupado = "Disponible"

            
    def __str__(self):
        return (f"----Empleado #{self.id}----\nID: {self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\
\nDireccion: {self.direccion}\nEgresado De {self.universidad}\nEs un Empleado: {self.tipo}\nSalario: {self.salario}\
\nActualmente se encuentra: {self.ocupado}")
        
#juanito= Empleado(False,"f",0)
#print(juanito)