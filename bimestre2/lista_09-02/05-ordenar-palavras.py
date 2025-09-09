# ordenação de palavras por critério personalizado
# escreva uma função `ordenar_palavras(frase)` que:
# 1. separe a frase em palavras,
# 2. ordene as palavras primeiro pelo tamanho e depois em ordem alfabética
# exemplo:
# entrada: "banana uva morango pera abacaxi"
# saída: ["uva", "pera", "banana", "abacaxi", "morango"]

def ordenar_palavras(frase):
    palavras = frase.split()
    ordem = []

    for i in range(len(palavras)):
        menor = min(palavras, key=len)
        ordem.append(menor)
        palavras.pop(palavras.index(menor))

    for i in range(len(ordem)):
        for j in range(len(ordem) - i - 1):
            if (len(ordem[j]) == len(ordem[j + 1])):
                if ordem[j].upper() > ordem[j + 1].upper():
                    ordem[j], ordem[j + 1] = ordem[j + 1], ordem[j]

    return ordem


frase = input("Insira uma frase: ")
print(ordenar_palavras(frase))
