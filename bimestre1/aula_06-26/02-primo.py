n = int(input("Insira um número: "))

i = n - 1
primo = True

while i > 1:
    if n % i == 0:
        primo = False
    i -= 1

if primo and n != 0 and n != 1:
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} não é primo!")
