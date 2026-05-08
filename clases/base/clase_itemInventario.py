from abc import ABC, abstractmethod
class ItemInventario(ABC):

    # constructor de la clase base
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad, umbral_critico):
        self.id_item = id_item
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.requisitos_seguridad = requisitos_seguridad
        self.umbral_critico = umbral_critico


    # metodo para mostrar el objeto
    def __str__(self):
        return f"[{self.id_item}] {self.nombre} - {self.cantidad} {self.unidad_medida}"


    # muestra toda la informacion del item
    def mostrar_info(self):
        print(f"Id: {self.id_item}")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Unidad de medida: {self.unidad_medida}")
        print(f"Requisitos de seguridad: {self.requisitos_seguridad}")
        print(f"Umbral critico: {self.umbral_critico}")


    # añade stock
    def añadir_stock(self, cantidad):

        if cantidad > 0:
            self.cantidad += cantidad
            print(f"Se han añadido {cantidad} {self.unidad_medida} de {self.nombre}")
        else:
            print("Cantidad no valida")


    # consume stock
    def consumir_stock(self, cantidad):

        if cantidad <= 0:
            print("Cantidad no valida")

        elif cantidad > self.cantidad:
            print("No hay suficiente stock")

        else:
            self.cantidad -= cantidad
            print(f"Se han consumido {cantidad} {self.unidad_medida} de {self.nombre}")


    # comprueba si el item esta en nivel critico
    def es_critico(self):
        return self.cantidad <= self.umbral_critico


    # muestra mensaje segun el nivel de stock
    def mostrar_estado_stock(self):

        if self.es_critico():
            print(f"{self.nombre} esta en nivel critico")
        else:
            print(f"{self.nombre} tiene stock suficiente")


    # cambia el nombre del item
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print("Nombre actualizado")


    # cambia los requisitos de seguridad
    def cambiar_requisitos_seguridad(self, nuevos_requisitos):
        self.requisitos_seguridad = nuevos_requisitos
        print("Requisitos de seguridad actualizados")


    # cambia el umbral critico
    def cambiar_umbral_critico(self, nuevo_umbral):

        if nuevo_umbral >= 0:
            self.umbral_critico = nuevo_umbral
            print("Umbral critico actualizado")
        else:
            print("Umbral no valido")


    # repone el item hasta una cantidad concreta
    def reponer_hasta(self, cantidad_objetivo):

        if cantidad_objetivo > self.cantidad:
            diferencia = cantidad_objetivo - self.cantidad
            self.cantidad += diferencia
            print(f"Se han repuesto {diferencia} {self.unidad_medida}")
        else:
            print("No hace falta reponer")


    # compara si dos items tienen el mismo id
    def mismo_id(self, otro_item):
        return self.id_item == otro_item.id_item


    print()

    @abstractmethod
    def mostrar_detalles(self):
        print("Detalles")
        pass
