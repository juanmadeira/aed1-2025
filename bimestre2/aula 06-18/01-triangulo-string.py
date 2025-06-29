# Formar um triângulo a partir de uma palavra
palavra = str(input("Insira uma palavra: "))
triangulo = ""

i = 0
while i < len(palavra):
    triangulo += palavra[i]
    print(triangulo)
    i += 1
