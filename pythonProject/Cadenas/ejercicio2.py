# Solicitar la carga por teclado de un string. Mostrar el total de caracteres del string y utilizar las
# funciones explicadas anteriormente (upper, lower y capitalize).

def totalcaracteres(cadena):
    print(cadena.upper())
    print(cadena.lower())
    print(cadena.capitalize())
    return "en total son", len(cadena), "caracteres"


ingreso = input("Ingrese una cadena")
resultado = totalcaracteres(ingreso)
print(resultado)

