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


    # cambia la ubicacion
    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print("Ubicacion actualizada")


    # cambia el certificado
    def cambiar_certificado(self, nuevo_certificado):
        self.certificado = nuevo_certificado
        print("Certificado actualizado")


    # realiza una prueba del equipo
    def realizar_prueba(self):
        print(f"Prueba realizada en {self.nombre}")


    # compara si dos equipos estan en la misma ubicacion
    def misma_ubicacion(self, otro_equipo):
        return self.ubicacion == otro_equipo.ubicacion


    print()