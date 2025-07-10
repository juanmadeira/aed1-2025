# Leia nome completo, pronome de tratamento e mostre "pronome sobrenome, nome"
# Ex: nome = "João Silva", pronome = "Sr."
# Sr. Silva, João
completo = input("Insira o nome completo: ")
trat = input("Insira o pronome de tratamento: ")
nome = ""
sobrenome = ""
espaco = False

i = 0
while i < len(completo):
    if completo[i] == " ":
        espaco = True
    if not espaco:
        nome += completo[i]
    else:
        sobrenome += completo[i]
    i += 1

sobrenome += ", "
sobrenome = sobrenome.upper()
print(trat + sobrenome + nome)
