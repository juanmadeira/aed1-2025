# Considere a saída do exercício 2 e crie uma função que gere um arquivo HTML com a lista de cidades.
# O arquivo deve ser formatado em uma tabela de modo a ter uma linha por cidade.
# Em cada linha, uma coluna para o nome da cidade e uma coluna para seu estado.
def procurarCidade(query):
    with open("cidades.csv", "r", encoding="UTF-8") as file:
        content = file.readlines()
        del content[0]
        result = "<table>\n"
        rows = []
        for row in content:
            rows.append(row.split(";"))
        for i in range(len(rows)):
            rows[i][2] = rows[i][2].strip()
        for i in rows:
            if query.upper() in i[1].upper():
                result += f"\t<tr>\n\t\t<td>{i[1]}</td><td>{i[2]}</td>\n\t</tr>\n" 
        result += "</table>"
    with open("busca.html", "w", encoding="UTF-8") as file:
        file.write(result)
    with open("busca.html", "r", encoding="UTF-8") as file:
        return file.read()

query = input("\nProcurar cidade: ")
print(f"\n{procurarCidade(query)}")