# implemente transpor(matriz) que receba uma matriz (lista de listas) e retorne sua transposta
# exemplo:
# entrada: [[1,2,3],[4,5,6]]
# saída: [[1,4],[2,5],[3,6]]

def transpor(matriz):
    transposta = []
    for i in range(len(matriz[0])):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        transposta.append(linha)
    return transposta


i = 0
j = 0
linha = []
matriz = []
while True:
    linha.append(input(f"Insira o elemento {i} da linha {j} (digite \"linha\" para ir para a próxima linha ou \"fim\" para encerrar a matriz): "))
    i += 1
    if linha[-1] == "linha":
        linha.pop(-1)
        matriz.append(linha)
        linha = []
        i = 0
        j += 1
    elif linha[-1] == "fim":
        linha.pop(-1)
        matriz.append(linha)
        break

# professor(a), entendo que a existência do bloco de código abaixo é tão inútil quanto a minha capacidade de resolver esses exercícios,
# porém, pelo capricho, resolvi testar algo que eu desconhecia.
# atesto que não foi utilizada nenhuma _LLM_ no desenvolvimento desse código.

try:
    transposta = transpor(matriz)
    print(f"\nMatriz original:\n{matriz}")
    print(f"\nMatriz transposta:\n{transposta}\n")
except IndexError:
    print("\nERRO!!!!!! A matriz é inválida.\n")
    pass
