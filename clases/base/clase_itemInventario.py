class ItemInventario:

    # Constructor: se ejecuta al crear un objeto
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad, umbral_critico):
        self.id_item = id_item                  # identificador del producto
        self.nombre = nombre                    # nombre del producto
        self.cantidad = cantidad                # cantidad disponible
        self.unidad_medida = unidad_medida      # unidades (kg, ml, unidades, etc.)
        self.requisitos_seguridad = requisitos_seguridad  # normas de seguridad
        self.umbral_critico = umbral_critico    # mínimo antes de ser crítico



    def __str__(self):
        return f"[{self.id_item}] {self.nombre} - {self.cantidad} {self.unidad_medida}"


    # Método para añadir stock al inventario
    def añadir_stock(self, cantidad_a_añadir):

        # Comprobamos que la cantidad sea positiva
        if cantidad_a_añadir > 0:
            self.cantidad += cantidad_a_añadir   # sumamos al stock
            print(f"Se han añadido {cantidad_a_añadir} {self.unidad_medida} de {self.nombre}")
        else:
            print("Error: no se puede añadir una cantidad negativa o cero")


    # Método para consumir (restar) stock
    def consumir_stock(self, cantidad_a_consumir):

        # Validación: debe ser mayor que 0
        if cantidad_a_consumir <= 0:
            print("Error: la cantidad a consumir debe ser mayor que cero")

        # Validación: no puedes consumir más de lo que hay
        elif cantidad_a_consumir > self.cantidad:
            print("Error: no hay suficiente stock")

        # Caso correcto: se resta
        else:
            self.cantidad -= cantidad_a_consumir
            print(f"Se han consumido {cantidad_a_consumir} {self.unidad_medida} de {self.nombre}")


    # Método para comprobar si el stock es crítico
    def es_critico(self):
        return self.cantidad <= self.umbral_critico