class Conta(object):
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_saldo(self):
        return self.saldo
    def __str__(self):
        s = f'Nome: {self.nome}, R$ {self.saldo}'
        return s
    def deposito(self, valor):
        self.saldo += valor
    def retirada(self, valor):
        self.valor -= valor
    def retirada_rn(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor

class Conta_PF(Conta):
    def __init__(self, nome, saldo=0.0, genero='m', cpf=''):
        super().__init__(nome, saldo)
        self.genero = genero
        self.cpf = cpf
    def get_genero(self):
        return self.genero
    def set_genero(self, novo_genero):
        self.genero = novo_genero
    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

class Conta_PJ(Conta):
    def __init__(self, nome, saldo=0.0, modalidade='MEI', cnpj=''):
        super().__init__(nome,saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj
    def get_modalidade(self):
        return self.modalidade
    def get_cnpj(self):
        return self.cnpj
    def set_cnpj(self, novo_cnpj):
        self.cnpj = novo_cnpj

if __name__ == '__main__':
    c = Conta('Alice')
    print(c)
    print('- Superclasse: \nNome:', c.get_nome())
    print('Saldo:', c.get_saldo())
    c.set_nome('Emily')
    print('Nome alterado: ', c.get_nome())
    print(c.__str__())
    pf1 = Conta_PF('Ana', 3000.0, 'f', '1234')
    print(pf1)
    print('Pessoa Física 1: \nNome:', pf1.get_nome())
    print('Saldo:', pf1.get_saldo())
    pf2 = Conta_PF('Ailton', 7000.0)
    print(pf2)
    print('- Pessoa Física 2:\nNome: ', pf2.get_nome())
    print("Saldo:", pf2.get_saldo())
    print('CPF:', pf2.get_cpf())
    pf2.set_cpf('123456789')
    print('Saída usando as funções vars e __dict__ d python:')
    print(vars(pf2))
    print(pf2.__dict__)
    pj1 = Conta_PJ('Café ABC', 15000.0)
    print(pj1)
    print('- Pessoa Jurídica:\nNome: ', pj1.get_nome())
    print('Saldo:',pj1.get_saldo())
    print('CNPJ:',pj1.get_cnpj())
    print(pj1)
    print(vars(pj1))
    print(pj1.__dict__)





