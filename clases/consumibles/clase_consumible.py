from datetime import datetime
from clases.base.clase_itemInventario import ItemInventario


class Consumible(ItemInventario):

    # constructor de consumible
    def __init__(self, id_item: str, nombre: str, cantidad: int, unidad_medida: str,
                 requisitos_seguridad: str, umbral_critico: int,
                 fecha_caducidad: datetime, lote: str) -> None:

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico)

        # atributos propios
        self.fecha_caducidad = fecha_caducidad
        self.lote = lote


    # metodo para mostrar el objeto
    def __str__(self) -> str:
        info = super().__str__()
        fecha_str = self.fecha_caducidad.strftime("%d/%m/%Y")
        return f"{info} | lote: {self.lote} | caduca: {fecha_str}"


    # muestra toda la informacion del consumible
    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"Fecha de caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}")
        print(f"Lote: {self.lote}")


    # comprueba si el consumible esta caducado
    def esta_caducado(self) -> bool:
        return datetime.now() > self.fecha_caducidad


    # muestra cuantos dias quedan para caducar
    def mostrar_estado_caducidad(self) -> None:
        if self.esta_caducado():
            print(f"AVISO: {self.nombre} esta CADUCADO desde {self.fecha_caducidad.strftime('%d/%m/%Y')}")
        else:
            dias = (self.fecha_caducidad - datetime.now()).days
            print(f"OK: {self.nombre} caduca en {dias} dias ({self.fecha_caducidad.strftime('%d/%m/%Y')})")


    # cambia el lote
    def cambiar_lote(self, nuevo_lote: str) -> None:
        if not nuevo_lote.strip():
            raise ValueError("El lote no puede estar vacio")
        self.lote = nuevo_lote
        print("Lote actualizado")


    # consume stock solo si el producto no esta caducado
    def consumir_stock(self, cantidad: int) -> None:
        if self.esta_caducado():
            raise ValueError(f"No se puede consumir '{self.nombre}': producto caducado")
        super().consumir_stock(cantidad)


    # compara si dos consumibles tienen el mismo lote
    def mismo_lote(self, otro_consumible: "Consumible") -> bool:
        return self.lote == otro_consumible.lote