
"""Definimos la clase Auditorio, que lo unico que hace es tener 2 procesos, registrar el uso y ver el historial de uso
estos datos se guardan en una lista "Historial de uso" """
class Auditoria:
    def registar_uso(self,usuario,cantidad,motivo):
        registro= f"Usuario {usuario} | Retiró {cantidad} | Motivo {motivo}"
        self.historial_uso.append(registro)
        print(f"Registro Guardado: {registro}")


    def ver_historial(self):
        print(f"Historial de Auditoría: {self.nombre}")
        if not self.historial_uso:
            print("No existe historial de uso")

        else:
            for registro in self.historial_uso:
                print(f"-{registro}")

