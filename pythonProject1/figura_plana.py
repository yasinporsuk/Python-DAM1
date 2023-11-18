class Figura_plana:
    def __init__(self, base, altura):

     def area(self):
         return self.base * self.altura


class Rectangulo(Figura_plana):
    def __init__(self, base, altura):
        Figura_plana.__init__(self, base, altura)


    def mostrar_datos(self):
        Figura_plana.mostrar_datos(self)

    def