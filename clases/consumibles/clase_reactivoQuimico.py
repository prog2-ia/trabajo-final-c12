from clases.consumibles.clase_consumible import Consumible


class ReactivoQuimico(Consumible):

    # constructor de reactivo quimico
    def __init__(self, id_item, nombre, cantidad, unidad_medida, requisitos_seguridad,
                 umbral_critico, fecha_caducidad, lote, formula_quimica, nivel_toxicidad):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # atributos propios
        self.formula_quimica = formula_quimica
        self.nivel_toxicidad = nivel_toxicidad


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | Formula: {self.formula_quimica} | Toxicidad: {self.nivel_toxicidad}"


    # muestra toda la informacion del reactivo
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Formula quimica: {self.formula_quimica}")
        print(f"Nivel de toxicidad: {self.nivel_toxicidad}")


    # cambia la formula quimica
    def cambiar_formula(self, nueva_formula):
        self.formula_quimica = nueva_formula
        print("Formula quimica actualizada")


    # cambia el nivel de toxicidad
    def cambiar_toxicidad(self, nuevo_nivel):
        self.nivel_toxicidad = nuevo_nivel
        print("Nivel de toxicidad actualizado")


    # compara si dos reactivos tienen la misma formula
    def misma_formula(self, otro_reactivo):
        return self.formula_quimica == otro_reactivo.formula_quimica

    #Metodo Abstracto heredado de ItemInventario
    def mostrar_detalles(self):
        print(f" FICHA TÉCNICA QUÍMICA")
        print(f"Reactivo: {self.nombre}")
        print(f"Fórmula: {self.formula_quimica}")
        print(f"Nivel de Riesgo: {self.nivel_toxicidad}")
        print(f"Lote de Control: {self.lote}")
        print(f"Medidas de Seguridad: {self.requisitos_seguridad}")
