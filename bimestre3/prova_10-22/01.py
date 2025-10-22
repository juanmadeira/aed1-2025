# O arquivo cidades.csv contém todo o cadastro de cidades, independentemente do estado.
# Criar um arquivo com as cidades de cada estado e assim separar as cidades.
# Os nomes dos arquivos devem ser “cidades_RS.csv” para as cidades do Rio Grande do Sul,
# “cidades_SP.csv” para cidades de São Paulo etc.
with open("cidades.csv", "r", encoding="UTF-8") as file:
    content = file.readlines()
    del content[0]
    rows = []
    for row in content:
        rows.append(row.split(";"))
    for i in rows:
        estado = i[2].strip()
        with open(f"dados/cidades_{estado}.csv", "w", encoding="UTF-8") as file_output:
            file_output.write(f"id_cidade;nm_cidade;uf\n")
    for i in rows:
        estado = i[2].strip()
        with open(f"dados/cidades_{estado}.csv", "a", encoding="UTF-8") as file_output:
            file_output.write(f"{i[0]};{i[1]};{i[2]}")
