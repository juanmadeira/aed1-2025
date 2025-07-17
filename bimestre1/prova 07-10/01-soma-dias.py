# Crie um programa em Python que leia uma data inicial e um número de dias.
# Calcule e escreva a data correspondente ao número de dias. Por exemplo:
# 01/01/2024    55      25/02/2024
# 01/01/2024    150     31/5/2024
# 01/01/2024    400     5/2/2025
# Não precisa considerar o ano bissexto, ou seja, pode considerar que todo fevereiro tem 28 dias.

dia = int(input("Insira o dia: "))
while dia > 31 or dia < 1:
    int(input("O dia não pode ser maior que 31 ou menor que 1. Insira o dia: "))

mes = int(input("Insira o mês: "))
while mes > 12 or mes < 1:
    int(input("O dia não pode ser maior que 12 ou menor que 1. Insira o mês: "))

ano = int(input("Insira o ano: "))

intervalo = int(input("Insira o número de dias para ser considerado como intervalo: "))

if mes == 2:
    if dia + intervalo > 28:
        dia = dia + intervalo - 28
        mes += 1
    else:
        dia = dia + intervalo

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if intervalo > 31:
        while intervalo > 31:
            mes += 1
            if mes > 12:
                ano += 1
                mes = 1
            intervalo -= 31
        dia = dia + intervalo
    else:
        dia = dia + intervalo

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia + intervalo > 30:
        dia = dia + intervalo - 30
        mes += 1
    else:
        dia = dia + intervalo

if mes == 12 and (dia + intervalo > 31):
    ano += 1

print(f"{dia}/{mes}/{ano}")
