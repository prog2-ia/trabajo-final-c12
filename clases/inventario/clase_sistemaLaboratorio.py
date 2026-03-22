from clases.inventario.clase_gestorInventario import GestorInventario


class SistemaLaboratorio:
    def __init__(self):
        self.gestorInventario = GestorInventario()

    def iniciar(self):
        print("="*50)
        print("Iniciando el sistema de almacenamiento del laboratorio")
        print("="*50)

        print(">>Inventario inicial: ")
        self.gestorInventario.mostrar_inventario()

        for item in self.gestorInventario.items:
            if item.id_item.startswith("RC"):
                item.consumir_stock_critico(50,usuario="Profesor Romero",motivo="Practica número 3")

                print("Verificando la Auditoria del reactivo")
                item.ver_historial()
                break

