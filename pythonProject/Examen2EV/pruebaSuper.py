class Padre:
    def saludar(self):
        print("Hola desde la clase Padre")

class Hijo(Padre):
    def saludar(self):
        print("hola desde hijo")


hijo = Hijo()
hijo.saludar()