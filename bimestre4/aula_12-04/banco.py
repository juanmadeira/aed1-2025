from Cliente import Cliente
from ContaBancaria import ContaBancaria

x = Cliente()
x.setIdentificacao("João", "001.002.003-04")
y = ContaBancaria("João", "012345678-9", "10")
x.setConta(y)

print(x)