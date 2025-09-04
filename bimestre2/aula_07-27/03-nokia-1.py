def nokia(texto):
    teclado = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    texto = texto.lower()
    codigo = ""
    for i in range(len(texto)):
        if texto[i] == " ":
            codigo += "0"
        for j in range(len(teclado)):
            if texto[i] in teclado[j]:
                tecla = str(j + 2)
                if texto[i] == teclado[j][0]:
                    codigo += tecla * 1
                elif texto[i] == teclado[j][1]:
                    codigo += tecla * 2
                elif texto[i] == teclado[j][2]:
                    codigo += tecla * 3
                elif texto[i] == teclado[j][3]:
                    codigo += tecla * 4
        codigo += " "
    return codigo


texto = input("Insira um texto: ")
print(f"\n{nokia(texto)}\n")
