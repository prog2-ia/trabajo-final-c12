
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
                print(item)
                item.mostrar_detalles()
                print("--------------------------------------\n")

