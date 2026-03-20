
class ItemInventario:

    def __init__(self,id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico):
        self.id_item = id_item
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
        self.requisitos_seguridad = requisitos_seguridad
        self.umbral_critico = umbral_critico

    def __str__(self):
        return f"[{self.id_item}]{self.nombre} - {self.cantidad} {self.unidad_medida}"

