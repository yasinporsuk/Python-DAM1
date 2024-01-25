def funcion(cadena):
    ultima_posicion = len(cadena)-1
    for i in range(ultima_posicion // 2+1):
        if cadena[i] != cadena[ultima_posicion-i]:
            return False
    return True


ingreso = input("ingrese cadena: ")
resultado = funcion(ingreso)
print(resultado)