from clases.consumibles.clase_consumible import Consumible
from clases.inventario.auditoria import Auditoria

class ReactivoCritico(Consumible, Auditoria):

    def __init__(self, id_item,nombre,cantidad,unidad_medida,requisitos_seguridad,umbral_critico,fecha_caducidad,lote,nivel_peligro):
        super().__init__(id_item,nombre,cantidad,unidad_medida,requisitos_seguridad,umbral_critico,fecha_caducidad,lote)
        self.nivel_peligro = nivel_peligro

        self.historial_uso = []

    def __str__(self):
        info_consumible = super().__str__()
        return f"{info_consumible} | Peligro:  {self.nivel_peligro} | Registo: {len(self.historial_uso)}"

    def consumir_stock_critico(self,cantidad_a_consumir,usuario,motivo):
        super().consumir_stock(cantidad_a_consumir)
        self.registar_uso(usuario,cantidad_a_consumir,motivo)