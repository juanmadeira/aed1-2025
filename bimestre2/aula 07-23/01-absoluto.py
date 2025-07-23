def absoluto(n):
    if n > 0:
        return n
    return n * -1

n = int(input("Insira um número: "))
print(absoluto(n), id(absoluto(n)))
