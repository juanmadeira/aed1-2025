# faça um programa que leia um arquivo texto
# crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por um * (asterisco).
with open("01.txt", "r") as file:
    vowels = "aeiou"
    vowels_censored = ""

    content = file.read()
    for i in content:
        if i.lower() in vowels:
            vowels_censored += "*"
        else:
            vowels_censored += i

with open("05.txt", "w") as file:
    file.write(vowels_censored)

with open("05.txt", "r") as file:
    print(file.read())
