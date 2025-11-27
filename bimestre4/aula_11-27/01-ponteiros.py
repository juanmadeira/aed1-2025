texto = "foo"
print(texto, id(texto))
texto += "bar"
print(texto, id(texto))
print("======================")
texto = "foo"
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print("======================")
print(texto, id(texto))
print(outro, id(outro))
print("======================")
texto = ["A", "B", "C"]
print(texto, id(texto))
texto[0] = "X"
print(texto, id(texto))
texto.pop()
print(texto, id(texto))
print("======================")
texto = ["A", "B", "C"]
outro = texto
print(texto, id(texto))
print(outro, id(outro))
print("======================")
texto.append("D")
print(texto, id(texto))
print(outro, id(outro))