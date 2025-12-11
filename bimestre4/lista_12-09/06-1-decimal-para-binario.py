def decimal_para_binario(array_binario, decimal):
    if decimal == 0:
        array_binario.append(0)  # caso especial quando o número é zero
    else:
        while decimal > 0:
            resto = decimal % 2
            array_binario.insert(0, resto)  # adiciona ao início do array
            decimal = decimal // 2  # divisão inteira por 2


array_binario = []
numero_decimal = 25

decimal_para_binario(array_binario, numero_decimal)

print("A representação binária é:", array_binario)