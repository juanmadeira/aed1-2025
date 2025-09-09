# implemente uma função recursiva eh_palindromo(texto)
# que receba uma string e retorne True se for palíndromo e False caso contrário
# (desconsiderando espaços, acentos e diferenças entre maiúsculas/minúsculas)

def eh_palindromo(texto):
    texto = texto.upper()
    texto = texto.replace(" ", "")
    palindromo = ""
    i = 1
    while i <= len(texto):
        palindromo += texto[-i]
        i += 1

    if palindromo == texto:
        return True
    else:
        return False


texto = input("Insira um possível palíndomo: ")
if eh_palindromo(texto):
    print("\nÉ palíndromo!")
else:
    print("\nNão é palíndromo!")
