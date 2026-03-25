from clases.inventario.clase_gestorInventario import GestorInventario
from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from datetime import datetime

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
        print("Bienvenido al Sistema de almacenamiento del Laboratorio, escoja una acción (1,2,3,4): ")
        print("1: Mostrar Inventario","\n","2: Añadir Item","\n", "3: Borrar Item","\n", "4: Registrar uso de un Item ")
        opcion=int(input("Introduce tu elección: "))
        if opcion ==1:
            print(">>Inventario inicial: ")
            self.gestorInventario.mostrar_inventario()

        elif opcion==2:
            print("¿ Que tipo de Item desea añadir ?")
            print("1: Consumible (Reactivo Quimico, Material Biológico) | 2: Equipo (Equipo de Seguridad , Instrumentos Analíticos)")
            tipo_item=int(input("Introduce tu elección: "))

            if tipo_item==1:
                print("¿Que tipo de consumible quieres registrar?","\n","1: Reactivo Químico | 2:Material Biológico")
                tipo_consumible=int(input("Introduce tu elección: "))
                id_item = input("Id Item: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                unidad_medida = input("Unidad de Medida: ")
                requisitos_seguridad = input("Requisitos de Seguridad: ")
                umbral_critico = int(input("Umbral Crítico: "))
                fecha_caducidad = datetime.strptime(input("Fecha de caducidad (DD/MM/AAAA): "), "%d/%m/%Y")
                lote=input("Lote: ")
                if tipo_consumible==1:
                    formula_quimica= input("Introduce fórmula Química: ")
                    nivel_toxicidad=int(input("Introduce el nivel de toxicidad (1-5):"))
                    while True:
                        if nivel_toxicidad>5 or nivel_toxicidad<1:
                            print("Porfavor escoje un nivel válido ")
                            nivel_toxicidad=int(input("Introduce el nivel de toxicidad (1-5): "))
                        else:
                            return False
                    self.gestorInventario.agregar_item(nuevo_item=ReactivoQuimico(id_item,nombre, cantidad, unidad_medida, requisitos_seguridad, umbral_critico, fecha_caducidad, lote, formula_quimica, nivel_toxicidad))

                    GestorInventario.agregar_item()
    #Este bucle detecta si el Item del inventario es un Reactivo critico, mediante las 2 letras iniciales de su id, y si lo es registra su uso en el registro de auditoria
        for item in self.gestorInventario.items:
            if item.id_item.startswith("RC"):
                item.consumir_stock_critico(50,usuario="Profesor Romero",motivo="Practica número 3")

                print("Verificando la Auditoria del reactivo")
                item.ver_historial()
                break

