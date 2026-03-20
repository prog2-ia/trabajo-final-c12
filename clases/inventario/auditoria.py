

class AuditoriaMIxin:
    def registrar_auditoria(self,accion):

        with open ("auditoria_laboratorio.txt","a") as archivo:
            archivo.write(f"Auditoría- {self.nombre}:{accionS}\n")