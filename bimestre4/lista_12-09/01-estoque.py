# Desenvolva um sistema simples de gerenciamento de estoque para uma loja. Crie um programa
# em Python que realiza as seguintes operações:
# ● Inicialização do Estoque:
#     ● Crie um dicionário chamado estoque para armazenar informações sobre os
#     produtos em estoque.
#     ● Cada chave do dicionário representa o nome de um produto, e o valor associado
#     é a quantidade disponível desse produto.
# ● Adição de Produtos:
#     ● Crie uma função chamada adicionar_produto que aceite três parâmetros: o
#     dicionário de estoque, o nome do produto e a quantidade a ser adicionada.
#     ● A função deve verificar se o produto já existe no estoque. Se existir, a quantidade
#     deve ser somada à quantidade existente. Se não existir, adicione o produto ao
#     estoque com a quantidade fornecida.
# ● Venda de Produtos:
#     ● Crie uma função chamada vender_produto que aceite três parâmetros: o
#     dicionário de estoque, o nome do produto e a quantidade a ser vendida.
#     ● A função deve verificar se o produto existe no estoque e se a quantidade a ser
#     vendida é menor ou igual à quantidade em estoque. Se for o caso, subtraia a
#     quantidade vendida do estoque. Caso contrário, imprima uma mensagem
#     informando que a venda não pode ser realizada por falta de estoque.
# ● Relatório de Estoque:
#     ● Crie uma função chamada relatorio_estoque que aceite o dicionário de estoque
#     como parâmetro e imprima um relatório mostrando o nome de cada produto e sua
#     quantidade em estoque.
# ● Teste do Programa:
#     ● Crie um código principal que inicialize o estoque, adicione alguns produtos, venda
#     alguns produtos e gere um relatório de estoque

def ver_estoque(estoque):
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, qtd in estoque.items():
            print(f"{produto}: {qtd}")

def adicionar_produto(estoque, nome, qtd):
    if nome in estoque:
        estoque[nome] += qtd
    else:
        estoque[nome] = qtd

    print(f"\nProduto {nome} atualizado. Estoque atual: {estoque[nome]}")

def vender_produto(estoque, nome, qtd):
    if not nome in estoque:
        print(f"O produto {nome} não pode ser vendido pois não se encontra no estoque")
    elif estoque[nome] < qtd:
        print(f"O produto {nome} não pode ser vendido pois sua quantidade no estoque é menor do que a que deseja vender.")
    else:
        estoque[nome] -= qtd
        print(f"Produto {nome} vendido! Estoque atual: {estoque[nome]}")

def menu():
    print(
        f"\n"
        f"=========================\n"
        f"0. Sair\n"
        f"1. Adicionar produto\n"
        f"2. Vender produto\n"
        f"3. Relatório\n"
        f"=========================\n"
    )
    mode = input("O que deseja fazer? ")
    print("")

    if mode == "0":
        return
    elif mode == "1":
        nome = input("Insira o produto a ser adicionado: ")
        qtd = int(input(f"Quantos(as) {nome} deseja adicionar ao estoque? "))
        adicionar_produto(estoque, nome, qtd)
    elif mode == "2":
        nome = input("Insira o produto a ser vendido: ")
        qtd = int(input(f"Quantos(as) {nome} deseja vender? "))
        vender_produto(estoque, nome, qtd)
    elif mode == "3":
        ver_estoque(estoque)
    else:
        print("Opção inválida.")
    menu()

estoque = {}
menu()