# Passe o pseudocódigo abaixo para python:
# 1. Inicialização do baralho:
# 1.1 Crie uma lista chamada `baralho` representando as cartas
# 1.2 Para cada naipe (Copas, Espadas, Ouros, Paus):
# 1.2.1 Para cada valor de carta (Ás, 2, 3, ..., Rei):
# 1.2.1.1 Adicione a carta ao baralho.
# 2. Embaralhamento:
# 2.1 Para cada posição i no baralho (de trás para frente até a
# segunda posição):
# 2.1.1 Escolha uma posição aleatória j, onde 0 <= j < i.
# 2.1.2 Troque a carta na posição i com a carta na posição j.
# 3. Exibição do baralho embaralhado:
# 3.1 Para cada carta no baralho:
# 3.1.1 Exiba a carta.
# 4. Fim do programa.

import random

baralho = []
naipes = ["♥️", "♠️", "♦️", "♣️"]
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

for naipe in naipes:
    for valor in valores:
        baralho.append(f"{valor} {naipe}")

for i in range(len(baralho) - 1, 0, -1):
    j = random.randint(0, i - 1)
    baralho[i], baralho[j] = baralho[j], baralho[i]

for carta in baralho:
    print(carta)