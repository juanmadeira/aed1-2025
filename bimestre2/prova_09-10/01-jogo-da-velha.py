# um tabuleiro de jogo de velha pode ser representado por uma matriz na forma de uma lista de listas, com cada lista representando uma linha da matriz
# crie uma função que receba como parâmetro um tabuleiro de jogo da velha e retorne o estado do jogo,
# que pode ser: inacabado, X venceu, O venceu ou Velha.
# observe que não se está pedindo para desenvolver o jogo por completo nem pedir entrada de dados.

def velha(tabuleiro):
    resultado = ""

    espacos = 0
    for i in tabuleiro:
        for j in range(len(i)):
            if i[j] == " ":
                espacos += 1

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:  # diagonal
        jogador = tabuleiro[0][0]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:  # diagonal
        jogador = tabuleiro[0][2]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:  # vertical
        jogador = tabuleiro[0][0]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:  # vertical
        jogador = tabuleiro[0][1]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:  # vertical
        jogador = tabuleiro[0][2]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:  # horizontal
        jogador = tabuleiro[0][0]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:  # horizontal
        jogador = tabuleiro[1][0]
        resultado = f"{jogador} venceu!"
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:  # horizontal
        jogador = tabuleiro[2][0]
        resultado = f"{jogador} venceu!"
    elif espacos > 0:
        resultado = "Jogo inacabado!"
    else:
        resultado = "Deu velha!"

    return resultado


tabuleiro1 = [["X", " ", "O"], [" ", "X", "O"], [" ", " ", "X"]]
tabuleiro2 = [["O", "X", " "], ["O", "X", "X"], ["O", " ", " "]]
tabuleiro3 = [["X", "O", "O"], ["O", "X", "X"], ["X", "X", "O"]]
tabuleiro4 = [["X", " ", "O"], ["O", " ", "X"], ["X", "X", "O"]]

print("\nTabuleiro 1:")
for linha in tabuleiro1:
    print(linha)
print(velha(tabuleiro1))

print("\nTabuleiro 2:")
for linha in tabuleiro2:
    print(linha)
print(velha(tabuleiro2))

print("\nTabuleiro 3:")
for linha in tabuleiro3:
    print(linha)
print(velha(tabuleiro3))

print("\nTabuleiro 4:")
for linha in tabuleiro4:
    print(linha)
print(velha(tabuleiro4))
