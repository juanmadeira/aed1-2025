# escreva uma função `multiplicar_matrizes(A, B)` que multiplique duas matrizes (validando dimensões) e retorne o resultado
# exemplo:
# entrada: A=[[1,2],[3,4]], B=[[2,0],[1,2]]
# saída: [[4,4],[10,8]]

def multiplicar_matrizes(A, B):
    mult = []
    for i in range(len(A)):
        linha = []
        for j in range(len(B[i])):
            n = 0
            for k in range(len(A[j])):
                n += int(A[i][k]) * int(B[k][j])
            linha.append(n)
        mult.append(linha)

    return mult


matrizes = []
for k in range(2):
    i = 0
    j = 0
    linha = []
    matriz = []
    if k == 0:
        print("\nMatriz A\n")
    else:
        print("\nMatriz B\n")
    while True:
        linha.append(input(f"Insira o elemento {i} da linha {j} (digite \"linha\" para ir para a próxima linha ou \"fim\" para encerrar a matriz): "))
        i += 1
        if linha[-1] == "linha" or linha[-1] == "l":
            linha.pop(-1)
            matriz.append(linha)
            linha = []
            i = 0
            j += 1
        elif linha[-1] == "fim" or linha[-1] == "f":
            linha.pop(-1)
            matriz.append(linha)
            break
    matrizes.append(matriz)

A = matrizes[0]
B = matrizes[1]

try:
    mult = multiplicar_matrizes(A, B)
    print("\nMatriz A")
    for linha in A:
        print(linha)
    print("\nMatriz B")
    for linha in B:
        print(linha)
    print("\nResultado da multiplicação:")
    for linha in mult:
        print(linha)
except IndexError:
    print("\nERRO!!!!!! Pelo menos uma das matrizes inseridas é inválida.\n")
    pass
