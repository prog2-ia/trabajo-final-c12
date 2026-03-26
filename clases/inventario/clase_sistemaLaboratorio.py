from clases.inventario.clase_gestorInventario import GestorInventario
from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from datetime import datetime


class SistemaLaboratorio:
    def __init__(self):
        self.gestorInventario = GestorInventario()

    def iniciar(self):
        print("=" * 50)
        print("Iniciando el sistema de almacenamiento del laboratorio")
        print("=" * 50)

        def menu():
            # Variable para controlar el bucle principal del menú
            ejecutando_sistema = True

            while ejecutando_sistema:
                print("\nBienvenido al Sistema de almacenamiento del Laboratorio, escoja una acción (1,2,3,4,5): ")
                print(
                    " 1: Mostrar Inventario\n 2: Añadir Item\n 3: Borrar Item\n 4: Registrar uso de un Item\n 5: Salir del Sistema")

                opcion = int(input("Introduce tu acción elegida: "))

                if opcion not in [1, 2, 3, 4, 5]:
                    print("Introduce una opción válida")
                    continue

                elif opcion == 1:
                    print(">> Inventario actual: ")
                    self.gestorInventario.mostrar_inventario()

                    # Tu lógica de M/F
                    while True:
                        accion = input("Volver al Menu (M) | Finalizar el programa (F): ").upper()
                        if accion == "M":
                            break  # Rompe este bucle interno y vuelve al inicio del 'while ejecutando_sistema'
                        elif accion == "F":
                            ejecutando_sistema = False  # Apaga el sistema completo
                            break
                        else:
                            print("Acción inválida")

                elif opcion == 2:
                    print("¿Qué tipo de Item desea añadir?")
                    print("1: Consumible | 2: Equipo")
                    while True:
                        tipo_item = int(input("Introduce tu elección: "))
                        if tipo_item in [1, 2]:
                            break
                        else:
                            print("Introduce un tipo de Item correcto")

                    if tipo_item == 1:
                        print("¿Que tipo de consumible quieres registrar?\n 1: Reactivo Químico | 2: Material Biológico")
                        while True:
                            tipo_consumible = int(input("Introduce tu elección: "))
                            if tipo_consumible in [1, 2]:
                                break
                            else:
                                print("Introduce un tipo de consumible correcto")


                        # Datos comunes
                        id_item = input("Id Item: ")
                        nombre = input("Nombre: ")
                        cantidad = int(input("Cantidad: "))
                        unidad_medida = input("Unidad de Medida: ")
                        requisitos_seguridad = input("Requisitos de Seguridad: ")
                        umbral_critico = int(input("Umbral Crítico: "))
                        fecha_caducidad = datetime.strptime(input("Fecha de caducidad (DD/MM/AAAA): "), "%d/%m/%Y")
                        lote = input("Lote: ")



                        if tipo_consumible == 1:
                            formula_quimica = input("Introduce fórmula Química: ")

                            while True:
                                entrada = input("Introduce el nivel de toxicidad (1-5): ")
                                try:
                                    nivel_toxicidad = int(entrada)
                                    if 1 <= nivel_toxicidad <= 5:
                                        break
                                    else:
                                        print("Por favor escoja un nivel válido (1-5)")

                                except ValueError:
                                    print(f"{entrada} no es un número válido. Por favor solo utiliza dígitos ")

                            # AHORA agregamos el ítem (Fuera del bucle de validación, pero dentro del if)
                            nuevo_item = ReactivoQuimico(id_item, nombre, cantidad, unidad_medida,
                                                         requisitos_seguridad, umbral_critico,
                                                         fecha_caducidad, lote, formula_quimica, nivel_toxicidad)
                            self.gestorInventario.agregar_item(nuevo_item)
                            print("Item añadido con éxito.")

                elif opcion == 5:
                    ejecutando_sistema = False

        menu()

