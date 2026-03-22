from clases.equipos.clase_equipamiento import Equipamiento


class InstrumentoAnalitico(Equipamiento):

    # constructor de instrumento analitico
    def __init__(self, id_item, nombre, cantidad, requisitos_seguridad,
                 umbral_critico, fecha_mantenimiento, tipo_analisis, precision,
                 estado="Operativo"):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, requisitos_seguridad,
                         umbral_critico, fecha_mantenimiento, estado)

        # atributos propios
        self.tipo_analisis = tipo_analisis   # tipo de analisis que realiza
        self.precision = precision           # nivel de precision


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | Analisis: {self.tipo_analisis} | Precision: {self.precision}"


    # muestra toda la informacion del instrumento
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Tipo de analisis: {self.tipo_analisis}")
        print(f"Precision: {self.precision}")


    # cambia el tipo de analisis
    def cambiar_tipo_analisis(self, nuevo_tipo):
        self.tipo_analisis = nuevo_tipo
        print("Tipo de analisis actualizado")


    # cambia la precision
    def cambiar_precision(self, nueva_precision):
        self.precision = nueva_precision
        print("Precision actualizada")


    # simula un analisis
    def realizar_analisis(self):
        print(f"Analisis realizado con {self.nombre}")


    # compara si dos instrumentos tienen la misma precision
    def misma_precision(self, otro_instrumento):
        return self.precision == otro_instrumento.precision


    print()