while True:
    print("Seleccionar operacion")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Teclear la opcion:"))

    if opcion == 5:
        print("Exiting the calculator")
        break

    if opcion not in (1, 2, 3, 4):
        print("opcion no valida")
        continue

    operando1 = float(input("Introduzca operando1"))
    operando2 = float(input("introduzca operando2"))

    












