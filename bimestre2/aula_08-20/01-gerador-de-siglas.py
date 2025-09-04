# gerador de siglas
# a) simples: Centro de Ciências Computacionais => CCC
# b) com numeração: Centro de Ciências Computacionais => C3

def compacta(term):
    siglaCompacta = term[0]
    i = 1
    j = 1
    while i < len(term):
        if term[i] == term[i-1]:
            j += 1
        else:
            siglaCompacta += term[i-1]
            if j > 1:
                siglaCompacta += str(j)
            j = 1
        i += 1
    siglaCompacta += term[i-1]
    if j > 1:
        siglaCompacta += str(j)
    return siglaCompacta.upper()


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
        sigla = compacta(term)
        return "\n" + sigla + "\n"

    else:
        return "\nÉ necessário selecionar um modo (simples, numeracao)\n"


term = input("Insira um termo para gerar sua sigla: ")
mode = input("Selecione um modo para gerar sua sigla (simples, numeracao): ")
print(sigla(term, mode))
