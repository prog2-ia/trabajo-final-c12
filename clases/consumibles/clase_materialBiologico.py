from clases.consumibles.clase_consumible import Consumible


class MaterialBiologico(Consumible):

    # constructor de material biologico
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote,
                 tipo_muestra, nivel_bioseguridad, temperatura_almacenamiento):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # atributos propios
        self.tipo_muestra = tipo_muestra
        self.nivel_bioseguridad = nivel_bioseguridad
        self.temperatura_almacenamiento = temperatura_almacenamiento


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | Muestra: {self.tipo_muestra} | BSL: {self.nivel_bioseguridad} | Temp: {self.temperatura_almacenamiento}"


    # muestra toda la informacion del material biologico
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Tipo de muestra: {self.tipo_muestra}")
        print(f"Nivel de bioseguridad: {self.nivel_bioseguridad}")
        print(f"Temperatura de almacenamiento: {self.temperatura_almacenamiento}")


    # cambia el tipo de muestra
    def cambiar_tipo_muestra(self, nuevo_tipo):
        self.tipo_muestra = nuevo_tipo
        print("Tipo de muestra actualizado")


    # cambia el nivel de bioseguridad
    def cambiar_nivel_bioseguridad(self, nuevo_nivel):
        self.nivel_bioseguridad = nuevo_nivel
        print("Nivel de bioseguridad actualizado")


    # compara si dos materiales son del mismo tipo
    def mismo_tipo(self, otro_material):
        return self.tipo_muestra == otro_material.tipo_muestra

    #Metodo Abstracto heredado de ItemInventario
    def mostrar_detalles(self):
        print(f"PROTOCOLO BIOLÓGICO: {self.nombre}")
        print(f"Tipo de Muestra: {self.tipo_muestra}")
        print(f"Nivel de Bioseguridad: BSL-{self.nivel_bioseguridad}")
        print(f"Almacenamiento: {self.temperatura_almacenamiento}")
        print(f"Lote: {self.lote}")
