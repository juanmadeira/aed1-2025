# crie uma função que receba um string com um código HTML
# retorne apenas o texto, retirando assim todas as tags de formatação.

def removerHTML(html):
    html = list(html)

    for i in range(len(html)):
        while html[i] == "<":
            while html[i] != ">":
                html.pop(i)
                html.append("")
            html.pop(i)
            html.append("")
            texto = html

    output = ""
    for i in range(len(texto)):
        output += texto[i]

    return output


html = '''
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>O melhor sanduíche de todos os tempos (segundo o Chaves)</title>
    </head>
    <body>
        <h1>Sanduíche de Presunto (do Chaves)</h1>
        <p><u>Ingredientes:</u></p>
        <ul>
            <li>2 fatias de pão de forma</li>
            <li>1 fatia de presunto</li>
            <li>Margarina ou similar (opcional)</li>
        </ul>
    </body>
</html>
'''

print(f"\nHTML Original:\n{html}")
print(f"\nSem HTML: {removerHTML(html)}")
