# mantenha duas listas: produtos e quantidades
# o programa deve permitir adicionar produto, remover e vender (diminuindo quantidade)
# se um produto esgotar, deve removê-lo das listas

products = []
quantity = []
def addProduct():
    newProduct = input("\nInsira um produto para ser adicionado: ")
    if newProduct in products:
        quantity[products.index(newProduct)] += 1
    else:
        products.append(newProduct)
        quantity.append(int(1))
    selectMode()


def rmProduct():
    rm = input("\nInsira um produto para ser removido: ")
    products.pop(products.index(rm))
    quantity[products.index(rm)] -= 1
    selectMode()


def listProducts():
    print(f"Produtos: {products}\nQuantidades: {quantity}")
    selectMode()


def selectMode():
    mode = 0
    mode = int(input("\n1. Adicionar produto\n2. Remover produto\n3. Vender produto\n4. Ver produtos\n0. Encerrar\n\nO que fazer? "))

    if mode == 1:
        return print(addProduct())
    if mode == 2:
        return print(rmProduct())
    if mode == 4:
        return print(listProducts())
    elif mode == 0:
        print("\nPrograma encerrado.")
        listProducts()
    else:
        return print("Nenhuma opção válida foi inserida. Programa encerrado.")

    return print("Nenhuma opção válida foi inserida. Programa encerrado.")

print(selectMode())
