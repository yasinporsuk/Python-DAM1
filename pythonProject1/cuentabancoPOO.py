class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, saldo, tipo_interes):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo
        self.tipo_int = tipo_interes

    def vermenu(self):
        print("1. ver datos")
        print("2. consulta saldo")
        print("3. ingresar dinero")
        print("4. sacar dinero")
        print("5. Salir")
        opcionValida = False
        while not opcionValida:
            opcion = int(input("Introduce opcion entre 1 y 5"))
            opcionValida = opcion >= 1 and opcion <= 5
            return opcion

    def realizaroperacion(self):
        salir = False
        while not salir:
            opcion = self.vermenu()
            salir = (opcion == 5)
            if not salir:
                match opcion:
                    case 1:
                        self.verDatos()
                    case 2:
                        print("El saldo de la cuenta es: ", self.saldo)
                    case 3:
                        cantidad = float(input("Cuánto Dinero deseas ingresar: "))
                        self.ingreso(cantidad)
                    case 4:
                        cantidad = float(input("Cuanto Dinero deseas retirar: "))
                        self.reintegro(cantidad)

    def verDatos(self):
        print("El numero de cuenta es: ", self.numero_cuenta)
        print("El titular de la cuenta es: ", self.nombre_titular)
        print("El saldo de la cuenta es: ", self.saldo)
        print("El tipo de interes de la cuenta es: ", self.tipo_int)

    def ingreso(self, cantidad):
        if cantidad <= 0:
            print("error la cantidad debe ser mayor que 0")
        else:
            self.saldo = self.saldo + cantidad

    def reintegro(self, cantidad):
        if cantidad <= 0:
            print("la cantidad debe ser mayor que 0")
        else:
            if cantidad < self.saldo:
                self.saldo = self.saldo - cantidad
            else:
                print("no puedes retirar el dinero mayor al que tienes tu saldo")

    def verDatos(self):
        print("El numero de cuenta es: ", self.numero_cuenta)
        print("El titular de la cuenta es: ", self.nombre_titular)
        print("El saldo de la cuenta es: ", self.saldo)
        print("El tipo de interes de la cuenta es: ", self.tipo_int)

    def ingreso(self, cantidad):
        if cantidad <= 0:
            print("error la cantidad debe ser mayor que 0")
        else:
            self.saldo = self.saldo + cantidad

    def reintegro(self, cantidad):
        if cantidad <= 0:
            print("la cantidad debe ser mayor que 0")
        else:
            if cantidad < self.saldo:
                self.saldo = self.saldo - cantidad
            else:
                print("no puedes retirar el dinero mayor al que tienes tu saldo")


def main():
    cuenta = crear_cuenta()
    cuenta.realizaroperacion()
    cuenta.verDatos()


def crear_cuenta():
    numero_cuenta = input("Introduce el numero de cuenta: ")
    nombre_titular = input("Introduce el nombre del titular: ")
    saldo = int(input("cantidad inicial de la cuenta:"))
    tipo_interes = float(input("Introduce el tipo de interes: "))
    return Cuenta(numero_cuenta, nombre_titular, saldo, tipo_interes)


main()
