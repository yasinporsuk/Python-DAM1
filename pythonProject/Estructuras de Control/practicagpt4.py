def contar_vocales(cadena):
    cuenta_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for caracter in cadena:
        caracter = caracter.lower()

        if caracter in cuenta_vocales:
            cuenta_vocales[caracter] += 1

    return cuenta_vocales


entrada = input("introduzca para saber vocales")
resultado = contar_vocales(entrada)
print(resultado)

