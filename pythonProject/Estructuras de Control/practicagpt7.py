import random


def juego():
    numero_secreto = random.randint(1, 20)

    while True:
        intento = int(input("Ingresa un numero para adivinar! o ingresa -1 para rendirte"))

        if intento == -1:
            print("te has rendido el numero secreto era: ", numero_secreto)
            break
        if intento == numero_secreto:
            print("Has acertado!")
            break
        elif intento < numero_secreto:
            print("el numero secreto es mayor que eso!")
        else:
            print("El numero secreto es menor que eso!")


juego()


