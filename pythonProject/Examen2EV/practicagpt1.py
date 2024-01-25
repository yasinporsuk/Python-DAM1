class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Coche(Vehiculo):
    def __init__(self, marca, modelo, numeropuertas):
        super().__init__(marca, modelo)
        self.numeropuertas = numeropuertas

    def mostrar(self):
        print("datos de coche: ", self.marca, self.modelo, self.numeropuertas)


class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar(self):
        print("datos de moto: ", self.marca, self.modelo, self.cilindrada)


def main():
    coche1 = Coche("seat", "ibiza", "5")
    moto1 = Moto("kawasaki", "ultima", "450")

    moto1.mostrar()
    coche1.mostrar()


main()
