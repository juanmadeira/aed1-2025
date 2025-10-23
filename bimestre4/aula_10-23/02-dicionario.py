# crie um dicionário pessoa com nome, idade, cidade e cor-favorita.
# a) faça um programa de busca para mostrar o valor do parâmetro desejado.
# b) pergunte qual a profissão dessa pessoa e crie um novo campo no dicionário.
# c) parabéns pra você! crie uma função aniversário que retorna a idade + 1. atualize a idade no dicionário
# d) você foi demitido :( retire a profissão do seu dicionário
# e) você voltou p/ casa dos pais. atualize a cidade. pergunte a nova cidade a ser adicionada.
pessoa = {
    "nome": "Juan",
    "idade": "20",
    "cidade": "Rio Grande",
    "cor-favorita": "#008b8b"
}

# a)
# print(f"A pessoa possui: {print(i[0]) for i in pessoa}")
busca = input("Insira um campo para ser informado: ")
print(f"{busca}: {pessoa[busca]}\n")

# b)
profissao_update = input("Insira a profissão dessa pessoa: ")
pessoa["profissao"] = profissao_update
print(f"Profissão: {pessoa["profissao"]}\n")

# c)
def aniversario():
    pessoa["idade"] = str(int(pessoa["idade"]) + 1)
    print(f"Parabéns!!! {pessoa["nome"]} agora tem {pessoa["idade"]} anos.\n")

aniversario()

# d)
def demissao():
    print(f"Sinto muito... {pessoa["nome"]} perdeu seu emprego como {pessoa["profissao"]}\n")
    del pessoa["profissao"]

demissao()

# e)
def voltarPraBaia():
    cidade_update = input("Hora de voltar pra casa dos pais... qual o nome da cidade de destino? ")
    pessoa["cidade"] = cidade_update
    print(f"(...) {pessoa["nome"]} chegou em {pessoa["cidade"]}\n")

voltarPraBaia()
