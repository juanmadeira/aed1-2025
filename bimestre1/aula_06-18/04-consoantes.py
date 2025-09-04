# Leia uma palavra e mostre ela onde:
# Cada consoante foi trocada pela próxima consoante do alfabeto
# Cada vogal foi trocada pelo nº correspondente
# sendo A = 1, E = 2, I = 3, O = 4 e U = 5
palavra = input("Insira uma palavra: ")
palavra = palavra.lower()
palavra2 = ""
consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"

i = 0
while i < len(palavra):
    j = 0
    while j < len(consoantes):
        if palavra[i] == consoantes[j]:
            if consoantes[j] == "z":
                palavra2 += "b"
            else:
                palavra2 += consoantes[j+1]
        j += 1

    j = 0
    while j < len(vogais):
        if palavra[i] == vogais[j]:
            palavra2 += str(j+1)
        j += 1
    i += 1

print(palavra2)

