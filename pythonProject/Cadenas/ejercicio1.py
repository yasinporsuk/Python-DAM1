# Realizar la carga de dos cadenas de caracteres. Indicar si son iguales o no y mostrarlas ordenadas
# alfabéticamente
cadena1 = input("ingrese cadena1")
cadena2 = input("ingrese cadena2")
lista = (cadena1, cadena2)
ordenado = sorted(lista)

if cadena1 == cadena2:
    print("son iguales")
else:
    print("no son iguales")

print(ordenado)


