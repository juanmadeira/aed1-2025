# escreva um programa que leia os arquivos ordenados pares.txt e impares.txt,
# e gere um arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.
# para ler os dados contidos nos arquivos pares.txt e impares.txt, o programa somente poderá utilizar a função readlines().
# a medida que um dado é lido de um dos arquivos de entrada, este já deve ser salvo no arquivo pareseimpares.txt, respeitando a ordem numérica dos dados.
with open("17-pares.txt", "r") as file_even:
    with open("17-impares.txt", "r") as file_odd:
        todos = [0, 0]
        content_even = file_even.readlines()
        content_odd = file_odd.readlines()
        for i, j in zip(content_even, content_odd):
            i = int(i)
            j = int(j)
            if i < todos[-2]:
                todos.insert(-2, i)
            elif i < todos[-1]:
                todos.insert(-1, i)
            else:
                todos.append(i)
            if j < todos[-2]:
                todos.insert(-2, j)
            elif j < todos[-1]:
                todos.insert(-1, j)
            else:
                todos.append(j)

        del todos[0:2]

with open("17.txt", "w") as file:
    for i in todos:
        file.write(f"{str(i)}\n")

with open("17.txt", "r") as file:
    print(file.read())
