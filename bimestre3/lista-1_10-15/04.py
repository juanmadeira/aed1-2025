# faça um programa em python que leia um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece no arquivo.
with open("01.txt", "r") as file:
    content = file.read()
    alphabet = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "E": 0,
        "F": 0,
        "G": 0,
        "H": 0,
        "I": 0,
        "J": 0,
        "K": 0,
        "L": 0,
        "M": 0,
        "N": 0,
        "O": 0,
        "P": 0,
        "Q": 0,
        "R": 0,
        "S": 0,
        "T": 0,
        "U": 0,
        "V": 0,
        "W": 0,
        "X": 0,
        "Y": 0,
        "Z": 0,
    }

    for i in range(len(content)):
        for j in range(len(alphabet)):
            if content[i].upper() == list(alphabet)[j]:
                to_update = list(alphabet.keys())[j]
                alphabet[to_update] += 1

for i in alphabet:
    print(f"{i}: {alphabet[i]}")
