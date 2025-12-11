def modificar_valor(valor):
    print("Dentro da função (antes da modificação):", valor)
    print("ID do objeto (antes da modificação):", id(valor))

    # Modificar o valor
    valor += 10

    print("Dentro da função (após a modificação):", valor)
    print("ID do objeto (após a modificação):", id(valor))


# Código principal
numero = 5

print("Antes da chamada da função:")
print("Valor:", numero)
print("ID do objeto:", id(numero))

modificar_valor(numero)

print("\nDepois da chamada da função:")
print("Valor:", numero)
print("ID do objeto:", id(numero))
