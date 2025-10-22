# faça um programa, em python, que leia um arquivo texto contendo uma lista de endereços IP
# a partir dos IPs lidos, gere dois outros arquivos, um contendo os endereços IP válidos
# (quanto ao formato), e outro contendo os endereços inválidos.
# o formato de um endereço IP é num1.num.num.num, onde 1 ≤ num1 ≤ 255  e 0 ≤ num ≤ 255.
def verifyIP(file):
    with open(file, "r") as file:
        content = file.readlines()
        ip_all = []
        ip_valid = []
        ip_invalid = []

        for i in range(len(content)):
            ip_all.append(content[i].strip().split("."))

        for i, ii in enumerate(ip_all):
            if len(ii) != 4:
                ip_invalid.append(content[i])
            else:
                for j, jj in enumerate(ip_all[i]):
                    if not jj:  # vazio
                        ip_invalid.append(content[i])
                        break
                    else:
                        if "-" in jj:
                            ip_invalid.append(content[i])
                            break
                        else:
                            if j == 0:
                                if int(jj) < 1 or int(jj) > 255:
                                    ip_invalid.append(content[i])
                                    break
                            else:
                                if int(jj) < 0 or int(jj) > 255:
                                    ip_invalid.append(content[i])
                                    break
                    if j == 3:
                        ip_valid.append(content[i])

        with open("14-validos.txt", "w") as file:
            for i in ip_valid:
                file.write(i)
        with open("14-invalidos.txt", "w") as file:
            for i in ip_invalid:
                file.write(i)

verifyIP("14.txt")

with open("14.txt", "r") as file:
    print("\nTodos IPs:")
    print(file.read())

with open("14-validos.txt", "r") as file:
    print("\nIPs válidos:")
    print(file.read())

with open("14-invalidos.txt", "r") as file:
    print("\nIPs inválidos:")
    print(file.read())
