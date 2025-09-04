# Gerador de Anagramas de Palavras
# Crie uma função geraAnagramas(p) que retorne uma lista com TODOS os anagramas de uma palavra.
# Ignore acentos e diferenças de maiúsculas/minúsculas.
# Dica: o número de anagramas será o fatorial do número de diferentes letras.

import random
random.seed()


def fatorial(palavra):
    n = len(palavra)
    fatorial = 0
    i = 1
    while i < len(palavra):
        if i == 1:
            fatorial = n * (n - 1)
        else:
            fatorial = fatorial * (n - 1)
        n -= 1
        i += 1
    return fatorial


def geraAnagramas(palavra):
    anagramas = []
    pList = list(palavra)
    while len(anagramas) < fatorial(palavra):
        novoAnagrama = ""
        for i in range(len(pList)):
            randomIndex = random.randint(0, len(pList) - 1)
            if randomIndex > len(pList):
                randomIndex = -1

            novoAnagrama += pList[random.randint(0, randomIndex)]
            pList.pop(randomIndex)
        pList = list(palavra)
        anagramas.append(novoAnagrama)
    return pList, anagramas


palavra = input("Insira uma palavra: ")
print(f"\nPalavra: {palavra}\nAnagramas possíveis: {geraAnagramas(palavra)}")
