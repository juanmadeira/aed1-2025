# faça um dicionário contatos onde cada contato é um novo dicionário.
# faça uma busca a partir de um nome lido e mostre o telefone
contatos = {
    "Maria": {
        "telefone": 53981234567,
        "email": "maria@protonmail.com"
    },
    "João": {
        "telefone": 21982345678,
        "email": "joao@protonmail.com"
    }
}

def buscaTel(nome):
    for i in contatos:
        if i.upper() == nome.upper():
            return f"O telefone de {i} é {contatos[i]['telefone']}"

nome = input("Insira um nome para buscar seu telefone: ")
print(buscaTel(nome))