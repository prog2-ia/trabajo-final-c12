from clases.equipos.clase_equipoSeguridad import EquipoSeguridad
from clases.equipos.clase_instrumentoAnalitico import InstrumentoAnalitico
from clases.inventario.clase_gestorInventario import GestorInventario
from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from clases.consumibles.clase_materialBiologico import MaterialBiologico
from clases.consumibles.reactivo_quimico_critico import ReactivoQuimicoCritico
from clases.consumibles.material_biologico_critico import MaterialBiologicoCritico
from datetime import datetime


class SistemaLaboratorio:
    def __init__(self)->None:
        self.gestorInventario = GestorInventario()

    def iniciar(self)->None:
        print("=" * 50)
        print("Iniciando el sistema de almacenamiento del laboratorio")
        print("=" * 50)
        self.gestorInventario.cargar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")

        def menu()->None:
            # Variable para controlar el bucle principal del menú
            ejecutando_sistema = True

            while ejecutando_sistema:
                print("\nBienvenido al Sistema de almacenamiento del Laboratorio, escoja una acción (1,2,3,4,5,6): ")
                print(
                    " 1: Mostrar Inventario\n 2: Añadir Item\n 3: Borrar Item\n 4: Registrar uso de un Item\n 5: Aumentar Stock\n 6: Salir del Sistema")

                opcion = input("Introduce tu acción elegida: ")

                if opcion not in ["1","2","3","4","5","6"]:
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
                        item_existente = self.gestorInventario.buscar_item_id(id_item)

                        if item_existente is not None:
                            print(f"Error: Ya existe un ítem registrado con el ID '{id_item}' ({item_existente.nombre}).")
                            print("Si desea añadir más cantidad, utiliza la opción 5 (Aumentar Stock).")
                            continue
                        nombre = input("Nombre: ")

                        while True:
                            try:
                                cantidad = int(input("Cantidad: "))
                                break

                            except ValueError:
                                print("Porfavor ingrese un número")

                        unidad_medida = input("Unidad de Medida: ")
                        requisitos_seguridad = input("Requisitos de Seguridad: ")

                        while True:
                            try:
                                umbral_critico = int(input("Umbral Crítico: "))
                                break

                            except ValueError:
                                print("Porfavor ingresa un numero entero")

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


                            respuesta = input("¿Este reactivo es de alto peligro/crítico? (s/n): ").strip().lower()

                            if respuesta == 's':

                                nivel_peligro = int(input("Introduce el nivel de peligro (1-5): "))

                                nuevo_reactivo_critico = ReactivoQuimicoCritico(id_item, nombre, cantidad, unidad_medida,
                                                                    requisitos_seguridad, umbral_critico,
                                                                    fecha_caducidad, lote, formula_quimica,
                                                                    nivel_toxicidad, nivel_peligro)
                                self.gestorInventario.agregar_item(nuevo_reactivo_critico)
                                self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")
                            else:

                                nuevo_reactivo = ReactivoQuimico(id_item, nombre, cantidad, unidad_medida,
                                                             requisitos_seguridad, umbral_critico,
                                                             fecha_caducidad, lote, formula_quimica,
                                                             nivel_toxicidad)
                                self.gestorInventario.agregar_item(nuevo_reactivo)
                                self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")


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




                            respuesta = input("¿Este reactivo es de alto peligro/crítico? (s/n): ").strip().lower()

                            if respuesta == 's':

                                nivel_peligro = int(input("Introduce el nivel de peligro (1-5): "))

                                nuevo_material_critico = MaterialBiologicoCritico(id_item, nombre, cantidad, unidad_medida,
                                                                requisitos_seguridad, umbral_critico,
                                                                fecha_caducidad, lote,tipo_muestra,nivel_bioseguridad,temperatura_almacenamiento
                                                                ,nivel_peligro)
                                self.gestorInventario.agregar_item(nuevo_material_critico)
                                self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")
                            else:

                                nuevo_material = MaterialBiologico(id_item, nombre, cantidad, unidad_medida,
                                                         requisitos_seguridad, umbral_critico,
                                                         fecha_caducidad, lote,tipo_muestra,nivel_bioseguridad,temperatura_almacenamiento)
                                self.gestorInventario.agregar_item(nuevo_material)
                                self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")



                    if tipo_item == "2":
                        print("¿Que tipo de Equipamiento quieres registrar?\n 1: Equipo de Seguridad | 2: Instrumento Analítico")
                        while True:
                            tipo_equipo = input("Introduce tu elección: ")
                            if tipo_equipo in ["1","2"]:
                                break
                            else:
                                print("Introduce un tipo de equipo correcto")



                        id_item = input("Id Item: ")
                        item_existente = self.gestorInventario.buscar_item_id(id_item)

                        if item_existente is not None:
                            print(f"Error: Ya existe un ítem registrado con el ID '{id_item}' ({item_existente.nombre}).")
                            print("Si desea añadir más cantidad, utiliza la opción 5 (Aumentar Stock).")
                            continue
                        nombre = input("Nombre: ")

                        while True:
                            try:
                                cantidad = int(input("Cantidad: "))
                                break

                            except ValueError:
                                print("Porfavor ingresa solo número enteros")

                        requisitos_seguridad = input("Requisitos de Seguridad: ")

                        while True:
                            try:
                                umbral_critico = int(input("Umbral Crítico: "))
                                break
                            except ValueError:
                                print("Valor Incorrecto, inserta un número entero ")

                        fecha_mantenimiento = input("Fecha Mantenimiento: ")

                        estado = input("Estado del Equipo de Seguridad: ")

                        if tipo_equipo == "1":
                            ubicacion = input("Introduce la ubicación del Equipo de Seguridad: ")
                            certificado=input("Introduce el certificado del Equipo de Seguridad: ")



                            nuevo_item = EquipoSeguridad(id_item, nombre, cantidad,
                                                         requisitos_seguridad, umbral_critico,fecha_mantenimiento, ubicacion, certificado,estado)
                            self.gestorInventario.agregar_item(nuevo_item)
                            self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")
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

                            nuevo_instrumento = InstrumentoAnalitico(id_item, nombre, cantidad,
                                                                requisitos_seguridad, umbral_critico,
                                                                fecha_mantenimiento,tipo_analisis,precision)

                            self.gestorInventario.agregar_item(nuevo_instrumento)
                            self.gestorInventario.guardar_inventario_bin("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/inventario.dat")
                            print("Item añadido con éxito.")

                elif opcion=="3":
                    print(">BORRAR ITEM")
                    id_borrar= input("Introduce el Id del Item a borrar:")
                    self.gestorInventario.borrar_item(id_borrar)

                elif opcion =="4":

                    print(">> Registro de Uso")
                    id_uso=input("Introduce el ID del item a usar: ")

                    item=self.gestorInventario.buscar_item_id(id_uso)

                    if item is None:
                        print("Item no encontrado/Item inexistente")
                    else:
                        if hasattr(item,"consumir_stock_critico"):
                            print(f"ALERTA!!!, EL SIGUIENTE ITEM {item.nombre} REQUIERE AUDITORÍA")
                            try:
                                cantidad=int(input("Introduce la cantidad a retirar:"))
                                usuario= input("Introduce tu nombre/usuario: ")
                                motivo= input("Introduce el motivo de retiro: ")

                                item.consumir_stock_critico(cantidad,usuario,motivo)
                                item.guardar_historial_txt("/home/alvaro-imanol-castillo-romero/PycharmProjects/trabajo-final-c12/clases/inventario/historial_uso.txt")
                            except ValueError as e:
                                print(f"Error en el siguiente dato: {e}")


                        elif hasattr(item,"consumir_stock"):
                            try:
                                cantidad=int(input("Introduce la cantidad a usar:"))
                                item.consumir_stock(cantidad)
                                print(f"Se han consumido {cantidad} {item.unidad_medida} de {item.nombre}")
                            except ValueError as e:
                                print(f"Error en el siguiente dato: {e}")




                elif opcion == "5":
                    print("\n>> AUMENTAR STOCK")
                    id_aumentar = input("Introduce el ID del ítem a aumentar: ")


                    item = self.gestorInventario.buscar_item_id(id_aumentar)

                    if item is None:
                        print(f"Error: No se ha encontrado ningún ítem con ID {id_aumentar}")
                    else:

                        print(f"Ítem encontrado: {item.nombre}")
                        print(
                            f"Stock actual: {item.cantidad} {item.unidad_medida} | Umbral crítico: {item.umbral_critico}")

                        try:
                            cantidad_anadir = int(input("¿Cuántas unidades deseas añadir al stock?: "))

                            if cantidad_anadir <= 0:
                                print("Error: La cantidad a añadir debe ser mayor a 0.")
                            else:

                                item.cantidad += cantidad_anadir

                                print(f"¡¡¡¡¡Stock actualizado con éxito!!!!!")
                                print(f"Nuevo stock de {item.nombre}: {item.cantidad} {item.unidad_medida}")

                        except ValueError:
                            print("Error: Por favor, introduce un número válido, sin letras ni símbolos.")
                elif opcion == "6":
                    ejecutando_sistema = False

                else:
                    print("Introduce una opción válida")

        menu()

