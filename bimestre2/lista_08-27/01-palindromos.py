# dada uma lista de strings, crie um programa que retorne apenas as que são palíndromos

def palindrome(list):
    palindromes = []
    for i in range(len(list)):
        if list[i] == list[i][::-1]:
            palindromes.append(list[i])
    return palindromes


list = []
while True:
    list.append(input("Insira uma palavra para inserir à lista (vazio encerra): "))
    print(list[-1])
    if list[-1] == "":
        list.pop(-1)
        break

palindromes = []
palindromes = palindrome(list)
if len(palindromes) == 0:
    print("Nenhuma das palavras inseridas são palíndromos.")
else:
    print("Das palavras inseridas, estas são palíndromos:")
    for i in range(len(palindromes)):
        print(palindromes[i])
