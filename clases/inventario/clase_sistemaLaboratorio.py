from clases.inventario.clase_gestorInventario import GestorInventario

#Definimos la clase SitemaLaboratorio
class SistemaLaboratorio:
    #Esta clase utiliza los valores guardados en GestorInventario
    def __init__(self):
        self.gestorInventario = GestorInventario()
    #Metodo iniciar, que imprime los datos guardados en GestorInventario
    def iniciar(self):
        print("="*50)
        print("Iniciando el sistema de almacenamiento del laboratorio")
        print("="*50)

        print(">>Inventario inicial: ")
        self.gestorInventario.mostrar_inventario()
    #Este bucle detecta si el Item del inventario es un Reactivo critico, mediante las 2 letras iniciales de su id, y si lo es registra su uso en el registro de auditoria
        for item in self.gestorInventario.items:
            if item.id_item.startswith("RC"):
                item.consumir_stock_critico(50,usuario="Profesor Romero",motivo="Practica número 3")

                print("Verificando la Auditoria del reactivo")
                item.ver_historial()
                break

