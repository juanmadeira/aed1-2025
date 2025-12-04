class ContaBancaria():
    def __init__(self, titular, num, saldo):
        self.__titular__ = titular
        self.__num__ = num
        self.__saldo__ = saldo

    def __setSaldo__(self, valor):
        self.__saldo__ = valor

    def getSaldo(self):
        return self.__saldo__
    
    def __repr__(self):
        return f"Titular: {self.__titular__} | Conta: {self.__num__} | Saldo: {self.__saldo__}"