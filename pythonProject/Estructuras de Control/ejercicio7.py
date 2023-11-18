rentanual = int(input("Introduzca su renta anual para saber que tramo impuesto le corresponde: "))

if rentanual < 10000:
    print("Le corresponde pagar 5%")
elif (rentanual > 10000) and (rentanual < 20000):
    print("le corresponde pagar 15%")
elif 20000 < rentanual < 35000:
    print("le corresponde 20%")
elif rentanual > 35000 and rentanual < 60000:
    print("le corresponde 30%")
elif rentanual >= 60000:
    print("le corresponde 45%")
