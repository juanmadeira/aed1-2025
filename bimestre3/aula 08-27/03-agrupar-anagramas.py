# dada uma lista de palavras, agrupe as que são anagramas
# entrada   →   ["amor", "roma", "carro", "roca", "arco"]
# saída     →   [["amor", "roma"], ["carro"], ["roca", "arco"]]

# def anagram(term1, term2):
#     term1 = sorted(list(term1))
#     term2 = sorted(list(term2))
#     if term1 == term2:
#         return True
#     else:
#         return False
#
#
# term1 = input("Insira o primeiro termo: ")
# term2 = input("Insira o segundo termo: ")
# print(anagrama(term1, term2))

# def groupAnagrams(list):
#     listSorted = []
#     anagrams = []
#     for i in range(len(list)):
#         listSorted.append(sorted(list[i]))
#         for j in range(len(listSorted)):
#             if i != j:
#                 if listSorted[i] == listSorted[j]:
#                     anagrams.append([])
#                     for k in range(len(anagrams)):
#                         anagrams[k].append(list[i])
#                         anagrams[k].append(list[j])
#     return listSorted, anagrams

def groupAnagrams(list):
    listSorted = []
    anagrams = []
    for i in range(len(list)):
        listSorted.append(sorted(list[i]))
        for j in range(len(listSorted)):
            if i != j:
                if listSorted[i] == listSorted[j]:
                    anagrams.append([])
                    for k in range(len(anagrams)):
                        anagrams[k].append(list[i])
                        anagrams[k].append(list[j])
    return listSorted, anagrams

list = []
while True:
    list.append(input("Insira uma palavra para inserir à lista (vazio encerra): "))
    print(list[-1])
    if list[-1] == "":
        list.pop(-1)
        break

print(list)
print(groupAnagrams(list))
