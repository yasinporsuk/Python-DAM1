class Empleado:
    def __init__(self, dni, nombre):
        self.dni = dni
        self.nombre = nombre

    def mostrar(self, dni, nombre):
        print("el dni es: ", dni)
        print("el nombre es: ", nombre)


class EmpleadoJefe:
    def __init__(self, dni, nombre, departamento):
        self.dni = dni
        self.nombre = nombre
        self.departamento = departamento

    def mostrar(self):
        print(self.dni, self.nombre, self.departamento)


def main():
    jefe1 = EmpleadoJefe(270809, "juanjo", "ventas")
    jefe1.mostrar()

main()

