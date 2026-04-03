from clases.inventario.clase_sistemaLaboratorio import SistemaLaboratorio

if __name__ == "__main__":

    app = SistemaLaboratorio()

    print(">> Preparando base de datos inicial de prueba...\n")


    lista_inicial = []

    for objeto in lista_inicial:
        app.gestorInventario.agregar_item(objeto)
    if len(lista_inicial)==1:
        print(f"\n Base de datos inicial cargada con {len(lista_inicial)} elemento.\n")
    else:
        print(f"\n Base de datos inicial cargada con {len(lista_inicial)} elementos.\n")

    app.iniciar()