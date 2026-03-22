from clases.base.clase_itemInventario import ItemInventario


class Consumible(ItemInventario):

    # constructor de consumible
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico)

        # atributos propios
        self.fecha_caducidad = fecha_caducidad
        self.lote = lote


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | lote: {self.lote} | caduca: {self.fecha_caducidad}"


    # muestra toda la informacion del consumible
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Fecha de caducidad: {self.fecha_caducidad}")
        print(f"Lote: {self.lote}")


    # cambia la fecha de caducidad
    def cambiar_fecha_caducidad(self, nueva_fecha):
        self.fecha_caducidad = nueva_fecha
        print("Fecha de caducidad actualizada")


    # cambia el lote
    def cambiar_lote(self, nuevo_lote):
        self.lote = nuevo_lote
        print("Lote actualizado")


    # compara si dos consumibles tienen el mismo lote
    def mismo_lote(self, otro_consumible):
        return self.lote == otro_consumible.lote