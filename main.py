from clases.consumibles.clase_reactivoQuimico import ReactivoQuimico
from clases.consumibles.clase_materialBiologico import MaterialBiologico
from clases.consumibles.reactivo_critico import ReactivoCritico
from clases.equipos.clase_equipoSeguridad import EquipoSeguridad
from clases.equipos.clase_intrumentoAnalitico import InstrumentoAnalitico
from clases.inventario.clase_sistemaLaboratorio import SistemaLaboratorio

if __name__ == "__main__":

    app = SistemaLaboratorio()

    print(">> Preparando base de datos inicial de prueba...\n")

    # 1. REACTIVOS QUÍMICOS (Herencia Simple desde Consumible)
    req_1 = ReactivoQuimico("RQ-01", "Ácido Sulfúrico", 2500, "ml", "Campana y Guantes", 500, "2026-05-10", "L-882",
                            "H2SO4", "Alto")
    req_2 = ReactivoQuimico("RQ-02", "Cloruro de Sodio", 5000, "g", "Ninguno", 1000, "2028-01-01", "L-112", "NaCl",
                            "Bajo")


    # 2. MATERIAL BIOLÓGICO (Herencia Simple desde Consumible)
    bio_1 = MaterialBiologico("MB-01", "Cultivo E. Coli", 50, "ml", "Cabina Bioseguridad", 10, "2024-12-01", "Cepa-K12",
                              "Bacteria", "BSL-1",temperatura_almacenamiento= 32)
    bio_2 = MaterialBiologico("MB-02", "Suero Humano", 200, "ml", "Guantes y Lentes", 20, "2025-03-15", "L-SH99",
                              "Fluido", "BSL-2",temperatura_almacenamiento= 25)


    # 3. REACTIVOS CRÍTICOS (Herencia Múltiple: ReactivoQuimico + Auditoria)
    crit_1 = ReactivoCritico("RC-01", "Cianuro de Sodio", 500, "g", "Traje Hazmat", 50, "2025-10-31", "L-99", "Extremo")
    crit_2 = ReactivoCritico("RC-02", "Ácido Fluorhídrico", 1000, "ml", "Campana Especial", 100, "2024-11-20", "L-44",
                             "Extremo y Corrosivo")


    # 4. EQUIPOS DE SEGURIDAD (Herencia Simple desde Equipamiento)
    seg_1 = EquipoSeguridad("ES-01", "Extintor ABC", 1, "Revisión mensual", 1, "2024-01-15", "Pasillo Principal",
                            "NOM-154", "Operativo")
    seg_2 = EquipoSeguridad("ES-02", "Ducha de Emergencia", 1, "Purgar semanalmente", 1, "2024-04-01", "Laboratorio 2",
                            "ANSI-Z358", "Operativo")


    # 5. INSTRUMENTOS ANALÍTICOS (Herencia Simple desde Equipamiento)
    inst_1 = InstrumentoAnalitico("IA-01", "Balanza Analítica", 2, "Mesa Antivibración", 1, "2024-02-28", "Cuantitativo",
                                  "0.0001g", "Operativo")
    inst_2 = InstrumentoAnalitico("IA-02", "Espectrofotómetro", 1, "Corriente regulada", 1, "2023-11-10",
                                  "Cuantitativo", "190-1100nm", "Operativo")

    lista_inicial = [req_1, req_2, bio_1, bio_2, crit_1, crit_2, seg_1, seg_2, inst_1, inst_2]

    for objeto in lista_inicial:
        app.gestorInventario.agregar_item(objeto)

    print("\n✅ Base de datos inicial cargada con 10 elementos.\n")

    app.iniciar()