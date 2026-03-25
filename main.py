from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from clases.consumibles.clase_consumible import Consumible
from clases.consumibles.clase_materialBiologico import MaterialBiologico
from clases.consumibles.reactivo_critico import ReactivoCritico
from clases.equipos.clase_equipoSeguridad import EquipoSeguridad
from clases.equipos.clase_intrumentoAnalitico import InstrumentoAnalitico
from clases.inventario.clase_sistemaLaboratorio import SistemaLaboratorio

if __name__ == "__main__":

    app = SistemaLaboratorio()

    print(">> Preparando base de datos inicial de prueba...\n")



    # 3. REACTIVOS CRÍTICOS (Herencia Múltiple: ReactivoQuimico + Auditoria)
    crit_1 = ReactivoCritico("RC-01", "Cianuro de Sodio", 500, "g", "Traje Hazmat", 50, "2025-10-31", "L-99", "Extremo")


    lista_inicial = []

    for objeto in lista_inicial:
        app.gestorInventario.agregar_item(objeto)
    if len(lista_inicial)==1:
        print(f"\n Base de datos inicial cargada con {len(lista_inicial)} elemento.\n")
    else:
        print(f"\n Base de datos inicial cargada con {len(lista_inicial)} elementos.\n")

    app.iniciar()