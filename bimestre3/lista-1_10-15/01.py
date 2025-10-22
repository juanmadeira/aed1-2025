# faça um programa em python que leia um arquivo texto, e mostre na tela quantas linhas esse arquivo possui.
with open("01.txt", "r") as file:
    content = file.readlines()
    print(len(content))
