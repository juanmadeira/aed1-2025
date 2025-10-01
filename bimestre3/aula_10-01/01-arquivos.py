with open("01-arquivos.txt", "r") as arq:
    arq.seek(6)  # desloca o ponteiro
    conteudo = arq.read()
    print(arq)
    print(conteudo)

print(arq.read())  # ValueError: I/O operation on closed file.
