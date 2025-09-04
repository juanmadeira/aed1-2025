def calculadora(n1, n2, op):
    if op == "+":
        return n1 + n2, op
    elif op == "-":
        return n1 - n2, op
    elif op == "*":
        return n1 * n2, op
    elif op == "/":
        return n1 / n2, op
    elif op == "%":
        return n1 % n2, op


n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

op = input("Insira a operação: ")
while op != "+" and op != "-" and op != "*" and op != "/" and op != "%":
    print("Erro. A operação deve ser +, -, *, / ou %.")
    op = input("Insira a operação: ")

result, op = calculadora(n1, n2, op)
print(f"\n{n1} {op} {n2} = {result}")
