from clases.inventario.clase_gestorInventario import GestorInventario


class SistemaLaboratorio:
    def __init__(self):
        self.gestor = None

        def inicializar(self):
            print("--- Iniciando el Sistema ---")
            self.gestor = GestorInventario()
            print("Sistema listo.")

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
            self.inicializar()

            while True:
                self.mostrarMenu()
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    print("Llamando a gestor.agregar_item()...")
                elif opcion == "2":
                    print("Mostrando inventario...")
                elif opcion == "5":
                    print("Cerrando sistema. ¡Adiós!")
                    break
                else:
                    print("Opción no válida, intente de nuevo.")