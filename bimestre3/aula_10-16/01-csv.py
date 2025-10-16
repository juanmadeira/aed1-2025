# leia o arquivo e mostre linha por linha
with open("disciplinasC3_2025.csv", "r", encoding="ISO-8859-1") as file:
    content = file.read()

print(content)
