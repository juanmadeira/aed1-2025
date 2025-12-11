def ordenacao_por_selecao(array, tamanho):
    for elemento_i in range(tamanho):
        indice_minimo = elemento_i

        # encontra o índice do menor elemento na parte não ordenada
        for elemento_j in range(elemento_i + 1, tamanho):
            if array[elemento_j] < array[indice_minimo]:
                indice_minimo = elemento_j

        # trocar o menor elemento com o elemento atual
        if indice_minimo != elemento_i:
            array[elemento_i], array[indice_minimo] = array[indice_minimo], array[elemento_i]


array = [64, 25, 12, 22, 11]
tamanho = len(array)
print("array antes da ordenação:", array)

ordenacao_por_selecao(array, tamanho)

print("array após a ordenação:", array)