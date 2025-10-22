# faça um programa em python que leia um arquivo texto, e mostre na tela o total de vogais,
# o total de consoantes e o total de caracteres que não são nem vogais e nem consoantes contidos neste arquivo
with open("01.txt", "r") as file:
    vogais = 0
    consoantes = 0
    outros_caracteres = 0

    vogais_str = "aeiou"
    consoantes_str = "bcdfghjklmnpqrstvwxyz"

    content = file.read()
    for i in content:
        if i.lower() in vogais_str:
            vogais += 1
        elif i.lower() in consoantes_str:
            consoantes += 1
        else:
            outros_caracteres += 1

print(content)
print(f"Quantidade de vogais: {vogais}")
print(f"Quantidade de consoantes: {consoantes}")
print(f"Quantidade de outros caracteres: {outros_caracteres}")
