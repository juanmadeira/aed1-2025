def chamada(nome, lista):
    if nome in lista:
        return lista
    lista.append(nome)
    return lista


lista = ["Guilherme", "Breno (RIP)", "Murillo (RIP)"]
nome = input("Insira um nome: ")
print(chamada(nome, lista))
