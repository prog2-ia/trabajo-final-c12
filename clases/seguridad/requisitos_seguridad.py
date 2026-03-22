class Seguridad:

    # constructor de seguridad
    def __init__(self, nivel_seguridad, usuario_responsable):
        self.nivel_seguridad = nivel_seguridad
        self.usuario_responsable = usuario_responsable


    # metodo para mostrar el objeto
    def __str__(self):
        return f"Nivel de seguridad: {self.nivel_seguridad} | Responsable: {self.usuario_responsable}"


    # muestra toda la informacion de seguridad
    def mostrar_info_seguridad(self):
        print(f"Nivel de seguridad: {self.nivel_seguridad}")
        print(f"Usuario responsable: {self.usuario_responsable}")


    # cambia el nivel de seguridad
    def cambiar_nivel_seguridad(self, nuevo_nivel):
        self.nivel_seguridad = nuevo_nivel
        print("Nivel de seguridad actualizado")


    # cambia el usuario responsable
    def cambiar_usuario_responsable(self, nuevo_usuario):
        self.usuario_responsable = nuevo_usuario
        print("Usuario responsable actualizado")


    # comprueba si dos objetos tienen el mismo responsable
    def mismo_responsable(self, otro_objeto):
        return self.usuario_responsable == otro_objeto.usuario_responsable