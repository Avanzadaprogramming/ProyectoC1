class Pabellon:
    def __init__(self,iD,Empleado,Telefono):
        self.id = iD
        self.empleado= Empleado
        self.telefono= Telefono
        self.estado = "Disponible"
    
    def __str__(self):
        return f"----Pabellon #{self.id}----\nId Empleado Acargo: {self.empleado.id}\nNombre Empleado Acargo: {self.empleado.nombre} {self.empleado.apellido}\
\nTelefono: {self.telefono}\nEstado: {self.estado}"
