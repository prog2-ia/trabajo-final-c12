class GestorInventario:

    def __init__(self):
        self.lista_items = []   # lista donde se guardan los objetos


    def agregar_item(self, item):
        self.lista_items.append(item)   # añade un objeto a la lista
        print(f"Guardado: {item.nombre}")


    def mostrar_todo(self):

        # comprueba si la lista esta vacia
        if len(self.lista_items) == 0:
            print("Inventario vacio")

        else:
            # recorre todos los items
            for item in self.lista_items:
                print(item)


    def buscar_por_nombre(self, nombre):

        # recorre la lista buscando coincidencia
        for item in self.lista_items:
            if item.nombre.lower() == nombre.lower():
                return item

        return None   # no encontrado


    def eliminar_item(self, nombre):

        # recorre la lista para eliminar
        for item in self.lista_items:
            if item.nombre.lower() == nombre.lower():
                self.lista_items.remove(item)
                print(f"{nombre} eliminado")
                return

        print("No encontrado")