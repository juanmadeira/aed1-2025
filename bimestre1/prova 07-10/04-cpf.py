# Um CPF tem 11 dígitos: os 9 primeiros são o número base, os 2 últimos são os dígitos verificadores (DV1 e DV2), calculados da seguinte forma:

# Cálculo do 1º dígito verificador (DV1):
# - Multiplique cada um dos 9 primeiros dígitos pelos pesos 10 a 2, em ordem.
# - Some todos os resultados.
# - Calcule o resto da divisão da soma por 11.
# - Se o resto for 0 ou 1, DV1 é 0.
# - Caso contrário, DV1 = 11 - resto.

# Cálculo do 2º dígito verificador (DV2):
# - Multiplique os 9 dígitos originais + o DV1 pelos pesos 11 a 2, em ordem.
# - Some todos os resultados.
# - Calcule o resto da divisão da soma por 11.
# - Se o resto for 0 ou 1, DV2 é 0.
# - Caso contrário, DV2 = 11 - resto.

# Crie um programa em Python que leia um CPF com apenas números (11 dígitos, sem pontos nem traços), e verifique se ele é válido.
# Exemplo: Entrada = 12345678909
# Cálculo do DV1: (1×10 + 2×9 + 3×8 + 4×7 + 5×6 + 6×5 + 7×4 + 8×3 + 9×2) = 210
# 210 % 11 = 1 → DV1 = 0
# Cálculo do DV2:
# (1×11 + 2×10 + 3×9 + 4×8 + 5×7 + 6×6 + 7×5 + 8×4 + 9×3 + 0×2) = 255
# 255 % 11 = 2 → DV2 = 11-2 = 9
# Resultado: CPF termina em 09 → Válido

cpf = input("Insira o CPF: ")
while len(cpf) != 11:
    cpf = input("O CPF precisa ter 11 dígitos. Insira o CPF: ")

dv1 = 0
i = 0
j = 10
while j > 2:
    while i < 9:
        dv1 += int(cpf[i]) * j
        i += 1
    j -= 1
if (dv1 % 11 == 0) or (dv1 % 11 == 1):
    dv1 = 0
else:
    dv1 = 11 - (dv1 % 11)

dv2 = 0
i = 0
j = 10
while j > 2:
    while i < 9:
        dv2 += int(cpf[i]) * j
        i += 1
    j -= 1
dv2 += dv1 * 2
if (dv2 % 11 == 0) or (dv1 % 11 == 1):
    dv2 = 0
else:
    dv2 = 11 - (dv1 % 11)


if cpf[9] == "0" and cpf[10] == "9":
    print("O CPF é válido!")
else:
    print("O CPF é inválido!")
