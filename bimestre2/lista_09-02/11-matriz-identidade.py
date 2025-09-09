# crie uma função `matriz_identidade(n)` que receba um número inteiro `n`
# e retorne uma lista de listas representando uma matriz identidade de tamanho `n`
# exemplo:
# entrada: 3
# saída: [[1,0,0],[0,1,0],[0,0,1]]

def matriz_identidade(n):
    matriz = []
    i = 0
    while i < n:
        linha = []
        for j in range(n):
            linha.append(0)
        linha[i] = 1
        matriz.append(linha)
        i += 1

    return matriz


n = int(input("Insira um número inteiro: "))
matriz = matriz_identidade(n)
for linha in matriz:
    print(linha)
