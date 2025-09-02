# peça uma senha e verifique se ela é válida segundo as regras:
# 1. pelo menos 8 caracteres
# 2. contém pelo menos uma letra maiúscula, uma minúscula e um número
# 3. não pode ter espaços

def validatePassword(password):
    # 8 caracteres
    if len(password) < 8:
        return "SENHA INVÁLIDA! ❌ É necessário que ela possua pelo menos 8 caracteres."

    # uma letra maiúscula, uma minúscula e um número
    if password.islower():
        return "SENHA INVÁLIDA! ❌ É necessário que ela possua pelo menos uma letra maiúscula."
    if password.isupper():
        return "SENHA INVÁLIDA! ❌ É necessário que ela possua pelo menos uma letra minúscula."
    if password.isalpha():
        return "SENHA INVÁLIDA! ❌ É necessário que ela possua pelo menos um número."
    if password.isnumeric():
        return "SENHA INVÁLIDA! ❌ É necessário que ela possua pelo menos uma letra maiúscula e uma letra minúscula."

    # espaços
    passList = list(password)
    for i in range(len(passList)):
        if passList[i] == " ":
            return "SENHA INVÁLIDA! ❌ Não são permitidos espaços."
    return "Senha VÁLIDA! ✅"


password = input("Insira uma senha: ")
print(f"\n{validatePassword(password)}")
