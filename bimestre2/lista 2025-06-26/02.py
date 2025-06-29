# Some números lidos até que a entrada seja zero
# Se o resultado for um número ímpar, multiplique-o por 2
n = 1
soma = 0

while n != 0:
    n = 0
    n = int(input("Insira um número: "))
    soma += n

if soma % 2 != 0:
    soma *= 2

print(f"O resultado é {soma}.")
