from clases.equipos.clase_equipamiento import Equipamiento

class EquipoSeguridad(Equipamiento):
    def __init__ (self,id_item,nombre,cantidad, requisitos_seguridad, umbral_critico,fecha_manteniemiento,ubicacion , certificado,estado="Operativo"):
        super().__init__(nombre,nombre, cantidad, requisitos_seguridad, umbral_critico, fecha_manteniemiento, estado)
        self.ubicacion = ubicacion
        self.certificado = certificado

    def __str__(self):
        info_equipo=super().__str__()
        return f"{info_equipo} | Ubicacion: {self.ubicacion} | Certificado: {self.certificado}"

    def realizar_prueba(self):
        print(f"Simulacro realizado con el equipo {self.nombre} en la ubicacion {self.ubicacion}")

