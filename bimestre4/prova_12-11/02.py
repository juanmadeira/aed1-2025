# Crie uma função chamada inverter_dict(d) que recebe um
# dicionário Python e retorna um novo dicionário invertido, onde as chaves viram
# valores e os valores viram chaves. Caso dois ou mais elementos do dicionário original
# tenham o mesmo valor, a chave correspondente no dicionário invertido deve ter
# como valor uma lista contendo todas as chaves originais. Exemplo:
# {'a': 1, 'b': 2, 'c': 1} → {1: ['a', 'c'], 2: 'b'}

def inverter_dict(d):
    e = {}

    for value in d.values():
        e[value] = []

    for key, value in d.items():
        if value in e:
            e[value].append(key)
    
    for key, value in e.items():
        if len(value) == 1: # retira da lista se for apenas um elemento
            new_value = value[0]
            e[key] = new_value

    return e

d = {"a": 1, "b": 2, "c": 1}
print(inverter_dict(d))