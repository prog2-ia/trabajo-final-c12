from datetime import datetime
from clases.consumibles.clase_consumible import Consumible


class MaterialBiologico(Consumible):

    # constructor de material biologico
    def __init__(self, id_item: str, nombre: str, cantidad: int, unidad_medida: str,
                 requisitos_seguridad: str, umbral_critico: int,
                 fecha_caducidad: datetime, lote: str,
                 tipo_muestra: str, nivel_bioseguridad: int,
                 temperatura_almacenamiento: int) -> None:

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # atributos propios
        self.tipo_muestra = tipo_muestra
        self.nivel_bioseguridad = nivel_bioseguridad
        self.temperatura_almacenamiento = temperatura_almacenamiento


    # metodo para mostrar el objeto
    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Muestra: {self.tipo_muestra} | BSL: {self.nivel_bioseguridad} | Temp: {self.temperatura_almacenamiento}C"


    # muestra toda la informacion del material biologico
    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"Tipo de muestra: {self.tipo_muestra}")
        print(f"Nivel de bioseguridad: BSL-{self.nivel_bioseguridad}")
        print(f"Temperatura de almacenamiento: {self.temperatura_almacenamiento}C")


    # cambia el tipo de muestra
    def cambiar_tipo_muestra(self, nuevo_tipo: str) -> None:
        if not nuevo_tipo.strip():
            raise ValueError("El tipo de muestra no puede estar vacio")
        self.tipo_muestra = nuevo_tipo
        print("Tipo de muestra actualizado")


    # cambia el nivel de bioseguridad
    def cambiar_nivel_bioseguridad(self, nuevo_nivel: int) -> None:
        if nuevo_nivel not in [1, 2, 3, 4]:
            raise ValueError("El nivel de bioseguridad debe ser 1, 2, 3 o 4")
        self.nivel_bioseguridad = nuevo_nivel
        print("Nivel de bioseguridad actualizado")


    # cambia la temperatura de almacenamiento
    def cambiar_temperatura(self, nueva_temp: int) -> None:
        self.temperatura_almacenamiento = nueva_temp
        print("Temperatura de almacenamiento actualizada")


    # compara si dos materiales son del mismo tipo de muestra
    def mismo_tipo(self, otro_material: "MaterialBiologico") -> bool:
        return self.tipo_muestra == otro_material.tipo_muestra


    # metodo abstracto heredado de ItemInventario
    def mostrar_detalles(self) -> None:
        print(f"PROTOCOLO BIOLOGICO: {self.nombre}")
        print(f"Tipo de Muestra: {self.tipo_muestra}")
        print(f"Nivel de Bioseguridad: BSL-{self.nivel_bioseguridad}")
        print(f"Temperatura de almacenamiento: {self.temperatura_almacenamiento}C")
        print(f"Lote: {self.lote}")
        print(f"Caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}")
        self.mostrar_estado_caducidad()