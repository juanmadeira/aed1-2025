# Crie um programa que leia do usuário uma parte do nome de cidade.
# Escreva se a cidade está cadastrada e mostre os nomes das cidades selecionadas
# “Rio”
# Rio Grande
# Rio de Janeiro
# Rio das Pedras
def procurarCidade(query):
    with open("cidades.csv", "r", encoding="UTF-8") as file:
        content = file.readlines()
        del content[0]
        result = ""
        rows = []
        cidades = []
        for row in content:
            rows.append(row.split(";"))
        for i in rows:
            cidades.append(i[1])
        for cidade in cidades:
            if query.upper() in cidade.upper():
                result += cidade + "\n"

    if result == "":
        result = "Nenhuma cidade foi encontrada."

    return result

query = input("\nProcurar cidade: ")
print(f"\n{procurarCidade(query)}")