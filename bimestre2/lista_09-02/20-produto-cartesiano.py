# implemente `produto_cartesiano(lista1, lista2)` que retorne todas as combinações possíveis entre elementos de duas listas.
# exemplo:
# entrada: ([1,2], ['a','b'])
# saída: [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

def produto_cartesiano(lista1, lista2):
    prod = []
    for i in lista1:
        for j in lista2:
            prod.append([i, j])

    return prod


lista1 = [1, 2]
lista2 = ["a", "b"]
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Combinações possíveis: {produto_cartesiano(lista1, lista2)}")
