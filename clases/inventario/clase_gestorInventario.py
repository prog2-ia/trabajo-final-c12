
#Definimos la clase GestorInventario
class GestorInventario:
    #Dejamos una lista vacia en la cual se almacenen los objetos
    def __init__(self):
        self.items = []
    #Agrega los nuevos items a la lista item
    def agregar_item(self,nuevo_item):
        self.items.append(nuevo_item)
        print("Item agregado")
    #Se encarga de mostrar el inventario completo, si esta vacio, muestra que esta vacio
    def mostrar_inventario(self):
        if not self.items:
            print("El inventario está vacío.")
        else:
            for item in self.items:
                item.mostrar_info()
                print("--------------------------------------\n")


    def buscar_item_id(self,id_buscado:str):
        for item in self.items:
            if str(item.id_item)==str(id_buscado):
                return item
        return None

    def borrar_item(self, id_a_borrar: str):
        item_encontrado = self.buscar_item_id(id_a_borrar)

        if item_encontrado:
            self.items.remove(item_encontrado)
            print(f"Item '{item_encontrado.nombre}' (ID: {id_a_borrar}) eliminado del sistema.")
            return True
        else:
            print(f"No se pudo borrar: No existe ningún item con el ID '{id_a_borrar}'.")
            return False