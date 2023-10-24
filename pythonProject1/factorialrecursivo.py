def numfactorial(num):
    if num == 0 or num == 1:
        resultado = 1
    elif num>1:
        resultado = num * numfactorial(num-1)
    return resultado

def main():
    num = int(input("introduzca un numero "))
    print(numfactorial(num))

main()
