class contaBancaria:
    '''
    cria uma conta bancaria e permite fazer saques e depositos
    '''
    def __init__(self,id, nome,saldo =0):
        self.id = id
        self.titular= nome
        self.saldo = saldo
        print(f' A conta {self.id} criada com sucesso. Saldo atual é de R$ {self.saldo:,.2f} ')

    def __str__(self):
        return f' A conta {self.id} de {self.titular} tem R$ {self.saldo:,.2f} de saldo'

    def depositar(self,valor):
        self.saldo += valor
        print(f' Deposito de R${valor:,.2f}  autorizada na conta {self.id}')
    def saque(self,valor):
        if valor > self.saldo:
            print(f' saque Negado de R${valor:,.2f}  autorizada na conta {self.id} :saldo insuficiente')
        self.saldo -= valor
        print(f' saque de R${valor:,.2f}  autorizada na conta {self.id}')

c1= contaBancaria(id=112 , nome="Kalita", saldo=1000)
c1.depositar(500)
c1.saque(100)
print(c1)
