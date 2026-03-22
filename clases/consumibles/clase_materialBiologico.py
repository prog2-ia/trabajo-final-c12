from clases.consumibles.clase_consumible import Consumible


class MaterialBiologico(Consumible):

    # Constructor
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote,
                 tipo_muestra, nivel_bioseguridad, temperatura_almacenamiento):

        # Llamamos al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # Atributos propios de material biológico
        self.tipo_muestra = tipo_muestra                  # Ej: sangre, tejido, bacteria
        self.nivel_bioseguridad = nivel_bioseguridad      # Ej: BSL-1, BSL-2, BSL-3
        self.temperatura_almacenamiento = temperatura_almacenamiento  # Ej: -20°C


    # Método para mostrar el objeto
    def __str__(self):

        # Información heredada
        info_consumible = super().__str__()

        # Añadimos lo propio
        return f"{info_consumible} | Muestra: {self.tipo_muestra} | BSL: {self.nivel_bioseguridad} | Temp: {self.temperatura_almacenamiento}"


    # Método para comprobar si necesita condiciones especiales
    def necesita_refrigeracion(self):

        # Si la temperatura es menor que 0, necesita frío
        if "-" in str(self.temperatura_almacenamiento):
            return True
        else:
            return False