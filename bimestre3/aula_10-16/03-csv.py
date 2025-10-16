# leia o arquivo e mostre os nomes apenas da graduação
with open("disciplinasC3_2025.csv", "r", encoding="ISO-8859-1") as file:
    content = file.readlines()
    disciplinas = []
    for row in content:
        columns = row.split(";")
        disciplinas.append(columns[1][0:])
    for i in range(len(disciplinas)):
        disciplinas[i] = disciplinas[i].strip('"')
 
for i in range(len(disciplinas)):
    print(disciplinas[i])
