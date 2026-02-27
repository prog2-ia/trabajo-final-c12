class Coche:
    def __init__(self, marca, modelo, anyo, color):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.color = color
        self.en_marcha = False
        self.velocidad = 0
        self.velocidad_maxima = 200

    # 🔷 Métodos de control
    def arrancar(self):
        print("Arrancando el coche...")
        self.en_marcha = True

    def parar(self):
        print("Parando el coche...")
        self.en_marcha = False
        self.velocidad = 0

    def acelerar(self, incremento):
        if not self.en_marcha:
            print("El coche está apagado")
            return

        self.velocidad += incremento

        if self.velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            print("Ha alcanzado la velocidad máxima")

        print(f"Acelerando a {self.velocidad} km/h")

    def frenar(self, decremento):
        if not self.en_marcha:
            print("El coche está apagado")
            return

        self.velocidad -= decremento

        if self.velocidad < 0:
            self.velocidad = 0

        print(f"Frenando a {self.velocidad} km/h")

    # 🔷 Métodos especiales (muy recomendados)
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.color}: ({self.anyo})"

    def __repr__(self):
        return (
            f'Coche(marca="{self.marca}", '
            f'modelo="{self.modelo}", '
            f"anyo={self.anyo}, "
            f'color="{self.color}")'
        )