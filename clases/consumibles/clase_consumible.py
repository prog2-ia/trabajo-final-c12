from clases.base.clase_itemInventario import ItemInventario

class Consumible(ItemInventario):
    def __init__(self,id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico,fecha_caducidad,lote):
        super.__init__(id_item,nombre,cantidad,unidad_medida, requisitos_seguridad, umbral_critico)
        self.fecha_caducidad = fecha_caducidad
        self.lote = lote

    def __str__(self):
        info_item=super().__str__()
        return f"{info_item} | lote: {self.lote} | caduca: {self.fecha_caducidad}"



