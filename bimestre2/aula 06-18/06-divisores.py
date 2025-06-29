# Leia um número e mostre a soma de todos os seus divisores

n = int(input("Insira um número: "))
soma = 0

i = n
while i > 0:
    if (n % i) == 0:
        soma += i
    i -= 1

print(f"A soma dos divisores de \"{n}\" é igual a \"{soma}\".")
