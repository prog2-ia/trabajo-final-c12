#Clase base
class ItemInventario:

    categoria = "Item de laboratorio"

    def __init__(self,nombre, id_item, proveedor, cantidad):
        self.nombre = nombre
        self.id_item = id_item
        self.proveedor = proveedor
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} ,id : {self.id}, proveedor : {self.proveedor}, cantidad : {self.cantidad}"


    def consumir(self, unidades):
        self.cantidad += unidades
        if unidades > self.cantidad:
            print(f'Se han añadido {unidades} unidades')
        else:
            print(f'se han acabado {unidades} unidades')


    def mostrar_info(self):
        print(f'nombre : {self.nombre}')
        print(f'id_item : {self.id_item}')
        print(f'proveedor : {self.proveedor}')
        print(f'cantidad : {self.cantidad}')


print('guradas')


medicamentos = ItemInventario('paracetamol',123,'pyzher' )
print(medicamentos)
