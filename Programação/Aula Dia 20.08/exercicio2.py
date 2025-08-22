from random import randint

jogos = []
cont = 1

for j in range(0,4):
    
    jogador = {}
    jogador ['Nome'] = (input(f'Digite o nome do jogador {cont}º : \n')).capitalize()
    cont += 1
    jogador['Dado'] = randint(1,6)
    jogos.append(jogador.copy())
ranking = sorted(jogos, key=lambda x: x['Dado'],reverse=True)

print ('Ranking Final')
for i,j in enumerate(ranking, start=1):
    print(f'{i}º lugar foi {j['Nome']} com o numero {j['Dado']}\n')