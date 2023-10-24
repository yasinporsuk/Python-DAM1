validador = ""

while validador != 'si' and validador != 'no':
    validador = input("Desea continuar? si/no : ")

    if validador != 'si' and validador != 'no':
        print("Respuesta no Valida por favor diga si o no")

if validador == 'si':
    print("Continuando...")
else:
    print("Saliendo del programa")






