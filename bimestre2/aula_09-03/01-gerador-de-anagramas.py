# gerador de anagramas de palavras
# crie uma função geraAnagramas(p) que retorne uma lista com TODOS os anagramas de uma palavra.
# ignore acentos e diferenças de maiúsculas/minúsculas.
# dica: o número de anagramas será o fatorial do número de diferentes letras.

# INCOMPLETO

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
    palavra = list(palavra)

    # while len(anagramas) < fatorial(palavra):
    # maiorSalto = int(len(palavra) - 1)

    salto = 1
    while salto < 3:
        print(f"\nsalto = {salto}\n")
        for j in range(len(palavra)):
            for i in range(len(palavra)):
                print(f"\ni = {i}")

                cut = palavra[i:i + salto]
                cut = "".join(cut)
                print(f"cut = {cut}")

                resto = palavra[:i] + palavra[i + salto:]
                resto = "".join(resto)
                print(f"resto = {resto}")

                print(resto + cut)
                anagramas.append(resto + cut)
        salto += 1

    return anagramas


palavra = input("Insira uma palavra: ")
print(f"\nPalavra: {palavra}\nAnagramas possíveis: {geraAnagramas(palavra)}")
