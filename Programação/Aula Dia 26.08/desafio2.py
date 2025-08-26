saldo = 0
class Saldo():
    def __init__(self,valor):
        self.valor = valor
    def depositar(self):
        global saldo 
        saldo += self.valor
        print(f'Saldo é = R$ {self.valor}')
        
depositar = float(input('Qual valor deseja depositar ? '))
deposito = Saldo(depositar)
deposito.depositar()