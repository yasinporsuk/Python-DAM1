

def esprimo(numero):
    if numero < 2:
        return False
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False

        return True


num = int(input("introduzca numero si es primo o no"))
resultado = esprimo(num)
print("Es primo?", resultado)
