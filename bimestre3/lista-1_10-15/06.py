# escreva um programa que leia um arquivo, gerando um novo arquivo com o mesmo conteúdo,
# porém com todas as vogais convertidas para maiúsculas
# os nomes dos arquivos serão fornecidos, via teclado, pelo usuário
def vowelsUpper(file_input, file_output):
    with open(file_input, "r") as file:
        vowels = "aeiou"
        vowels_upper = ""

        content = file.read()
        for i in content:
            if i.lower() in vowels:
                vowels_upper += i.upper()
            else:
                vowels_upper += i.lower()

    with open(file_output, "w") as file:
        file.write(vowels_upper)

    with open(file_output, "r") as file:
        print(file.read())

file_input = input("Insira o nome do arquivo de entrada: ")
file_output = input("Insira o nome do arquivo de saída: ")
print()
vowelsUpper(file_input, file_output)
