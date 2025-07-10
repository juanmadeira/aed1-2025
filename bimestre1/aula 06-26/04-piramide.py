# Leia um tijolo (caractere): x
# Leia a altura: 5
#     x
#    xxx
#   xxxxx
#  xxxxxxx
# xxxxxxxxx
t = input("Insira um tijolo: ")
while len(t) != 1:
    t = input("Insira um (e apenas um) tijolo: ")

h = int(input("Insira a altura: "))

i = 0
linha = ""
piramide = "\n"
blank = h
while i < h:
    while blank > 0:
        piramide += " "
        blank -= 1
    if i == 0:
        linha += t
    else:
        linhaCopy = linha
        linha = t + linhaCopy + t
    piramide += linha + "\n"
    i += 1
    blank = h - i

print(f"{piramide}")
