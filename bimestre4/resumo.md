## 1. Dicionários

```python
aluno = {"nome": "João", "idade": 20, "curso": "ADS"}

print(aluno["nome"])       # João
print(aluno.get("idade"))  # 20

aluno["idade"] = 21        # atualiza valor
aluno["matricula"] = 12345 # insere novo par

del aluno["curso"]         # remove a chave "curso"
idade = aluno.pop("idade") # remove e retorna o valor

for chave, valor in aluno.items():
    print(chave, valor)

for chave in aluno.keys():
    print(chave)

for valor in aluno.values():
    print(valor)

len(aluno)         # Número de elementos
"nome" in aluno    # Verifica se a chave existe
aluno.clear()      # Limpa o dicionário
```

---

## 2. Ponteiros

* Variáveis em Python são **referências a objetos** na memória.
* Alterações em objetos mutáveis afetam todas as referências que apontam para ele.

```python
a = [1, 2, 3]
b = a  # b referencia o mesmo objeto que a
b.append(4)
print(a)  # [1, 2, 3, 4]
```

### 2.1 Comparações de referência vs valor

```python
x = [1, 2]
y = x
z = x.copy()  # cria uma cópia independente

x is y  # True, mesma referência
x is z  # False, referência diferente
x == z  # True, mesmo conteúdo
```

### 2.2 Passagem de parâmetros

* Funções recebem **referências** para objetos.
* Objetos mutáveis podem ser alterados dentro da função.
* Objetos imutáveis não podem ser alterados diretamente.

```python
def adiciona_elemento(lista):
    lista.append(10)

nums = [1, 2, 3]
adiciona_elemento(nums)
print(nums)  # [1, 2, 3, 10]
```

> Evitando efeitos indesejados

Criar **cópias** de objetos mutáveis para não alterar o original:

```python
lista1 = [1, 2, 3]
lista2 = lista1.copy()  # cópia superficial
```