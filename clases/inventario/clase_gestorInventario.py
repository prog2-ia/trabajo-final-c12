class GestorInventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, nuevo_item):
        self.items.append(nuevo_item)
        print("Item agregado")

    def mostrar_inventario(self):
        if not self.items:
            print("El inventario está vacío.")
        else:
            for item in self.items:
                print(item)
        print("--------------------------------------\n")

