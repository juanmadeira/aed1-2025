# Peça para o usuário digitar frases até que ele digite a palavra "sair"
# Diga quantas frases foram digitadas

frase = input("Insira uma frase: ")
frasesQtd = 0

if frase == "sair":
    frasesQtd = 0
else:
    while frase.lower() != "sair":
        frase = ""
        frase = input("Insira uma frase: ")
        frasesQtd += 1

print(f"\nForam digitadas {frasesQtd} frases.")
