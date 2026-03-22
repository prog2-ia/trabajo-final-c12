from clases.base.clase_itemInventario import ItemInventario


class Consumible(ItemInventario):

    # Constructor de la clase hija
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote):

        # Llamamos al constructor de la clase padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico)

        # Atributos propios de Consumible
        self.fecha_caducidad = fecha_caducidad   # fecha en la que caduca
        self.lote = lote                         # número o código de lote


    # Metodo especial para mostrar el objeto
    def __str__(self):

        # Cogemos primero la información de la clase padre
        info_item = super().__str__()

        # Le añadimos la información propia de Consumible
        return f"{info_item} | lote: {self.lote} | caduca: {self.fecha_caducidad}"


    # Metodo para comprobar si el consumible está caducado
    def esta_caducado(self, fecha_actual):

        # Comparamos la fecha actual con la fecha de caducidad
        if fecha_actual > self.fecha_caducidad:
            return True
        else:
            return False