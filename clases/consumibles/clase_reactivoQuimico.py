from datetime import datetime
from clases.consumibles.clase_consumible import Consumible


class ReactivoQuimico(Consumible):

    # constructor de reactivo quimico
    def __init__(self, id_item: str, nombre: str, cantidad: int, unidad_medida: str,
                 requisitos_seguridad: str, umbral_critico: int,
                 fecha_caducidad: datetime, lote: str,
                 formula_quimica: str, nivel_toxicidad: int) -> None:

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, unidad_medida,
                         requisitos_seguridad, umbral_critico,
                         fecha_caducidad, lote)

        # atributos propios
        self.formula_quimica = formula_quimica
        self.nivel_toxicidad = nivel_toxicidad


    # metodo para mostrar el objeto
    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Formula: {self.formula_quimica} | Toxicidad: {self.nivel_toxicidad}/5"


    # muestra toda la informacion del reactivo
    def mostrar_info(self) -> None:
        super().mostrar_info()
        print(f"Formula quimica: {self.formula_quimica}")
        print(f"Nivel de toxicidad: {self.nivel_toxicidad}/5")


    # cambia la formula quimica
    def cambiar_formula(self, nueva_formula: str) -> None:
        if not nueva_formula.strip():
            raise ValueError("La formula quimica no puede estar vacia")
        self.formula_quimica = nueva_formula
        print("Formula quimica actualizada")


    # cambia el nivel de toxicidad
    def cambiar_toxicidad(self, nuevo_nivel: int) -> None:
        if nuevo_nivel not in [1, 2, 3, 4, 5]:
            raise ValueError("El nivel de toxicidad debe ser entre 1 y 5")
        self.nivel_toxicidad = nuevo_nivel
        print("Nivel de toxicidad actualizado")


    # comprueba si el reactivo es de alta toxicidad (nivel 4 o 5)
    def es_alta_toxicidad(self) -> bool:
        return self.nivel_toxicidad >= 4


    # compara si dos reactivos tienen la misma formula
    def misma_formula(self, otro_reactivo: "ReactivoQuimico") -> bool:
        return self.formula_quimica == otro_reactivo.formula_quimica


    # metodo abstracto heredado de ItemInventario
    def mostrar_detalles(self) -> None:
        print(f"FICHA TECNICA QUIMICA: {self.nombre}")
        print(f"Formula: {self.formula_quimica}")
        print(f"Nivel de toxicidad: {self.nivel_toxicidad}/5")
        if self.es_alta_toxicidad():
            print("AVISO: Reactivo de ALTA TOXICIDAD")
        print(f"Lote: {self.lote}")
        print(f"Caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}")
        print(f"Medidas de seguridad: {self.requisitos_seguridad}")
        self.mostrar_estado_caducidad()