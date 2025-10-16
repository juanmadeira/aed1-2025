# pegar um texto da web e colocar em um arq.txt
# com esse arquivo:
# criar uma lista de palavrões e verificar se o arquivo está "puro" ou quais palavrões contém
# gerar o arquivo censurado (mantém primeira letra, resto vira "*")

cuss_words_list = ["PORRA", "CARALHO", "MERDA"]
def hasCussWords(file):
    with open(file, "r") as file:
        content = file.read().split()
        cuss_words = []
        qtd = 0
        for i in content:
            for j in range(len(cuss_words_list)):
                if cuss_words_list[j] in i.upper():
                    qtd += 1
                    cuss_words.append(cuss_words_list[j].lower())

        for i in range(len(content)):
            for j in range(len(cuss_words)):
                k = ""
                if cuss_words[j].upper() in content[i].upper():
                    k += content[i][0]
                    k += "*" * (len(content[i]) - 1)
                    content[i] = k

        content = str(content)
        with open("02-sem-palavroes.txt", "w") as file:
            file.write(content)

        cuss_words = ", ".join(cuss_words)
        cuss_words = str(cuss_words)
        if qtd > 0:
            return True, cuss_words
        else:
            return False

if hasCussWords("arquivo.txt"):
    has_cuss_words, cuss_words = hasCussWords("arquivo.txt")
    print(f"O texto contém os palavrões: {cuss_words}.")
else:
    print("O texto não contém palavrões.")
