# Leia um número n e mostre a sequência de fibonacci até o n-ésimo termo
n = int(input("Insira um número: "))
fib = 0
termo1 = 0
termo2 = 1

print(termo1)
print(termo2)

i = 0
while (i <= n - 3):
    fib = termo2 + termo1
    print(fib)
    termo1 = termo2
    termo2 = fib
    i += 1
