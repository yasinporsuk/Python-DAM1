def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    if suma_divisores == numero :
        return True
    else:
        return False



numero_ingresado = int(input("Ingrese un número entero: "))
resultado = es_numero_perfecto(numero_ingresado)

if resultado:
    print(f"{numero_ingresado} es un número perfecto.")
else:
    print(f"{numero_ingresado} no es un número perfecto.")
