# Remova todos os espaços de uma frase lida

frase = input("Insira uma frase: ")
fraseNova = ""

i = 0
while i < len(frase):
    if frase[i] != " ":
        fraseNova += frase[i]
    i += 1

print(f"\n{fraseNova}")
