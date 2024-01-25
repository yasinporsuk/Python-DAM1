def letradni(digitos_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKEO"
    return letras[digitos_dni % 23]


def main():
    validador = False
    while not validador:
        dni = input("ingresar dni: ")
        if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isascii():
            print("DNI correcto")
            validador = True
        else:
            print("dni no valido")


main()
