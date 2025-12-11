# Leia um texto e crie um programa python para as seguintes tarefas:
# a) Faça um dicionário com cada palavra como chave e como valor o número de
# ocorrências da palavra e uma lista de cada palavra imediatamente anterior àquela
# palavra. Separadores e nova linha devem ser ignorados. Por exemplo:
# “E o pulso ainda
# pulsa (pulso)
# (Pulso)
# O pulso ainda
# pulsa (pulso)
# (Pulso)”
#
# ->
#
# {
# ….
# ‘PULSO’:
# [6,[O,PULSA,PULSO]]
# ….
# }
#
# b) Salve os dados em um arquivo CSV com o cabeçalho
# (TERMO;OCORRÊNCIA;TERMOS). Por exemplo:
# ….
# pulso;6;o,pulsa,pulso
# ….

text = "E o pulso ainda\n" \
    "pulsa (pulso)\n" \
    "(Pulso)\n" \
    "O pulso ainda\n" \
    "pulsa (pulso)\n" \
    "(Pulso)"

text = text.lower()
text = text.replace("\n", " ")
text = text.replace("(", "")
text = text.replace(")", "")
text = text.split()

d = {}
e = []

for i in range(len(text)):
    if i == 0:
        d[text[i]] = [text.count(text[i]), e]
    else:
        d[text[i]] = [text.count(text[i]), text[i-1]]

csv = f"TERMO;OCORRÊNCIA;TERMOS\n"
for key, value in d.items():
    csv += f"{key};"
    for i in range(len(value)):
        if i == 0:
            csv += f"{value[i]};"
        elif i == len(value) - 1:
            csv += f"{value[i]}"
        else:
            csv += f"{value[i]},"
    csv += "\n"

print(csv)
with open("01.csv", "w") as file:
    file.write(csv)