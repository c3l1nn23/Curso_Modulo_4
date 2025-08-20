from random import randint

jogadores = {}
jogos = []
cont = 1

for j in range(0,3):
    (input(f'Digite o nome do jogador {cont}º : ')) 
    dado = randint(1,6)
    print (dado)
    cont += 1