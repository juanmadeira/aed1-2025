# dada uma string, compacte-a substituindo sequências repetidas pela letra seguida da quantidade
# ex.: "aaabbccccd" → "a3b2c4d1"

def letterAmount(string):
    amount = 1
    newString = ""
    string = list(string)
    for i in range(len(string)):
        if i + 1 < len(string):
            if string[i] == string[i + 1]:
                amount += 1
            else:
                newString += string[i]
                newString += str(amount)
                amount = 1
    newString += string[-1]
    newString += str(amount)
    return newString


string = input("Insira uma frase ou palavra: ")
print(letterAmount(string))
