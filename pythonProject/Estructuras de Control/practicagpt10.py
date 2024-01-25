def procesar_cadena(cadena):
    cadenamayuscula = cadena.upper()
    if len(cadena) % 2 == 0:
        print("es par")
    else:
        print("es impar")
    return cadenamayuscula


cadena_input = input("Ingrese una cadena")
resultado = procesar_cadena(cadena_input)
print(resultado)