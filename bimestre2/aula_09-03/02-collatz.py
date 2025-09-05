# sequência de Collatz
# a conjectura de Collatz é uma conjectura matemática que recebeu este nome em referência ao matemático alemão Lothar Collatz.
# esta conjectura aplica-se a qualquer número natural inteiro, e diz-nos para:

# se este número for par, o dividir por 2
# se for ímpar, para multiplicar por 3 e adicionar 1.
# embora não haja uma prova, acredita-se que sempre o valor vai chegar a 1.
# crie a função collatz(num) que retorna uma lista com todos os números da sequência até chegar a 1.

# exemplo:
# collatz(127)
# o maior número é 4372 e tem 47 itens.
# [127, 382, 191, 574, 287, 862, 431, 1294, 647, 1942, 971, 2914, 1457, 4372, 2186, 1093, 3280, 1640, 820, 410, 205, 616, 308, 154,
# 77, 232, 116, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


def collatz(n):
    collatz = []
    collatz.append(n)
    while collatz[-1] != 1:
        if par(collatz[-1]):
            collatz.append(collatz[-1] // 2)
        else:
            collatz.append((collatz[-1] * 3) + 1)
    maior = max(collatz)
    qtd = len(collatz)
    return f"\nO maior número é {maior} e tem {qtd} itens.\n\n{collatz}"


n = int(input("Insira um número para testá-lo na conjectura de Collatz: "))
print(collatz(n))
