from datetime import datetime
from clases.consumibles.clase_materialBiologico import MaterialBiologico
from clases.inventario.auditoria import Auditoria


class MaterialBiologicoCritico(MaterialBiologico, Auditoria):

    # constructor de material biologico critico
    def __init__(self, id_item: str, nombre: str, cantidad: int, unidad_medida: str,
                 requisitos_seguridad: str, umbral_critico: int,
                 fecha_caducidad: datetime, lote: str,
                 tipo_muestra: str, nivel_bioseguridad: int,
                 temperatura_almacenamiento: int, nivel_peligro: int) -> None:

        # llama al constructor de MaterialBiologico
        MaterialBiologico.__init__(self, id_item, nombre, cantidad, unidad_medida,
                                   requisitos_seguridad, umbral_critico,
                                   fecha_caducidad, lote, tipo_muestra,
                                   nivel_bioseguridad, temperatura_almacenamiento)

        # llama al constructor de Auditoria
        Auditoria.__init__(self)

        # atributos propios
        self.nivel_peligro = nivel_peligro


    # metodo para mostrar el objeto
    def __str__(self) -> str:
        info = super().__str__()
        return f"{info} | Peligro: {self.nivel_peligro}/5 | Registros: {len(self.historial_uso)}"


    # consume stock y obliga a registrar el uso en el historial
    def consumir_stock_critico(self, cantidad: int, usuario: str, motivo: str) -> None:
        if self.nivel_peligro >= 4:
            print(f"AVISO: Manipulando material biologico de ALTO PELIGRO (nivel {self.nivel_peligro}/5)")
        super().consumir_stock(cantidad)
        self.registrar_uso(usuario, cantidad, motivo)


    # cambia el nivel de peligro
    def cambiar_nivel_peligro(self, nuevo_nivel: int) -> None:
        if nuevo_nivel not in [1, 2, 3, 4, 5]:
            raise ValueError("El nivel de peligro debe ser entre 1 y 5")
        self.nivel_peligro = nuevo_nivel
        print("Nivel de peligro actualizado")


    # metodo abstracto heredado de ItemInventario
    def mostrar_detalles(self) -> None:
        print(f"ALERTA: MATERIAL BIOLOGICO CRITICO")
        print(f"Material: {self.nombre} | Peligro: {self.nivel_peligro}/5")
        print(f"Tipo de muestra: {self.tipo_muestra} | BSL-{self.nivel_bioseguridad}")
        print(f"Temperatura: {self.temperatura_almacenamiento}C")
        print(f"Seguridad: {self.requisitos_seguridad}")
        print(f"Caducidad: {self.fecha_caducidad.strftime('%d/%m/%Y')}")
        self.mostrar_estado_caducidad()
        print(f"Historial: {len(self.historial_uso)} registros de auditoria")
        self.ver_historial()