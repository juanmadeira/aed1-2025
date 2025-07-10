limite = int(input("Insira um limite: "))
n = 2
primosQtd = 0

while n < limite:
    i = 2
    primo = True

    while i < n and primo:
        if (n % i) == 0:
            primo = False
        i += 1

    if primo:
        print(f"{n} é primo!")
        primosQtd += 1

    n += 1

print(f"Entre 2 e {n} há {primosQtd} números primos.")
