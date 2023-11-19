
def calcular_promedio(i):
    suma = sum(i)
    longitud = len(i)
    promedio = suma/longitud
    return promedio


listnums = [30,35]
print(calcular_promedio(listnums))
