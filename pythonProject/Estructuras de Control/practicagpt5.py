def es_primo(numero):
    if numero < 2:
        return False
    for i in range (2,numero):
        if numero % i == 0:
            return False
    return True

entrada = int(input("ingrese num entero para saber si es primo"))
resultado = es_primo(entrada)
print(resultado)