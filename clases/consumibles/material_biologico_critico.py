from datetime import datetime
from clases.consumibles.clase_materialBiologico import MaterialBiologico
from clases.inventario.auditoria import Auditoria


class MaterialBiologicoCritico(MaterialBiologico, Auditoria):

    def __init__(self, id_item: str, nombre: str, cantidad: int, unidad_medida: str,
                 requisitos_seguridad: str, umbral_critico: int,
                 fecha_caducidad: datetime, lote: str,
                 tipo_muestra: str, nivel_bioseguridad: int,
                 temperatura_almacenamiento: int, nivel_peligro: int) -> None:
        # 1. Llamamos al constructor del padre (MaterialBiologico)
        MaterialBiologico.__init__(self, id_item, nombre, cantidad, unidad_medida,
                                   requisitos_seguridad, umbral_critico,
                                   fecha_caducidad, lote, tipo_muestra,
                                   nivel_bioseguridad, temperatura_almacenamiento)

        # 2. Llamamos al constructor de la Auditoria
        Auditoria.__init__(self)

        # 3. Atributo propio de la criticidad
        self.nivel_peligro = nivel_peligro

    def consumir_stock_critico(self, cantidad: int, usuario: str, motivo: str) -> None:
        if self.nivel_peligro >= 4:
            print(f"⚠️ AVISO: Manipulando material biológico de ALTO PELIGRO (nivel {self.nivel_peligro}/5)")

        # Consume el stock usando el metodo heredado de Consumible
        super().consumir_stock(cantidad)
        # Registra la auditoría
        self.registrar_uso(usuario, cantidad, motivo)

