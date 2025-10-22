# faça um programa em python que leia um arquivo texto e um caractere
# mostre na tela quantas vezes este caractere ocorre no arquivo
def charCount(file, char):
    with open("01.txt", "r") as file:
        qtd = 0
        content = file.read()
        for i in content:
            if i.upper() == char.upper():
                qtd += 1
        return qtd


file = "01.txt"
char = input("Insira um caractere: ")
print(charCount(file, char))
