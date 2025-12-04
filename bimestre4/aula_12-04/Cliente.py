class Cliente:
    def __init__(self):
        self.__nome__ = ""
        self.__cpf__= ""
        self.__conta__ = False

    def __validaCPF__(self, cpf):
        if len(cpf) == 14:
            return True
        return False
    
    def setConta(self, ContaBancaria: object):
        self.__conta__ = ContaBancaria.__num__
    
    def setIdentificacao(self, nome, cpf):
        self.__nome__ = nome
        if self.__validaCPF__(cpf):
            self.__cpf__ = cpf
        else:
            print(f"ERRO: CPF inválido")

    def __repr__(self):
        saida = f"Cliente: {self.__nome__} | CPF: {self.__cpf__}"
        if self.__conta__:
            saida += f" | Conta: {self.__conta__}"
        return saida