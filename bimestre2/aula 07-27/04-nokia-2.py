# def nokia(codigo):
#     teclado = ["2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888", "9", "99", "999", "9999"]
#     texto = ""
#     for i in range(len(codigo)):
#         if codigo[i] == "0":
#             texto += " "
#         while codigo[i] != " ":
#             for j in range(len(teclado)):
#                 if codigo[i] in teclado[j]:
#                     if codigo[i] == teclado[j][0]:
#                         codigo += tecla * 1
#                     elif texto[i] == teclado[j][1]:
#                         codigo += tecla * 2
#                     elif texto[i] == teclado[j][2]:
#                         codigo += tecla * 3
#                     elif texto[i] == teclado[j][3]:
#                         codigo += tecla * 4
#     return texto
#
#
# codigo = input("Insira um código de teclado nokia: ")
# print(f"\n{nokia(codigo)}\n")
