# gere um novo arquivo csv apenas com as disciplinas com "algoritmo" no nome
with open("disciplinasC3_2025.csv", "r", encoding="ISO-8859-1") as file:
    content = file.readlines()
    algoritmo = content[0]
    algoritmo = algoritmo[:-1]
    algoritmo += ";\n"
    for row in content:
        columns = row.split(";")
        if "algoritmo" in columns[4].lower():
            algoritmo += row

with open("04-csv.csv", "w") as file:
    file.write(algoritmo)

with open("04-csv.csv", "r") as file:
    print(file.read())
