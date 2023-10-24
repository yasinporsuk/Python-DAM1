def factorial(num):
    if num == 0 or num == 1:
        resultado = 1
    elif num>1:
        resultado = num*factorial(num-1)
    return resultado

factory=factorial(5)
print(factory)
