from clases.consumibles.clase_consumible import Consumible
from clases.inventario.auditoria import Auditoria

#Definimos la clase ReactivoCritico
class ReactivoCritico(Consumible, Auditoria):
    # Definimos los atributos que hereda de la clase Consumible
    def __init__(self, id_item,nombre,cantidad,unidad_medida,requisitos_seguridad,umbral_critico,fecha_caducidad,lote,nivel_peligro):
        super().__init__(id_item,nombre,cantidad,unidad_medida,requisitos_seguridad,umbral_critico,fecha_caducidad,lote)
        self.nivel_peligro = nivel_peligro

    #Definimos Historial_uso como una lista en donde se guardaran los usos del reactivo
        self.historial_uso = []

    #Metodo que devuelve los datos de Reactivo critico como un string
    def __str__(self):
        info_consumible = super().__str__()
        return f"{info_consumible} | Peligro:  {self.nivel_peligro} | Registo: {len(self.historial_uso)}"

    #Metodo el cual obliga al usuario a registrar el uso del reactivo
    def consumir_stock_critico(self,cantidad_a_consumir,usuario,motivo):
        super().consumir_stock(cantidad_a_consumir)
        self.registar_uso(usuario,cantidad_a_consumir,motivo)