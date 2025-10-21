# gere uma nova planilha apenas com as disciplinas sem nome em inglês
with open("disciplinasC3_2025.csv", "r", encoding="ISO-8859-1") as file:
    content = file.readlines()
    disciplinas = []
    englishless = content[0]
    englishless = englishless[:-1]
    englishless += ";\n"
    for row in content:
        columns = row.split(";")
        if columns[6] == "\n":
            englishless += row

with open("05-csv.csv", "w") as file:
    file.write(englishless)

with open("05-csv.csv", "r") as file:
    print(file.read())
