# Conte quantas vogais há em uma palavra

palavra = input("Insira uma palavra: ")
vogais = "aeiou"
vogaisQtd = 0

i = 0
while i < len(palavra):
    j = 0
    while j < len(vogais):
        if palavra[i] == vogais[j]:
            vogaisQtd += 1
        j += 1
    i += 1

print(f"\nA palavra {palavra} possui {vogaisQtd} vogais.")
