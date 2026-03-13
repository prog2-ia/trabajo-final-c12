from clases.inventario.clase_gestorInventario import GestorInventario


class SistemaLaboratorio:
    def __init__(self):
        self.gestor=None

    def iniciar(self):
        print("Cargando inventario..")
        self.gestor=GestorInventario
        print("Sistema listo")

    def mostrarMenu(self):
        print("\n" + "=" * 30)
        print("   SISTEMA DE LABORATORIO")
        print("=" * 30)
        print("1. Registrar nuevo ítem (Reactivo/Equipo)")
        print("2. Ver inventario completo")
        print("3. Buscar ítem por nombre")
        print("4. Eliminar ítem")
        print("5. Salir")
        print("=" * 30)

    def ejecutar(self):
        self.iniciar()

        while True:
            self.mostrarMenu()
            opcion=input("Escribe una opcion: ")

            if opcion=="1":
                print("Agregando Item:")
            elif opcion=="2":
                print("Mostrando Inventario: ")
            elif opcion=="5":
                print("Cerrando el sistema")
                break
            else:
                print("Opcion invalida, intente de nuevo")



