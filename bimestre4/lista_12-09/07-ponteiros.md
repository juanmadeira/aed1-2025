# 1)

> (fora) antes da chamada:

valor: 5, ID: X

> (dentro) antes da modificação:

valor: 5, ID: X

> (dentro) depois da modificação:

valor: 15, ID: Y

> (fora) depois da chamada:

valor: 5, ID: X

# 2)

O valor não é alterado fora da função pois variáveis são imutáveis, diferentemente de listas.

# 3)

Identificar o objeto exato que está sendo manipulado.

# 4)

Ao tratar de objetos imutáveis, o ponteiro pode ser o mesmo, mas o objeto em si, não. O que acontece é uma referência a outro objeto.