# vendedor = 'Marcelo'
# meta = float(input('Qual foi o valor de venda do vendedor ? '))
# if meta >= 500:
#     print (f"{vendedor} Bateu a meta")
# else:
#     print(f"{vendedor} não bateu a meta")

# class Vendas():
#     def __init__(self, nome):
#         self.nome = nome
#         self.vendas = 0
#     def vendeu(self,vendas):
#         self.vendas = vendas
#     def bateumeta (self,meta):
#         if self.vendas >= meta:
#              print(f'{self.nome} bateu a meta')
#         else:
#             print(f'{self.nome} não bateu a meta')
            
# vendedor1 = Vendas('Marcelo')
# vendedor1.vendeu(1000)
# vendedor1.bateumeta(600)

# vendedor1 = Vendas('Tralaleiro Tralala')
# vendedor1.vendeu(1000)
# vendedor1.bateumeta(500)

class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def exibir(self):    
        print(f"Meu nome é {self.nome} e tenho {self.idade} de Idade")


        
nome = input('Qual o nome da pessoa ? ')
idade = input(f'Qual a idade do {nome} ? ')
apresentacao = Pessoa(nome,idade)
apresentacao.exibir()