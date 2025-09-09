# implemente uma função `compactar(texto)` que comprima a string substituindo sequências de caracteres repetidos pelo caractere seguido da contagem.
# depois, implemente `descompactar(texto)` que faça o processo inverso.
# exemplo:
# entrada: "aaabbcccc"
# saída: "a3b2c4"

# entrada: "a3b2c4"
# saída: "aaabbcccc"

def compactar(texto):
    qtd = 1
    novoTexto = ""
    texto = list(texto)
    for i in range(len(texto)):
        if i + 1 < len(texto):
            if texto[i] == texto[i + 1]:
                qtd += 1
            else:
                novoTexto += texto[i]
                novoTexto += str(qtd)
                qtd = 1
    novoTexto += texto[-1]
    novoTexto += str(qtd)

    return novoTexto


def descompactar(texto):
    novoTexto = ""
    i = 0
    while i < len(texto):
        if i + 1 < len(texto):
            novoTexto += texto[i] * int(texto[i + 1])
        i += 2

    return novoTexto


mode = input("1. Compactar texto\n2. Descompactar texto\nO que deseja fazer? ")
if mode == "1":
    texto = input("\nInsira uma frase ou palavra: ")
    print(compactar(texto))
elif mode == "2":
    texto = input("\nInsira uma frase ou palavra: ")
    print(descompactar(texto))
else:
    print("\nModo não reconhecido. Programa encerrado.")
