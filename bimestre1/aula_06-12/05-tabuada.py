# Leia um número e faça a tabuada deste número de zero a cem
n = int(input("Insira um número: "))
cont = 0

while cont < 100:
    result = n * cont
    print(f"{n} x {cont} = {result}")
    cont += 1
