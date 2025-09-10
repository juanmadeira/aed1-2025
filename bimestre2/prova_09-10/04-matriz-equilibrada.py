# uma matriz pode ser considerada equilibrada quando
# a soma dos itens de suas linhas (independentes) é igual a soma dos itens das suas colunas.
# crie uma função que receba uma matriz (representada como lista de listas)
# retorne True ou False caso seja ou não uma matriz equilibrada.

def matrizEquilibrada(matriz):
    linhas = [[] for _ in range(len(matriz))]
    colunas = [[] for _ in range(len(matriz))]

    if len(matriz) == 1:
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[0][i]
        if soma == 0:
            return True
        else:
            return False

    for i in range(len(matriz)):
        somaLinhas = 0
        somaColunas = 0
        for j in range(len(matriz[i])):
            somaLinhas += int(matriz[i][j])
            somaColunas += int(matriz[j][i])
        linhas[i].append(somaLinhas)
        colunas[i].append(somaColunas)

    if linhas == colunas:
        return True
    else:
        return False


# matriz = [[0, 0, 0, 0]]  # deve retornar True
# matriz = [[1, 2, 3, 4]]  # deve retornar False
matriz = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]  # deve retornar True
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # deve retornar False

print("\nMatriz original:")
for linha in matriz:
    print(linha)

equilibrada = matrizEquilibrada(matriz)
if equilibrada:
    print(f"\nA matriz é equilibrada!\n{equilibrada}")
else:
    print(f"\nA matriz NÃO é equilibrada!\n{equilibrada}")
