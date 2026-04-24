from clases.equipos.clase_equipoSeguridad import EquipoSeguridad
from clases.equipos.clase_intrumentoAnalitico import InstrumentoAnalitico
from clases.inventario.clase_gestorInventario import GestorInventario
from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from clases.consumibles.clase_materialBiologico import MaterialBiologico
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
                print("\nBienvenido al Sistema de almacenamiento del Laboratorio, escoja una acción (1,2,3,4,5,6): ")
                print(
                    " 1: Mostrar Inventario\n 2: Añadir Item\n 3: Borrar Item\n 4: Registrar uso de un Item\n 5: Aumentar Stock\n 6: Salir del Sistema")

                opcion = input("Introduce tu acción elegida: ")

                if opcion not in ["1","2","3","4","5"]:
                    print("\n","Introduce una opción válida")
                    continue

                elif opcion == "1":
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

                elif opcion == "2":
                    print("¿Qué tipo de Item desea añadir?")
                    print("1: Consumible | 2: Equipo")
                    while True:
                        tipo_item = input("Introduce tu elección: ")
                        if tipo_item in ["1","2"]:
                            break
                        else:
                            print("Introduce un tipo de Item correcto")

                    if tipo_item == "1":
                        print("¿Que tipo de consumible quieres registrar?\n 1: Reactivo Químico | 2: Material Biológico")
                        while True:
                            tipo_consumible = input("Introduce tu elección: ")
                            if tipo_consumible in ["1","2"]:
                                break
                            else:
                                print("Introduce un tipo de consumible correcto")



                        id_item = input("Id Item: ")
                        nombre = input("Nombre: ")
                        cantidad = input("Cantidad: ")
                        while True:
                            if cantidad.isdigit():
                                cantidad=int(cantidad)
                                break

                            else:
                                print(f"{cantidad} no es un número, porfavor inserta un número entero ")
                                cantidad = input("Cantidad: ")

                        unidad_medida = input("Unidad de Medida: ")
                        requisitos_seguridad = input("Requisitos de Seguridad: ")
                        umbral_critico = input("Umbral Crítico: ")
                        while True:
                            if umbral_critico.isdigit():
                                umbral_critico=int(umbral_critico)
                                break
                            else:
                                print(f"{umbral_critico} valor no aceptado, porfavor inserta un número")
                                umbral_critico=input("Umbral Critico: ")

                        while True:
                            fecha_caducidad_str = input("Fecha de Caducidad (DD/MM/AAAA): ")
                            try:
                                fecha_caducidad = datetime.strptime(fecha_caducidad_str, "%d/%m/%Y")
                                break
                            except ValueError:
                                print(
                                    f"'{fecha_caducidad_str}' no es un valor aceptado. Por favor, introduce una fecha válida (DD/MM/AAAA).")

                        lote = input("Lote: ")


                        if tipo_consumible == "1":
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


                            nuevo_item = ReactivoQuimico(id_item, nombre, cantidad, unidad_medida,
                                                         requisitos_seguridad, umbral_critico,
                                                         fecha_caducidad, lote, formula_quimica, nivel_toxicidad)
                            self.gestorInventario.agregar_item(nuevo_item)
                            print("Item añadido con éxito.")


                        if tipo_consumible=="2":
                            tipo_muestra = input("Tipo de Muestra: ")

                            while True:
                                entrada = input("Introduce el nivel de Bioseguridad (1-4): ")
                                try:
                                    nivel_bioseguridad = int(entrada)
                                    if 1 <= nivel_bioseguridad <= 4:
                                        break
                                    else:
                                        print("Por favor escoja un nivel válido (1-4)")

                                except ValueError:
                                    print(f"{entrada} no es un número válido. Por favor solo utiliza dígitos ")

                            while True:
                                entrada = input("Introduce la temperatura de almacenamiento (Cº): ")
                                try:
                                    temperatura_almacenamiento = int(entrada)
                                    break

                                except ValueError:
                                    print(f"{entrada} no es un número válido. Por favor solo utiliza dígitos ")

                            nuevo_item = MaterialBiologico(id_item, nombre, cantidad, unidad_medida,
                                                         requisitos_seguridad, umbral_critico,
                                                         fecha_caducidad, lote,tipo_muestra,nivel_bioseguridad, temperatura_almacenamiento)
                            self.gestorInventario.agregar_item(nuevo_item)
                            print("Item añadido con éxito.")

                    if tipo_item == "2":
                        print("¿Que tipo de Equipamiento quieres registrar?\n 1: Equipo de Seguridad | 2: Instrumento Analítico")
                        while True:
                            tipo_equipo = input("Introduce tu elección: ")
                            if tipo_equipo in ["1","2"]:
                                break
                            else:
                                print("Introduce un tipo de equipo correcto")



                        id_item = input("Id Item: ")
                        nombre = input("Nombre: ")
                        cantidad = input("Cantidad: ")
                        while True:
                            if cantidad.isdigit():
                                cantidad=int(cantidad)
                                break

                            else:
                                print(f"{cantidad} no es un número, porfavor inserta un número entero ")
                                cantidad = input("Cantidad: ")

                        unidad_medida = "unidades"
                        requisitos_seguridad = input("Requisitos de Seguridad: ")
                        umbral_critico = input("Umbral Crítico: ")
                        while True:
                            if umbral_critico.isdigit():
                                umbral_critico=int(umbral_critico)
                                break
                            else:
                                print(f"{umbral_critico} valor no aceptado, porfavor inserta un número")
                                umbral_critico=input("Umbral Critico: ")

                        while True:
                            fecha_mantenimiento_str = input("Fecha del último mantenimiento (DD/MM/AAAA): ")
                            try:
                                fecha_mantenimiento = datetime.strptime(fecha_mantenimiento_str, "%d/%m/%Y")
                                break
                            except ValueError:
                                print(
                                    f"'{fecha_mantenimiento_str}' no es un valor aceptado. Por favor, introduce una fecha válida (DD/MM/AAAA).")

                        estado = input("Estado del Equipo de Seguridad: ")

                        if tipo_equipo == "1":
                            ubicacion = input("Introduce la ubicación del Equipo de Seguridad: ")
                            certificado=input("Introduce el certificado del Equipo de Seguridad: ")



                            nuevo_item = EquipoSeguridad(id_item, nombre, cantidad,
                                                         requisitos_seguridad, umbral_critico,fecha_mantenimiento, ubicacion, certificado,estado)
                            self.gestorInventario.agregar_item(nuevo_item)
                            print("Item añadido con éxito.")


                        if tipo_equipo=="2":
                            tipo_analisis = input("Tipo de Análisis: ")

                            while True:
                                entrada = input("Introduce la precision del Instrumento Analítico (%): ")
                                try:
                                    precision = int(entrada)
                                    if 1<=precision<=100:
                                        break
                                    else:
                                        print("Por favor escoja un nivel válido (1-100)")

                                except ValueError:
                                    print(f"{entrada} no es un número válido. Por favor solo utiliza dígitos ")

                            nuevo_item = InstrumentoAnalitico(id_item, nombre, cantidad, unidad_medida,
                                                         requisitos_seguridad, umbral_critico,
                                                         fecha_mantenimiento,tipo_analisis,precision)
                            self.gestorInventario.agregar_item(nuevo_item)
                            print("Item añadido con éxito.")

                elif opcion=="3":
                    print(">BORRAR ITEM")
                    id_borrar= input(("Introduce el Id del Item a borrar:"))
                    self.gestorInventario.borrar_item(id_borrar)

                elif opcion =="4":
                    print(">> Registro de Uso")
                    id_uso=input("Introduce el ID del item a usar: ")

                elif opcion == "5":
                    print(">>Aumentar Stock")
                    id_uso=input("Introduce el ID del item a aumentar: ")
                elif opcion == "6":
                    ejecutando_sistema = False

                else:
                    print("Introduce una opción válida")

        menu()

