from clases.base.clase_itemInventario import ItemInventario

class Equipamiento(ItemInventario):
    def __init__(self,id_item,nombre,cantidad, requisitos_seguridad, umbral_critico,fecha_manteniemiento,estado="Operativo"):
        super().__init__(id_item,nombre,cantidad,"unidades",requisitos_seguridad,umbral_critico)
        self.fecha_manteniemiento = fecha_manteniemiento
        self.estado = estado

    def __str__(self):
        info_item=super().__str__()
        return f"{info_item} | Estado: {self.estado} | Ultimo Mantenimiento: {self.fecha_manteniemiento}"

    def registar_mantenimiento(self,nueva_fecha):
        self.fecha_mantenimiento = nueva_fecha
        self.estado = "Operativo"
        print (f"Mantenimiento actualizado para {self.nombre}")


