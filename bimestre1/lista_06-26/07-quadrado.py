# Leia um caractere e um número n
# Mostre um quadrado nxn com o caractere lido

c = input("Insira um caractere: ")
n = int(input("Insira um número: "))
quadrado = ""

i = 0
while i < n:
    j = 0
    while j < n:
        quadrado += c
        j += 1
    quadrado += "\n"
    i += 1

print(quadrado)
