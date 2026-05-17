from clases.consumibles.clase_consumible import Consumible
from clases.consumibles.clase_materialBiologico import MaterialBiologico


class MaterialBiologicoCritico(MaterialBiologico):
    def __init__(self):
        super().__init__()
        self.items = []


