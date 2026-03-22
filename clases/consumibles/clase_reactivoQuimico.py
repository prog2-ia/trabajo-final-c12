from clases.consumibles.clase_consumible import Consumible


class ReactivoQuimico(Consumible):

    # Constructor
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote, formula_quimica, nivel_toxicidad):

        # Llamamos al constructor del padre (Consumible)
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # Atributos propios del reactivo químico
        self.formula_quimica = formula_quimica     # Ej: H2O, NaCl
        self.nivel_toxicidad = nivel_toxicidad     # Ej: bajo, medio, alto


    # Método para mostrar el objeto
    def __str__(self):

        # Información del padre (Consumible + ItemInventario)
        info_consumible = super().__str__()

        # Añadimos lo propio de esta clase
        return f"{info_consumible} | Fórmula: {self.formula_quimica} | Toxicidad: {self.nivel_toxicidad}"


    # Método simple para comprobar si es peligroso
    def es_peligroso(self):

        # Si el nivel de toxicidad es alto, lo consideramos peligroso
        if self.nivel_toxicidad.lower() == "alto":
            return True
        else:
            return False