from clases.equipos.clase_equipamiento import Equipamiento


class EquipoSeguridad(Equipamiento):

    # constructor de equipo de seguridad
    def __init__(self, id_item, nombre, cantidad, requisitos_seguridad,
                 umbral_critico, fecha_mantenimiento, ubicacion, certificado,
                 estado="Operativo"):

        # llama al constructor del padre
        super().__init__(id_item, nombre, cantidad, requisitos_seguridad,
                         umbral_critico, fecha_mantenimiento, estado)

        # atributos propios
        self.ubicacion = ubicacion
        self.certificado = certificado


    # metodo para mostrar el objeto
    def __str__(self):

        info = super().__str__()

        return f"{info} | Ubicacion: {self.ubicacion} | Certificado: {self.certificado}"


    # muestra toda la informacion del equipo
    def mostrar_info(self):

        super().mostrar_info()
        print(f"Ubicacion: {self.ubicacion}")
        print(f"Certificado: {self.certificado}")

    # realiza una prueba del equipo
    def realizar_prueba(self):
        print(f"Prueba realizada en {self.nombre}")


    # compara si dos equipos estan en la misma ubicacion
    def misma_ubicacion(self, otro_equipo):
        return self.ubicacion == otro_equipo.ubicacion



    #Metodo Abstracto heredado de ItemInventario
    def mostrar_detalles(self):
        print(f" [PROTOCOLO DE SEGURIDAD:{self.nombre}")
        print(f"ID: {self.id_item} | Ubicación: {self.ubicacion}")
        print(f"Estado Actual: {self.estado}")
        print(f"Certificación: {self.certificado}")
        print(f"Última Inspección: {self.fecha_mantenimiento}")
        print(f"Requisitos Técnicos: {self.requisitos_seguridad}")