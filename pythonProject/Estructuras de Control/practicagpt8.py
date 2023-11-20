def verificar_pin():

    intentos = 3
    pin_correcto = 8940

    while intentos > 0:

        pin_ingresado = int(input("ingresa el numero PIN: "))

        if pin_ingresado == pin_correcto:
            print("Pin correcto!")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print("no es correcto, te quedan ", intentos, " intentos")

verificar_pin()