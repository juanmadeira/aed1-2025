# Peça uma frase e uma letra.
# Conte quantas vezes essa letra aparece na frase

frase = input("Insira uma frase: ")
letra = input("Insira uma letra: ")
soma = 0

i = 0
while i < len(frase):
    if frase[i] == letra:
        soma += 1
    i += 1

print(f"\nA letra \"{letra}\" aparece {soma} vezes na frase \"{frase}\".")
