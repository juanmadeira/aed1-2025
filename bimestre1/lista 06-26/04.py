# Conte quantos números de 1 a 1000 são divisíveis por 7

i = 1
divisiveis = 0

while i <= 1000:
    if i % 7 == 0:
        divisiveis += 1
    i += 1

print(f"{divisiveis} números de 1 a 1000 são divisíveis por 7.")
