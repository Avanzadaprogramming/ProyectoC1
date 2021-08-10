import random
class Portafolio:
    def __init__(self,ID):
        self.id = ID
        self.foto= "Soy muy Sexy ;)"
        self.anoCreacion = random.randint(1800, 2020)

    def __str__(self):
        return f"----Portafolio #{self.id}----\nPortafolioID: {self.id}\nFoto: {self.foto}\nAño Creacion: {self.anoCreacion}"

