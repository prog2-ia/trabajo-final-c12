from clases.base.clase_itemInventario import ItemInventario


class Equipamiento(ItemInventario):

    # constructor de equipamiento
    def __init__(self, id_item, nombre, cantidad, requisitos_seguridad,
                 umbral_critico, fecha_mantenimiento, estado="Operativo"):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, "unidades",
                         requisitos_seguridad, umbral_critico)

        # atributos propios
        self.fecha_mantenimiento = fecha_mantenimiento
        self.estado = estado


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | Estado: {self.estado} | Mantenimiento: {self.fecha_mantenimiento}"


    # muestra toda la informacion del equipamiento
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Fecha de mantenimiento: {self.fecha_mantenimiento}")
        print(f"Estado: {self.estado}")


    # cambia la fecha de mantenimiento
    def cambiar_fecha_mantenimiento(self, nueva_fecha):
        self.fecha_mantenimiento = nueva_fecha
        print("Fecha de mantenimiento actualizada")


    # cambia el estado del equipo
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print("Estado actualizado")


    # pone el equipo como operativo despues del mantenimiento
    def registrar_mantenimiento(self, nueva_fecha):
        self.fecha_mantenimiento = nueva_fecha
        self.estado = "Operativo"
        print(f"Mantenimiento actualizado para {self.nombre}")


    # compara si dos equipos tienen el mismo estado
    def mismo_estado(self, otro_equipo):
        return self.estado == otro_equipo.estado

    print()