# pegar um texto da web e colocar em um arq.txt
# com esse arquivo:
# a) salvar em outro arquivo o mesmo texto sem as vogais
# b) criar uma lista de palavrões e verificar se o arquivo está "puro" ou quais palavrões contém
# c) gerar o arquivo censurado (mantém primeira letra, resto vira "*")

def removeVowels(file):
    with open(file, "r") as file:
        vowels = ["A", "E", "I", "O", "U", "Á", "À", "Â", "Ã", "É", "Ê", "Í", "Ì", "Ó", "Ô", "Õ"]
        content = file.read()
        output = content
        for i in content:
            for j in vowels:
                if i.upper() == j:
                    output = output.replace(i, "")
    with open("01-sem-vogais.txt", "w") as file:
        file.write(output)
    with open("01-sem-vogais.txt", "r") as file:
        return file.read()


def hasCussWords(file):
    with open(file, "r") as file:
        cuss_words = ["PORRA", "CARALHO"]
        content = file.read().split()
        qtd = 0
        for i in content:
            for j in cuss_words:
                if i.upper() == j:
                    qtd += 1
        if qtd > 0:
            return True
        else:
            return False


# def censor(file):
#     with open(file, "r") as file:
#         cuss_words = ["PORRA", "CARALHO"]
#         content = file.read().split()
#         for i in content:
#             for j in cuss_words:
#                 k = ""
#                 if i.upper() == j:
#                     k += i[0]
#                     k += "*" * (len(i) - 1)
#                     content = content.replace(i, k)
#         return content


print(removeVowels("01-arquivos.txt"))

if hasCussWords("01-arquivos.txt"):
    print("O texto contém palavrões.")
else:
    print("O texto não contém palavrões.")

# print(f"\n{censor('01-arquivos.txt')}")
