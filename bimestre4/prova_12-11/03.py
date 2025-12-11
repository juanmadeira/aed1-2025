# Crie um gerador de relatórios HTML. O gerador consiste em uma função
# que recebe como parâmetro um dicionário contendo os dados de um formulário e
# retorna o string contendo o código HTML deste formulário. No dicionário de entrada,
# há espaço para o nome de cada item do formulário, tipo (text, checkbox…) e, caso
# haja necessidade, as opções.
# Para simplificar, seu gerador de formulário somente precisa reconhecer input, password,
# checkbox e select. Os elementos podem aparecer diversas vezes, ou seja, podemos ter um
# formulário muito grande!

def gerarHTML(campos):
    html = "<form>\n"

    for key, value in campos.items():
        if value["tipo"] == "checkbox":
            html += f"\t<label>{key}:</label><br>\n"
            for i in range(len(value["opcoes"])):
                html += f"\t<input type=\"{value["tipo"]}\" name=\"{key}\" value=\"{value["opcoes"][i]}\"> {value["opcoes"][i]}<br>\n"
            html += f"\n"

        elif value["tipo"] == "select":
            html += f"\t<label>{key}:</label>\n"
            html += f"\t<select name=\"{key}\">\n"
            for i in range(len(value["opcoes"])):
                html += f"\t\t<option>{value["opcoes"][i]}</option>\n"
            html += f"\t</select><br>\n"
        else:
            html += f"\t<label>{key}:</label>\n"
            html += f"\t<input type=\"{value["tipo"]}\" name=\"{key}\"><br>\n\n"

    html += "</form>"

    return html

campos = {
    "usuario": {
        "tipo": "text",
        "opcoes": None
    },
    "senha": {
        "tipo": "password",
        "opcoes": None
    },
    "interesses": {
        "tipo": "checkbox",
        "opcoes": ["música", "esportes", "viagens"]
    },
    "cidade": {
        "tipo": "select",
        "opcoes": ["São Paulo", "Rio de Janeiro", "Curitiba"]
    }
}

print(gerarHTML(campos))
with open("03.html", "w", encoding="UTF-8") as file:
    file.write(gerarHTML(campos))