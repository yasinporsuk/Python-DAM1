def calcular_mcd_recursivo(num1, num2):
    if num2 == 0:
        return num1
    else:
        return calcular_mcd_recursivo(num2, num1 % num2)

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

mcd_resultado = calcular_mcd_recursivo(numero1, numero2)
print(f"El máximo común divisor de {numero1} y {numero2} es: {mcd_resultado}")
