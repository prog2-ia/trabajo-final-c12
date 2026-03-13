# Clase base
class ItemInventario:

    categoria = "Item de laboratorio"

    def __init__(self, nombre, id_item, proveedor, cantidad):
        self.nombre = nombre
        self.id_item = id_item
        self.proveedor = proveedor
        self._cantidad = 0
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre}, id: {self.id_item}, proveedor: {self.proveedor}, cantidad: {self.cantidad}"

    def consumir(self, unidades):
        if unidades <= 0:
            print("Las unidades a consumir deben ser positivas")
        elif unidades > self.cantidad:
            print("No hay suficientes unidades")
        else:
            self._cantidad -= unidades
            print(f"Se han consumido {unidades} unidades")

    def mostrar_info(self):
        print(f"nombre: {self.nombre}")
        print(f"id_item: {self.id_item}")
        print(f"proveedor: {self.proveedor}")
        print(f"cantidad: {self.cantidad}")

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor < 0:
            print("La cantidad no puede ser negativa")
        else:
            self._cantidad += valor
            print(f"Se han añadido {valor} unidades")


