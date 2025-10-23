# crie uma lista turma que contenha dicionarios de aluno e nota.
# a) calcule a média da turma
# b) faça uma opção de o usuário digitar o nome do aluno e mostre a nota.
# se houver mais de uma nota p/ o mesmo nome, mostre a média das notas encontradas
turma = [
    {
        "nome": "João",
        "nota": 9
    },
    {
        "nome": "Maria",
        "nota": 10
    },
    {
        "nome": "João",
        "nota": 8
    }
]

# a)
def mediaTurma(turma):
    notas_soma = 0
    for i in turma:
        notas_soma += int(i["nota"])

    media = notas_soma / len(turma)
    return media


print(turma)
print(f"A média de notas da turma é: {mediaTurma(turma)}.\n")

# b)
def mostrarNota(turma, nome):
    qtd = 0
    nota = 0
    nota_final = 0
    for i in turma:
        if nome.upper() == i["nome"].upper():
            qtd += 1
            nota += int(i["nota"]) 

    if qtd == 0:
        return False

    nota_final = nota / qtd
    return nota_final


nome = input("Insira o nome de um aluno para buscar sua nota: ")
if not mostrarNota(turma, nome):
    print("Nenhum aluno foi encontrado")
else:
    print(f"A nota do aluno {nome} é {mostrarNota(turma, nome)}")
