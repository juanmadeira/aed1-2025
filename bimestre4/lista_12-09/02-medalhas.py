# Crie um programa em Python para realizar o acompanhamento de medalhas olímpicas de países.
# ● Inicialização das Medalhas:
#     ● Crie um dicionário chamado medalhas para armazenar informações sobre as
#     medalhas.
#     ● Use nomes de países como chaves do dicionário e, como valores associados, crie
#     outro dicionário com as seguintes chaves: 'ouro', 'prata' e 'bronze', representando
#     a contagem de medalhas de ouro, prata e bronze para cada país. Exemplo:
#     medalhas = {'PaisA': {'ouro': 2, 'prata': 1, 'bronze': 0}, 'PaisB': {'ouro': 0, 'prata': 2,
#     'bronze': 1}}
# ● Atualização de Medalhas:
#     ● Crie uma função chamada atualizar_medalhas que aceite três parâmetros: o
#     dicionário de medalhas, o nome do país e a medalha conquistada (ouro, prata ou
#     bronze).
#     ● A função deve incrementar a contagem de medalhas correspondente ao país e ao
#     tipo de medalha fornecidos.
# ● Relatório de Medalhas:
#     ● Crie uma função chamada relatorio_medalhas que aceite o dicionário de
#     medalhas como parâmetro e imprima um relatório mostrando o nome de cada
#     país e suas respectivas contagens de ouro, prata e bronze.
# ● Teste do Programa:
#     ● Inicialize o dicionário de medalhas com alguns países fictícios e suas medalhas.
#     ● Utilize a função atualizar_medalhas para simular a conquista de novas medalhas
#     por alguns países.
#     ● Imprima o relatório de medalhas utilizando a função relatorio_medalhas

def atualizar_medalhas(medalhas, pais, tipo, qtd):
    if pais in medalhas:
        medalhas[pais][tipo] += qtd
    else:
        medalhas[pais] = {'ouro': 0, 'prata': 0, 'bronze': 0}
        medalhas[pais][tipo] = qtd

def relatorio_medalhas(medalhas):
    for pais, tipos in medalhas.items():
        print(f"{pais}:")
        for tipo_medalha, tipo_qtd in tipos.items():
            print(f"\t{tipo_medalha}: {tipo_qtd}")

def menu():
    print(
        f"\n"
        f"=========================\n"
        f"0. Sair\n"
        f"1. Atualizar medalhas\n"
        f"2. Relatório\n"
        f"=========================\n"
    )
    mode = input("O que deseja fazer? ")
    print("")

    if mode == "0":
        return
    elif mode == "1":
        pais = input("Insira o país a ser alterado: ")
        tipo = input(f"Qual tipo de medalha deseja adicionar? ")
        qtd = int(input(f"Quantas medalhas de {tipo} deseja adicionar ao país {pais}: "))
        atualizar_medalhas(medalhas, pais, tipo, qtd)
    elif mode == "2":
        relatorio_medalhas(medalhas)
    else:
        print("Opção inválida.")
    menu()

medalhas = {
    'Brasil': {'ouro': 2, 'prata': 1, 'bronze': 0},
    'China': {'ouro': 0, 'prata': 2, 'bronze': 1},
    'Marrocos': {'ouro': 1, 'prata': 0, 'bronze': 3}
}

menu()