#Clase base
class ItemInventario:
    def __init__(self,nombre, id, proveedor):
        self.nombre = nombre
        self.id = id
        self.proveedor = proveedor

    def __str__(self):
        return f"{self.nombre} , {self.id}, {self.proveedor}"



medicamentos = ItemInventario('paracetamol',123,'pyzher' )
print(medicamentos)
