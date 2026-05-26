from clases.equipos.clase_equipamiento import Equipamiento


class InstrumentoAnalitico(Equipamiento):

    # constructor de instrumento analitico
    def __init__(self, id_item:str, nombre:str, cantidad:int, requisitos_seguridad:str,
                 umbral_critico:int, fecha_mantenimiento:str, tipo_analisis:str, precision:int,
                 estado:str="Operativo"):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, requisitos_seguridad,
                         umbral_critico, fecha_mantenimiento, estado)

        # atributos propios
        self.tipo_analisis = tipo_analisis   # tipo de analisis que realiza
        self.precision = precision           # nivel de precision


    # metodo para mostrar el objeto
    def __str__(self)->str:

        info = super().__str__()

        return f"{info} | Analisis: {self.tipo_analisis} | Precision: {self.precision}"


    # muestra toda la informacion del instrumento
    def mostrar_info(self)->None:

        super().mostrar_info()
        print(f"Tipo de analisis: {self.tipo_analisis}")
        print(f"Precision: {self.precision}")


    # simula un analisis
    def realizar_analisis(self)->None:
        print(f"Analisis realizado con {self.nombre}")


    # compara si dos instrumentos tienen la misma precision
    def misma_precision(self, otro_instrumento:"InstrumentoAnalitico")->bool:
        return self.precision == otro_instrumento.precision


    #Metodo abstracto heredado de ItemInventario
    def mostrar_detalles(self)->None:
        print(f"ESPECIFICACIONES TÉCNICAS: {self.nombre} ")
        print(f"ID: {self.id_item} | Análisis: {self.tipo_analisis}")
        print(f"Precisión nominal: {self.precision}")
        print(f"Estado del equipo: {self.estado}")
        print(f"Próximo mantenimiento: {self.fecha_mantenimiento}")
        print(f"Protocolo de uso: {self.requisitos_seguridad}")