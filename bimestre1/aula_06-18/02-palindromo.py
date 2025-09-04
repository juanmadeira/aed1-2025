# Imprima todos os números palíndromos de 1 a 1000
# Ex: 747 (ao contrário segue igual)
i = 1
while i <= 1000:
    if len(str(i)) == 1:
        print(i)
    if len(str(i)) == 2:
        if str(i)[0] == str(i)[1]:
            print(i)
    if len(str(i)) == 3:
        if str(i)[0] == str(i)[2]:
            print(i)
    i += 1
