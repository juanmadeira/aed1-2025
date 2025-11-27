import sys
texto = ["2345678"]
print("ponteiros texto --->", sys.getrefcount(texto))
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print("======================")
print("ponteiros texto --->", sys.getrefcount(texto))
print("ponteiros outro --->", sys.getrefcount(outro))