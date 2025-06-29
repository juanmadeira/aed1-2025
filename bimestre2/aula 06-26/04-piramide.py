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
piramide = ""
while i < h:
    if i == 0:
        piramide += t
    else:
        piramide2 = piramide
        piramide += t + piramide2 + t

    piramide += "\n"
    i += 1

print(f"{piramide}")
