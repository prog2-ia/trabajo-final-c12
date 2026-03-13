class GestorInventario:
    def __init__(self):
        self.lista_items = []

    def agregar_item(self, item):
        self.lista_items.append(item)
        print(f" Guardando en el sistema : {item.nombre} ({type(item).__name__})")

    def buscar_por_nombre(self, nombre):
        for item in self.lista_items:
            if item.nombre.lower() == nombre.lower():
                return item
        return None

    def reporte_completo(self):
        if not self.lista_items:
            print("El inventario está vacío.")
            return

        print("\n--- REPORTE DE EXISTENCIAS ---")
        print(f"{'Categoría':<20} | {'Nombre':<20} | {'Stock':<10}")
        print("-" * 55)

        for item in self.lista_items:
            categoria = type(item).__name__
            print(f"{categoria:<20} | {item.nombre:<20} | {item.stock:<10}")

    def eliminar_item(self, nombre):
        item = self.buscar_por_nombre(nombre)
        if item:
            self.lista_items.remove(item)
            print(f" {nombre} ha sido eliminado del inventario.")
        else:
            print(f" No se encontró '{nombre}' para eliminar.")