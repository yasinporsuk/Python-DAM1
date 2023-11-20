def obtener_codigo_mes():
    codigo_valido = False
    codigo_mes = None
    while not codigo_valido:
        codigo_mes = int(input("ingrese codigo mes 1-12"))
        if 1 <= codigo_mes <= 12:
            codigo_valido = True
        else:
            print("error kod no valido")
            
    return codigo_mes


codigo_valido = obtener_codigo_mes()
print(f"ha ingresado el codgio de mes válido: {codigo_valido}")
