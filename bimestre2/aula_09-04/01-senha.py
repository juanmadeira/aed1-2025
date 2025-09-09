# crie uma função que "quebre" uma senha
# para facilitar, considere testes com números + letras maiúsculas

# INCOMPLETO

def quebraSenha(senha):
    senha = senha.upper()
    tentativa = ""
    # A-Z (65-90)
    # 0-9 (48-57)
    for i in range(len(senha)):
        print(tentativa)
    if testaSenha(tentativa, senha):
        return senha
    else:
        quebraSenha(senha)


def testaSenha(tentativa, senha):
    tentativa = tentativa.upper()
    if tentativa == senha:
        return True
    return False


senha = "SENHA123"
# senha = input("Insira uma senha: ")
print(quebraSenha(senha))
