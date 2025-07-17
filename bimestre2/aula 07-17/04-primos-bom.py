import math


def primo(n):
    i = int(math.sqrt(n))
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True


n = int(input("Insira um número: "))
if primo(n):
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} não é primo!")
