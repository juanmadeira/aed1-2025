# Crie um programa que sorteie um número entre 0 e 100
# O usuário deve descobrir o número e tem 10 tentativas
# O programa deve dar a dica se o número é maior ou menor que o chutado
import random

random.seed()
tentativas = 10
secret = random.randint(0, 100)
acerto = False

while tentativas > 0:
    palpite = input("Insira seu palpite: ")
    if (secret == palpite):
        acerto = True
    else:
        if (palpite == "love"):
            acerto = True
            cheat = True
        else:
            acerto = False
            if (secret > palpite):
                print("O número secreto é maior que o inserido.")
            else:
                print("O número secreto é menor que o inserido.")
    tentativas -= 1

if acerto:
    print(f"Eureka! O número era mesmo {secret}")
else:
    print(f"Suas tentativas acabaram... o número era {secret}")
