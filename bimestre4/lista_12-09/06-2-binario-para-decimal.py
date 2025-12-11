def binario_para_decimal(array_binario):
    decimal = 0
    tamanho = len(array_binario)
    for i in range(tamanho):
        decimal += array_binario[i] * (2 ** (tamanho - 1 - i))
    return decimal

array_binario = [1, 1, 0, 0, 1] 
numero_decimal = binario_para_decimal(array_binario)

print("A representação decimal é:", numero_decimal)