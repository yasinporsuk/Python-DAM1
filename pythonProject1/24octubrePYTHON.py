def pruebabucle(num):
    acum = 1
    for i in range (1, num + 1):
        acum =  acum * i

    return acum

def main():
    num = int(input("introduzca un numero "))
    print("el resultado es ", pruebabucle(num))

main()
