from Personas import Persona
from Agencias import Agencia
import random
class Modelo(Persona):
    def __init__(self,Automatico,Genero="None",Id=0,IdAgencia=0,IdPortafolio=0):

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
            #Colores 
            colorOjos = ["Cafe","Verde","Azul","Violeta","Negro"]
            colorPiel = ["Negro","Moreno","Blanco"]
            copasBusto = ["A","B","C","D"]
            particularidades = ["Acromatopsia","Vitíligo","Difalia","Dismetría","Hermafroditismo"]


            


            ##Declaraciones
            self.id= Id
            self.agencia = IdAgencia
            self.portafolio = IdPortafolio

            self.pasaporte = random.randint(1000000,9999999)                
            self.pais = paises[random.randint(0,len(paises)-1)]
            self.fechaNacimiento = str(f"{random.randint(1,30)}/{random.randint(1,12)}/{random.randint(1990,2020)}")
            self.colorOjos = colorOjos[random.randint(0,len(colorOjos)-1)]
            self.colorPiel = colorPiel[random.randint(0,len(colorPiel)-1)]
            self.estatura = str(random.randint(100,250))
            self.cintura = str(random.randint(30,80))
            self.busto = copasBusto[random.randint(0,len(copasBusto)-1)]
            self.tallaZapato = str(random.randint(25,45))
            self.peso = str(random.randint(40,120))
            self.particularidad =[particularidades[random.randint(0,len(particularidades)-1)]]
        else:            
            print("---Ingrese la siguiente informacion de la Modelo---")
            self.id= Id
            self.agencia = IdAgencia
            self.portafolio = IdPortafolio

            Persona.__init__(self,Automatico,Genero)

            self.pasaporte = input("Pasaporte: ")               
            self.pais = input("Pais de Origen: ")
            self.fechaNacimiento = input("Fecha de nacimiento: ")
            self.colorOjos = input("Color de Ojos: ")
            self.colorPiel = input("Color de Piel: ")
            self.estatura = input("Estatura en cm: ")
            self.cintura = input("Medida Cintura: ")
            self.busto = input("Copa Busto: ")
            self.tallaZapato = input("Medida de Zapatos: ")
            self.peso = input("Peso: ")
            self.particularidad = list(input("Ingrese las particularidades de la modelo separadas por espacio").strip().split())

            

    def __str__(self):
        return (f"------------Modelo #{self.id}------------\nID: {self.id}\nAgencia: #{self.agencia.id}\nPortafolio: #{self.portafolio.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\
\nDireccion: {self.getDireccion()}\nPasaporte {self.pasaporte}\nPais de Origen: {self.pais}\nFecha Nacimiento: {self.fechaNacimiento}\
\n------Descripción Fisica------\nColor Ojos: {self.colorOjos}\nColor Piel: {self.colorPiel}\nEstatura: {self.estatura} cm\
\nDiametro Cintura: {self.cintura} cm\nCopa Busto: {self.busto}\nTalla Zapatos: {self.tallaZapato}\nPeso: {self.peso} Kilos\nParticularidades: {self.particularidad}")






#juanito = Modelo(True,"m",3121,21,132)
#print(juanito)
