#declaração de classe
class gafanhoto:

    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem Nome e Idade.
    para criar uma nova pessoa, use
    variavel = gafanhoto(nome, idade)
    """
    def __init__(self,nome="",idade= 0):#metodo construtor
        #atributos de instancia
        self.nome = nome
        self.idade = idade

    #metodos de instancia
    def aniversario(self):
        self.idade = self.idade+1

    def __str__(self):
        return f'{self.nome} é Ganfanhoto (a) e tem {self.idade} anos de idade'

    def mensagem(self):
        return f'{self.nome} é Ganfanhoto (a) e tem {self.idade} anos de idade'
    def __getstate__(self):
        return f'Estado: nome= {self.nome} ; idade = {self.idade}'

#declaração de objetos
g1=gafanhoto('Maria',17)
g1.aniversario()
#print(g1.mensagem())

