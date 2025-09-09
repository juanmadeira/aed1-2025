# implemente uma função `maior_substring_unica(texto)` que encontre a maior substring sem caracteres repetidos
# exemplo:
# entrada: "abcabcbb"
# saída: "abc"
# entrada: "bbbbb"
# saída: "b"

def maior_substring_unica(texto):
    maior = ""
    recorde = ""
    maiorLen = 0
    for i in range(len(texto)):
        if texto[i] not in maior:
            maior += texto[i]
            if len(maior) > maiorLen:
                maiorLen = len(maior)
                recorde = maior
        else:
            maior = ""

    return recorde


texto = input("Insira um texto: ")
print(maior_substring_unica(texto))
