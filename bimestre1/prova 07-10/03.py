# Uma sequência de DNA é composta por duas Hélices com as proteínas Timina, Guanina, Adenina e Citosina
# Sabendo que as duas cadeias devem ter o mesmo tamanho e que as ligações devem ser sempre A-T ou C-G
# Crie um programa em Python que leia cada um dos lados de uma cadeia de DNA e verifique se a cadeia é válida.

lado1 = input("Insira o primeiro lado da cadeia de DNA: ").upper()
while lado1 == "":
    lado1 = input("Apenas são aceitos os caracteres \"A, T, C e G\". Insira o primeiro lado da cadeia de DNA: ").upper()

i = 0
while i < len(lado1):
    while lado1 == "" or (lado1[i] != "A" and lado1[i] != "T" and lado1[i] != "C" and lado1[i] != "G"):
        lado1 = input("Apenas são aceitos os caracteres \"A, T, C e G\". Insira o primeiro lado da cadeia de DNA: ").upper()
    i += 1

lado2 = input("Insira o segundo lado da cadeia de DNA: ").upper()
while lado2 == "":
    lado2 = input("Apenas são aceitos os caracteres \"A, T, C e G\". Insira o segundo lado da cadeia de DNA: ").upper()

i = 0
while i < len(lado2):
    while lado2 == "" or (lado2[i] != "A" and lado2[i] != "T" and lado2[i] != "C" and lado2[i] != "G"):
        lado2 = input("Apenas são aceitos os caracteres \"A, T, C e G\". Insira o segundo lado da cadeia de DNA: ").upper()
    i += 1

if len(lado1) == len(lado2):
    erro = False
    i = 0
    while i < len(lado1):
        if lado1[i] == "T":
            if lado2[i] != "A":
                erro = True
        elif lado1[i] == "C":
            if lado2[i] != "G":
                erro = True
        i += 1
    if erro:
        print("ERRO! As ligações devem ser sempre A-T ou C-G. A cadeia é INVÁLIDA.")
    else:
        print(f"\nLado 1: {lado1}")
        print(f"Lado 2: {lado2}")
        print("\nA cadeia é VÁLIDA!")
else:
    print("\nERRO! As cadeias não são do mesmo tamanho, portanto, a cadeia é INVÁLIDA.")
