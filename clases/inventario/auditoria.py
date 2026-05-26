
"""Definimos la clase Auditorio, que lo unico que hace es tener 2 procesos, registrar el uso y ver el historial de uso
estos datos se guardan en una lista "Historial de uso" """
class Auditoria:
    def __init__(self)->None:
        if not hasattr(self, 'historial_uso'):
            self.historial_uso = []


    def registrar_uso(self,usuario,cantidad,motivo)->None:
        if not hasattr(self, 'historial_uso'):
            self.historial_uso = []

        registro= f"Usuario {usuario} | Retiró {cantidad} | Motivo {motivo}"
        self.historial_uso.append(registro)
        print(f"Registro Guardado: {registro}")


    def ver_historial(self)->None:
        print(f"Historial de Auditoría: {self.nombre}")
        if not self.historial_uso:
            print("No existe historial de uso")

        else:
            for i,registro in enumerate( self.historial_uso,1):
                print(f"-{registro}")

# guarda el historial en un fichero de texto
    def guardar_historial_txt(self, ruta: str) -> None:
        fichero = open(ruta, "w", encoding="utf-8")
        fichero.write(f"Historial de: {self.nombre}\n")
        for registro in self.historial_uso:
            fichero.write(registro + "\n")
        fichero.close()
        print(f"Historial guardado en {ruta}")

    # carga el historial desde un fichero de texto
    def cargar_historial_txt(self, ruta: str) -> None:
        try:
            fichero = open(ruta, "r", encoding="utf-8")
            lineas = fichero.readlines()
            fichero.close()
            self.historial_uso = []
            for linea in lineas:
                if "|" in linea:
                    self.historial_uso.append(linea.strip())
            print(f"Historial cargado desde {ruta}")
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontro el fichero {ruta}")