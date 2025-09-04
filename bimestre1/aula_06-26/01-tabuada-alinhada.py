limite = int(input("Qual o limite da tabuada? "))
i = 0
j = 0

print("TABUADA: ")
while i < limite:
    i += 1
    while j <= 10:
        print(f"{i} × {j} = {i*j}")
        j += 1
    print("\n")
    j = 0
