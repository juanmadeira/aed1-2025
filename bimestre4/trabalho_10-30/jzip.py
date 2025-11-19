# transformar arquivo texto em arquivo de extensão arbitrária compactado
def compactar(input_path="input.txt", output_path="output.jz"):
    id = 0
    keys = {}
    sequence = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word not in keys:
                    keys[word] = id
                    id += 1
                sequence.append(keys[word])

            if "\\n" not in keys:
                keys["\\n"] = id
                id += 1
            sequence.append(keys["\\n"])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(keys) + "\n")
        f.write(" ".join(map(str, sequence)))

    return f"\n:: Arquivo {input_path} compactado com sucesso para {output_path}\n"


def descompactar(input_path="output.jz", output_path="output_descompactado.txt"):
    with open(input_path, "r", encoding="utf-8") as f:
        dict_line = f.readline().strip()
        seq_line = f.readline().strip()

    keys = eval(dict_line)
    inv_keys = {}
    for word, idx in keys.items():
        inv_keys[idx] = word

    sequence = []
    for item in seq_line.split():
        item = item.strip()
        if item.isdigit():
            sequence.append(int(item))

    words = []
    for idx in sequence:
        token = inv_keys[idx]
        if token == "\\n":
            words.append("\n")
        else:
            words.append(token + " ")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("".join(words))

    return f"\n:: Arquivo {input_path} descompactado com sucesso para {output_path}\n"


def menu():
    print("")
    print("======== jzip.py ========")
    print(" O que deseja fazer?")
    print(" 1. Compactar arquivo")
    print(" 2. Descompactar arquivo")
    print(" 3. Sair")
    print("=========================")
    option = ""
    while option != "1" and option != "2" and option != "3":
        print(option)
        option = input("> ")
    print("\n")
    if option == "1":
        print("=== Compactar arquivo ===")
        print(" Insira o nome do arquivo para compactação")
        print(" (padrão: input.txt)")
        print("=========================")
        input_path = input("> ")
        if input_path == "":
            input_path = "input.txt"
        print(compactar(input_path))
        menu()
    elif option == "2":
        print("== Descompactar arquivo ==")
        print(" Insira o nome do arquivo para descompactação")
        print(" (padrão: output.jz)")
        print("==========================")
        input_path = input("> ")
        if input_path == "":
            input_path = "output.jz"
        print(descompactar(input_path))
        menu()
    else:
        print(":: Programa encerrado. Saindo...")
menu()
