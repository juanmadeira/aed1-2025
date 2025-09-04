# Verifique se uma string é formada apenas por letras

frase = input("Insira uma frase: ")
letras = "abcdefghijklmnopqrstuvwxyzáãâéẽêíĩîóõôúũû"
apenasLetras = 0

i = 0
while i < len(frase):
    j = 0
    while j < len(letras):
        if frase[i].lower() == letras[j]:
            apenasLetras += 1
        j += 1
    i += 1

if frase == "":
    print("A string não é formada apenas por letras.")
else:
    if apenasLetras == len(frase):
        print("A string é formada apenas por letras.")
    else:
        print("A string não é formada apenas por letras.")
