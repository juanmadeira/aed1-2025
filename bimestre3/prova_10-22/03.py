# Criar um arquivo com dados sumarizados das cidades com os seguintes itens
# e crie um arquivo texto com estas informações.
# a)​ Quantas cidades por cada estado;
# b)​ Qual a cidade com nome mais longo;
# c)​ Qual a cidade com nome mais curto;
with open("cidades.csv", "r", encoding="UTF-8") as file:
    content = file.readlines()
    del content[0]
    rows = []
    cidades = []
    estados = []
    cidades_por_estado = []
    nome_longo, nome_curto = "", ""
    for row in content:
        rows.append(row.split(";"))
    for i in range(len(rows)):
        rows[i][2] = rows[i][2].strip()
    for i in rows:
        cidades.append(i[1])
        estados.append(i[2])

    # nome mais longo
    recorde = 0
    for cidade in cidades:
        tamanho = len(cidade)
        if tamanho > recorde:
            recorde = tamanho
            nome_longo = cidade

    # nome mais curto
    recorde = 999
    for cidade in cidades:
        tamanho = len(cidade)
        if tamanho < recorde:
            recorde = tamanho
            nome_curto = cidade

    for estado in estados:
        cidades_por_estado.append([estado, estados.count(estado)])

    for i in range(len(cidades_por_estado)):
        if cidades_por_estado[i] == cidades_por_estado[i - 1]:
            cidades_por_estado[i - 1] = [""]

    cidades_por_estado_str = ""
    for i in cidades_por_estado:
        if i != [""]:
            cidades_por_estado_str += f"{i[0]}: {i[1]} cidade(s)\n"

with open("sumario.txt", "w", encoding="UTF-8") as file:
    file.write("\t=== SUMÁRIO ===\n\n")
    file.write(f"a) Quantas cidades por cada estado: \n{cidades_por_estado_str}\n")
    file.write(f"b) Cidade com nome mais longo: \n{nome_longo}\n\n")
    file.write(f"c) Cidade com nome mais curto: \n{nome_curto}")

with open("sumario.txt", "r", encoding="UTF-8") as file:
    print(file.read())