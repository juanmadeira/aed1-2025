# Crie um programa em Python que leia uma string e diga qual a maior sequência de letras repetidas na string.
# Por exemplo: “ABCDDDEEFGHIJKKKKOP”
# A maior sequência é de “K”, com 4 incidências.

string = input("Insira uma string: ")
sequencia = 0
recorde = 0
alfabeto = "abcdefghijklmnopqrstuvwxyz"
caractere = ""

i = 0
while i < len(string):
    j = 0
    while j < len(alfabeto):
        if string[i].upper() == alfabeto[j].upper():
            sequencia += 1
        if recorde == 0 or (sequencia > recorde):
            recorde = sequencia
            caractere = string[i]
        else:
            sequencia = 0
        j += 1
    i += 1

print(caractere)
print(recorde)

# i = 0
# while i < len(string):
#     if sequencia >= 1 and (string[i] != string[i - 1]):
#         if sequencia > recorde:
#             recorde = sequencia
#             caractere = string[i - 1]
#     if string[i] == string[i - 1]:
#         if sequencia == 0:
#             sequencia += 1
#         if recorde == 0:
#             caractere = string[i]
#     i += 1
