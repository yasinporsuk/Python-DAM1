class Volumen:
    def __init__(self):
        self.nivel = 3
        print("nivel", self.nivel)

    def subir(self):
        self.nivel += 1
        if self.nivel > 10:
            self.nivel = 10
        print("nivel", self.nivel)

    def bajar(self):
        self.nivel -= 1
        if 0 > self.nivel:
            self.nivel = 0
        print("nivel", self.nivel)

    def silenciar(self):
        self.nivel = 0
        print("nivel", self.nivel)

class Graves(Volumen):
    pass


control_graves = Graves()
control_graves.subir()

