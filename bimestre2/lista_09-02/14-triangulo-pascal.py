# crie uma função `triangulo_pascal(n)` que retorne uma lista de listas representando as primeiras `n` linhas do triângulo de Pascal.
# exemplo:
# entrada: 5
# saída: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def triangulo_pascal(n):
    pascal = [[] for _ in range(n)]

    for i in range(n):
        pascal[i] = [1 for _ in range(i + 1)]

    if n > 2:
        i = 2
        while i < (n):
            for j in range(1, len(pascal[i]) - 1):
                pascal[i][j] = pascal[i - 1][j] + pascal[i - 1][j - 1]
            i += 1

    return pascal


n = int(input("Insira o número de linhas: "))
pascal = triangulo_pascal(n)
for linha in pascal:
    print(linha)
