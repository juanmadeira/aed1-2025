# crie uma função que seja um particionador de listas
# ela deve receber como parâmetro uma lista e um número n
# você deve retornar uma lista de listas com o tamanho dado

def particionador(lista, n):
    part = []
    aux = []

    for i in range(len(lista)):
        aux.append(lista[i])
        if len(aux) == n:
            if len(part) == 0:
                part.append(aux)
            aux = []
            part.append(aux)

    for i in part:
        if i == []:
            part.remove(i)

    return part


lista = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
n = 5

print(f"\nLista original: {lista}")
print(f"\nLista particionada: {particionador(lista, n)}")
