# pegar um texto da web e colocar em um arq.txt
# com esse arquivo:
# salvar em outro arquivo o mesmo texto sem as vogais

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


print(removeVowels("arquivo.txt"))
