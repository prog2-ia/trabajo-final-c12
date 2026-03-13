from clases.base.clase_itemInventario import ItemInventario

class Seguridad:

    def __init__(self):
        self.usuarios_autorizados = ["admin", "tecnico", "supervisor"]
        self.registros = []

    def validar_acceso(self, usuario):
        if usuario in self.usuarios_autorizados:
            return True
        else:
            return False

    def registrar_acceso(self, usuario, accion):
        registro = f"Usuario: {usuario} - Acción: {accion}"
        self.registros.append(registro)
        print("Acceso registrado")

    def alertar_riesgo(self, nivel, item):
        print(f"Alerta de riesgo {nivel} con el item {item.nombre}")

medicamento = ItemInventario("paracetamol", 123, "pyzher", 21)

seguridad = Seguridad()

print(seguridad.validar_acceso("admin"))
print(seguridad.validar_acceso("juan"))

seguridad.registrar_acceso("admin", "ha entrado al sistema")
seguridad.alertar_riesgo("alto", medicamento)

print(seguridad.registros)