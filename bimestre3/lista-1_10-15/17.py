# escreva um programa que leia os arquivos ordenados pares.txt e impares.txt,
# e gere um arquivo pareseimpares.txt com todas as linhas dos outros dois arquivos, de forma a preservar a ordem numérica.
# para ler os dados contidos nos arquivos pares.txt e impares.txt, o programa somente poderá utilizar a função readlines().
# a medida que um dado é lido de um dos arquivos de entrada, este já deve ser salvo no arquivo pareseimpares.txt, respeitando a ordem numérica dos dados.
with open("17-pares.txt", "r") as even, open("17-impares.txt", "r") as odd:
    todos = [0, 0]
    while True:
        even_line = even.readline()
        odd_line = odd.readline()

        if not even_line and not odd_line:
            break

        if even_line.strip():
            even_i = int(even_line.strip())
            if even_i < todos[-2]:
                todos.insert(-2, even_i)
            elif even_i < todos[-1]:
                todos.insert(-1, even_i)
            else:
                todos.append(even_i)

        if odd_line.strip():
            odd_i = int(odd_line.strip())
            if odd_i < todos[-2]:
                todos.insert(-2, odd_i)
            elif odd_i < todos[-1]:
                todos.insert(-1, odd_i)
            else:
                todos.append(odd_i)

    del todos[0:2]

with open("17.txt", "w") as file:
    for i in todos:
        file.write(f"{str(i)}\n")

with open("17.txt", "r") as file:
    print(file.read())
