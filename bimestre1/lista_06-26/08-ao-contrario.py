# Leia uma frase e imprima ela ao contrário

frase = input("Insira uma frase: ")
esarf = ""

i = 0
while i < len(frase):
    esarf += frase[len(frase) - i - 1]
    i += 1

print(f"\n{esarf}")
