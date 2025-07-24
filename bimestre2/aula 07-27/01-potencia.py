def potencia(base, expoente):
    if expoente == 0:
        return 1
    resultado = base
    i = 1
    while i < expoente:
        resultado = resultado * base
        i += 1
    return resultado


base = int(input("Insira o número da base: "))
expoente = int(input("Insira o número do expoente: "))
print(potencia(base, expoente))
