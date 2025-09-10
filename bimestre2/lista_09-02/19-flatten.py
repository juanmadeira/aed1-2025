# escreva `flatten(lista)` que receba uma lista com sublistas aninhadas de profundidade arbitrária e retorne uma lista "achatada"
# exemplo:
# entrada: [1, [2, [3, 4]], 5]
# saída: [1,2,3,4,5]

# def flatten(lista):
#     while isinstance(lista[0], list):
#         print(lista)
#         if lista[0] == []:
#             lista.remove([])
#         else:
#             pop = lista[0][0]
#             lista[0].pop(0)
#             lista.append(pop)
#     else:
#         pop = lista[0]
#         lista.pop(0)
#         lista.append(pop)
#
#     for i in lista:
#         if isinstance(i, list):
#             flatten(lista)
#
#     return lista

def flatten(lista):
    flat = []
    for i in lista:
        if isinstance(i, list):
            flat += flatten(i)
        else:
            flat.append(i)
    return flat


lista = [1, [2, [3, 4, [5, 6]], 7, [8, 9], 10]]
print(f"Lista original: {lista}")
print(f"Lista \"achatada\": {flatten(lista)}")
