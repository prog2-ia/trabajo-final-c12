from clases.consumibles.clase_consumible import Consumible

class MaterialBiologico(Consumible):
    def __init__(self,id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico,fecha_caducidad,lote,tipo_muestra,nivel_bioseguridad,_temperatura_almacenamiento):
        super().__init__(id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico,fecha_caducidad,lote)
        self.tipo_muestra=tipo_muestra
        self.nivel_bioseguridad=nivel_bioseguridad
        self.temperatura_almacenamiento=_temperatura_almacenamiento

    def _str(self):
        info_consumible=super().__str__()
        return f"{info_consumible} | Muestra: {self.tipo_muestra} | BSL: {self.nivel_bioseguridad} | Temperatura de Almacenamiento: {self.temperatura_almacenamiento}"



