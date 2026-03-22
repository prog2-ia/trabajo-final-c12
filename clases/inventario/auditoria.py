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

