# crie uma função `estatisticas_texto(texto)` que receba uma string e retorne uma lista com:
# - número de palavras,
# - número de caracteres,
# - tamanho médio das palavras,
# - a palavra mais longa.

# exemplo:
# entrada: "Python é divertido"
# saída:
# [['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'], [3, 17, 5.6, 'divertido'}]]

def estatisticas_texto(texto):
    splitted = texto.split()
    wordsQtd = len(splitted)

    listted = list(texto)
    charQtd = len(listted)

    withoutSpaces = "".join(splitted)
    mediumLen = len(withoutSpaces) // wordsQtd

    longestLen = 0
    longestWord = ""
    for i in range(len(splitted)):
        if len(splitted[i]) > longestLen:
            longestLen = len(splitted[i])
            longestWord = splitted[i]

    stats = [['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'], [wordsQtd, charQtd, mediumLen, longestWord]]

    return stats, wordsQtd, charQtd, mediumLen, longestWord


texto = input("Insira um texto: ")

stats, wordsQtd, charQtd, mediumLen, longestWord = estatisticas_texto(texto)
print(f"\nNúmero de palavras: {wordsQtd}")
print(f"Número de caracteres: {charQtd}")
print(f"Tamanho médio de palavras: {mediumLen}")
print(f"Palavra mais longa: {longestWord}\n")
print(stats)
