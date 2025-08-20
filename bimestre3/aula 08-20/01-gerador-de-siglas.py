# gerador de siglas
# a) simples: Centro de Ciências Computacionais => CCC
# b) com numeração: Centro de Ciências Computacionais => C3

# modes: simples, numeracao
def sigla(term, mode):
    sigla = ""
    mode = mode.upper()
    termSplitted = term.upper()
    termSplitted = termSplitted.split()
    connectives = ["DE", "DA", "PARA", "DOS", "E"]

    for i in range(len(termSplitted)):
        if termSplitted[i] not in connectives:
            sigla += termSplitted[i][0]

    if mode == "SIMPLES" or mode == "S":
        return "\n" + sigla + "\n"

    elif mode == "NUMERACAO" or mode == "N":
        # fazer!!!!!!!!!!!!!!!!!!
        return "\n" + sigla + "\n"

    else:
        return "\nÉ necessário selecionar um modo (simples, numeracao)\n"


term = input("Insira um termo para gerar sua sigla: ")
mode = input("Selecione um modo para gerar sua sigla (simples, numeracao): ")
print(sigla(term, mode))
