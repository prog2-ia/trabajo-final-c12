from clases.consumibles.clase_consumible import Consumible

class ReactivoQuimico(Consumible):
    def __init__(self,id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico,fecha_caducidad,lote,formula_quimica,nivel_toxicidad):
        super().__init__(id_item,nombre,cantidad,unidad_medida,requisitos_seguridad,umbral_critico,fecha_caducidad,lote)
        self.formula_quimica=formula_quimica
        self.nivel_toxicidad=nivel_toxicidad

    def __str__(self):
        info_consumible=super().__str__()
        return f"{info_consumible} | Fórmula: {self.formula_quimica} | Riesgo: {self.nivel_toxicidad}"

