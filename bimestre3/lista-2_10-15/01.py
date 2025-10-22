# faça um programa em python para ler “n” números inteiros, armazenando-os em uma lista
# (o usuário informará um valor inteiro positivo para “n”)
# após, crie duas outras listas a partir desta primeira digitada, sendo que uma conterá os números positivos (>= 0),
# e a outra conterá os números negativos. Mostre na tela como ficaram as três listas.
n = []
while True:
    n.append(input("Insira um número inteiro: "))
    if n[-1] == "":
        n.pop()
        break

positivos = [] 
negativos = [] 
for i in n:
    i = int(i)
    if i >= 0:
        positivos.append(i)
    else:
        negativos.append(i)
    
print(f"\nLista original: {n}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
