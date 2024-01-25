
class Cuenta:
    # constructor
    def __init__(self, numero_cuenta, nombre_titular, saldo, tipo_interes):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo
        self.tipo_interes = tipo_interes

    def set_numero_cuenta(self, numero_cuenta):
        self.numero_cuenta = numero_cuenta

    def set_nombre_titular(self, nombre_titular):
        self.nombre_titular = nombre_titular

    def set_saldo(self, saldo):
        self.saldo = saldo

    def set_tipo_interes(self, tipo_interes):
        self.tipo_interes = tipo_interes

    def ingreso(self, cantidad):
        self.saldo += cantidad
        print("nueva cantidad de saldo: ", self.saldo)

    def reintegro(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("reintegro realizado, nuevo saldo: ", self.saldo)
        else:
            print("no tiene suficiente saldo")

    def mostrar_datos(self):
        print(self.numero_cuenta, self.nombre_titular, self.saldo, self.tipo_interes)

    def mostrar_operaciones(self):
        print("Operaciones disponibles:")
        print("1. Consultar saldo")
        print("2. Realizar ingreso")
        print("3. Realizar reintegro")
        print("4. Mostrar datos de la cuenta")
        print("5. Salir de la aplicación")

def main():
    cuenta1 = Cuenta("5543", "Juan Pérez", 1200.0, 2.5)

    continuar = True
    while continuar:
        cuenta1.mostrar_operaciones()
        opcion = int(input("Ingrese el número de la operación que desea realizar: "))

        if opcion == 1:
            print(cuenta1.saldo)
        elif opcion == 2:
            ingreso = int(input("cuanto quiere ingresar: "))
            cuenta1.ingreso(ingreso)
        elif opcion == 3:
            reintegro = int(input("cuanto quiere reintegrar: "))
            cuenta1.reintegro(reintegro)
        elif opcion == 4:
            cuenta1.mostrar_datos()
        elif opcion == 5:
            print("hasta luego!")
            continuar = False


main()

