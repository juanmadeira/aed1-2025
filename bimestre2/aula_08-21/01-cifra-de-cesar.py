# cifra de césar

def cesar(text, shift):
    text = list(text.upper())
    cypher = ""
    ascii = 0
    for i in range(len(text)):
        ascii = ord(text[i]) + shift
        if ascii > 90:
            ascii = 65
        cypher += chr(ascii)
    return cypher


text = input("Insira um texto para cifrar: ")
shift = int(input("Insira um passo para a cifra: "))
print(f"\ntexto: {text.upper()} \ncifra: {cesar(text, shift)}")
