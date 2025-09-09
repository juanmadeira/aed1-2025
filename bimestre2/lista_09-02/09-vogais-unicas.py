# escreva uma função `vogais_unicas(texto)` que conte quantas vogais distintas aparecem na string
# exemplo:
# entrada: "Programacao"
# saída: 2

def vogais_unicas(texto):
    vogais = ["a", "e", "i", "o", "u"]
    vogaisUnicas = 0
    vogaisTexto = []
    for i in range(len(texto)):
        if texto[i] in vogais and texto[i] not in vogaisTexto:
            vogaisUnicas += 1
            vogaisTexto.append(texto[i])

    return vogaisUnicas


texto = input("Insira um texto: ")
print(vogais_unicas(texto))
