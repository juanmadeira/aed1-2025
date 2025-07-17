def boasVindas(nome="Viajante"):
    print(f"Bem-vindo, {nome}!")


nome = input("Insira seu nome: ")
if nome == "":
    boasVindas()
else:
    boasVindas(nome)
