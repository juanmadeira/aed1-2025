# faça um programa que leia dois arquivos, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos
# (o conteúdo do primeiro seguido do conteúdo do segundo arquivo).

with open("05.txt", "r") as file:
    file1 = file.read()
with open("06.txt", "r") as file:
    file2 = file.read()

with open("07.txt", "w") as file:
    file3 = file1 + file2
    file.write(file3)

with open("07.txt", "r") as file:
    print(file.read())
