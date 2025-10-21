# crie uma planilha com o seguinte formato
# Disciplinas: 456
# Disciplinas Ativas: xxx
# Disciplinas Inativas: xxx
# Disciplinas da Graduação: xxx
# Disciplinas da Pós-Graduação: xxx
with open("disciplinasC3_2025.csv", "r", encoding="ISO-8859-1") as file:
    output = "Disciplinas;Disciplinas Ativas;Disciplinas Inativas;Disciplinas da Graduação;Disciplinas da Pós-Graduação;\n"
    content = file.readlines()
    disciplinas_qtd = -1
    disciplinas_ativas = 0
    disciplinas_inativas = 0
    disciplinas_grad = 0
    disciplinas_pos = 0
    for row in content:
        columns = row.split(";")
        disciplinas_qtd += 1
        if columns[3].upper() == "SIM":
            disciplinas_ativas += 1
        elif columns[3].upper() == "NÃO":
            disciplinas_inativas += 1
        if columns[1].upper() == "GRADUAÇÃO":
            disciplinas_grad += 1
        elif columns[1].upper() == "PÓS-GRADUAÇÃO":
            disciplinas_pos += 1

output += str(disciplinas_qtd) + ";" + str(disciplinas_ativas) + ";" + str(disciplinas_inativas) + ";" + str(disciplinas_grad) + ";" + str(disciplinas_pos) + ";"

with open("06-csv.csv", "w") as file:
    file.write(output)

with open("06-csv.csv", "r") as file:
    print(file.read())
