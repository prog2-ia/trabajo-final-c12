from abc import ABC, abstractmethod


class ItemInventario(ABC):

    # constructor de la clase base
    def __init__(self, id_item: str, nombre: str, cantidad: int,
                 unidad_medida: str, requisitos_seguridad: str, umbral_critico: int) -> None:
        self.id_item = id_item
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.requisitos_seguridad = requisitos_seguridad
        self.umbral_critico = umbral_critico


    # metodo para mostrar el objeto
    def __str__(self) -> str:
        return f"[{self.id_item}] {self.nombre} - {self.cantidad} {self.unidad_medida}"


    # compara si dos items tienen la misma cantidad
    def __eq__(self, otro: object) -> bool:
        if isinstance(otro, ItemInventario):
            return self.cantidad == otro.cantidad
        return NotImplemented


    # compara si este item tiene menos cantidad que otro
    def __lt__(self, otro: "ItemInventario") -> bool:
        return self.cantidad < otro.cantidad


    # compara si este item tiene mas cantidad que otro
    def __gt__(self, otro: "ItemInventario") -> bool:
        return self.cantidad > otro.cantidad


    # suma las cantidades de dos items y devuelve el total
    def __add__(self, otro: "ItemInventario") -> int:
        return self.cantidad + otro.cantidad


    # muestra toda la informacion del item
    def mostrar_info(self) -> None:
        print(f"Id: {self.id_item}")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Unidad de medida: {self.unidad_medida}")
        print(f"Requisitos de seguridad: {self.requisitos_seguridad}")
        print(f"Umbral critico: {self.umbral_critico}")


    # añade stock
    def añadir_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a añadir debe ser mayor que 0")
        self.cantidad += cantidad
        print(f"Se han añadido {cantidad} {self.unidad_medida} de {self.nombre}")


    # consume stock
    def consumir_stock(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad a consumir debe ser mayor que 0")
        if cantidad > self.cantidad:
            raise ValueError(f"No hay suficiente stock. Disponible: {self.cantidad} {self.unidad_medida}")
        self.cantidad -= cantidad
        print(f"Se han consumido {cantidad} {self.unidad_medida} de {self.nombre}")


    # comprueba si el item esta en nivel critico
    def es_critico(self) -> bool:
        return self.cantidad <= self.umbral_critico


    # muestra mensaje segun el nivel de stock
    def mostrar_estado_stock(self) -> None:
        if self.es_critico():
            print(f"AVISO: {self.nombre} esta en nivel critico ({self.cantidad} {self.unidad_medida})")
        else:
            print(f"OK: {self.nombre} tiene stock suficiente ({self.cantidad} {self.unidad_medida})")


    # cambia el nombre del item
    def cambiar_nombre(self, nuevo_nombre: str) -> None:
        self.nombre = nuevo_nombre
        print("Nombre actualizado")


    # cambia los requisitos de seguridad
    def cambiar_requisitos_seguridad(self, nuevos_requisitos: str) -> None:
        self.requisitos_seguridad = nuevos_requisitos
        print("Requisitos de seguridad actualizados")


    # cambia el umbral critico
    def cambiar_umbral_critico(self, nuevo_umbral: int) -> None:
        if nuevo_umbral < 0:
            raise ValueError("El umbral critico no puede ser negativo")
        self.umbral_critico = nuevo_umbral
        print("Umbral critico actualizado")


    # repone el item hasta una cantidad concreta
    def reponer_hasta(self, cantidad_objetivo: int) -> None:
        if cantidad_objetivo > self.cantidad:
            diferencia = cantidad_objetivo - self.cantidad
            self.cantidad += diferencia
            print(f"Se han repuesto {diferencia} {self.unidad_medida}")
        else:
            print("No hace falta reponer")


    # compara si dos items tienen el mismo id
    def mismo_id(self, otro_item: "ItemInventario") -> bool:
        return self.id_item == otro_item.id_item


    @abstractmethod
    def mostrar_detalles(self) -> None:
        pass