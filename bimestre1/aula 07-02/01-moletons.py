'''
1. Leia o nome e o tamanho do moletom de cada aluno/professor que encomendou o moletom
Termine de ler quando o nome for vazio
Mostre na tela o nome e o tamanho de cada moletom
2. Cada moletom custa R$135,00. Calcule quanto deverá ser coletado de dinheiro
3. Leia o tamanho e escreva quantos moletons foram encomendados deste tamanho
4. Leia um nome e escreva qual o tamanho do moletom. Se o nome não estiver na lista, escreva "tu não encomendou!"
5. Leia um tamanho e mostre uma lista dos nomes que encomendaram moletom desse tamanho
6. Leia as listas e gere uma tabela HTML com os dados bem formatados
'''
cliente = "."
clientes = []
tamanhos = []

cliente = input("Insira o nome do aluno/professor: ")
clientes.append(cliente)
while cliente != "":
    tamanho = input("Insira o tamanho do moletom desejado: ").upper()
    tamanhos.append(tamanho)
    cliente = input("Insira o nome do aluno/professor: ")
    clientes.append(cliente)

custoUnidade = 135
custoTotal = len(clientes) * custoUnidade
print(f"\nO custo total dos moletons é de R${custoTotal}")

print()
consultaTamanho = input("Insira um tamanho para consulta: ").upper()
consultaTamanhoQtd = 0
for item in tamanhos:
    if item == consultaTamanho:
        consultaTamanhoQtd += 1

print(f"Quantidades de moletom tamanho \"{consultaTamanho}\" encomendados: {consultaTamanhoQtd}")

print()
consultaCliente = input("Insira um nome para consulta: ")
if consultaCliente in clientes:
    print(f"O cliente {consultaCliente} encomendou um moletom de tamanho \"{tamanhos[clientes.index(consultaCliente)].upper()}\"")
else:
    print("Tu não encomendou!")

print()
consultaTamanho2 = input("Insira um tamanho para consulta: ").upper()
consultaTamanho2Clientes = []
i = 0
while i < len(tamanhos):
    if tamanhos[i] == consultaTamanho2:
        consultaTamanho2Clientes.append(clientes[i])
    i += 1

print(f"Clientes que encomedaram um moletom de tamanho {consultaTamanho2}:")
print(*consultaTamanho2Clientes, sep=", ")
