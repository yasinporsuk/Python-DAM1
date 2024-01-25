class Empleado:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def mostrar(self):
        print("el dni es: ", self.dni)
        print("el nombre es: ", self.nombre)


class EmpleadoJefe(Empleado):
    def __init__(self, dni, nombre, departamento):
        super().__init__(dni, nombre)
        self.departamento = departamento

    def mostrar(self):
        super().mostrar()
        print("Su dpto es: ", self.departamento)


def main():
    jefe1 = EmpleadoJefe(270809, "juanjo", "ventas")
    jefe1.mostrar()


main()

