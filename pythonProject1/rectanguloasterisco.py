altura = int(input("introduzca una altura"))
base = int(input("introduce una base"))

#utilizamos 2 bucles anidados

for i in range(altura):
    #este bucle imprime la fila de asteriscos
    for j in range(base):
        print("*", end="")
    #saltamos a la siguente fila
    print()
