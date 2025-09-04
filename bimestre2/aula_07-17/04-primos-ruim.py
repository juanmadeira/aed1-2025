from timeit import default_timer as timer


def primo(n):
    i = n - 1
    primo = True

    while i > 1:
        if n % i == 0:
            primo = False
        i -= 1

    if primo and n != 0 and n != 1:
        return True
    else:
        return False


n = int(input("Insira um número: "))
tempoInicio = timer()

if primo(n):
    print(f"O número {n} é primo!")
else:
    print(f"O número {n} não é primo!")

tempoFim = timer()
tempoTotal = tempoFim - tempoInicio

print(f"\nTempo de execução: {tempoTotal}")
