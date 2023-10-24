def maximo_comun_divisor(num1, num2):
    if num1 == num2:
        return num1
    elif num1 > num2:
        return maximo_comun_divisor(num1 - num2, num2)
    else:
        return maximo_comun_divisor(num1, num2 - num1)

# tambien se puede hacer de la siguente forma
# while num1 != num2:
#      if (num1 > num2):
#          num1 -= num2
#      else
#           num2 -= num1
# return num1

def main():
    num1 = int(input("introduzca primer numero"))
    num2 = int(input("introduzca segundo numero"))
    resultado = maximo_comun_divisor(num1, num2)
    print("el maximo divisior comun de " ,num1 ,"y" , num2 , "es " , resultado )

main()