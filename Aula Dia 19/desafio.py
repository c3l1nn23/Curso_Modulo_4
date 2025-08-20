from random import randint
import time

lista = []
jogos = []
cont = 1
print('-='*8, 'Jogo Do Marcelão', '-='*8)
quant = int(input('Informe a quantidade de jogos que deseja fazer\nR: '))
total = 1
while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-='*6, f'Sorteando {quant} Jogos', '-='*6)
for i, n in enumerate(jogos):
    time.sleep(1)
    print(f'{i+1} Jogo: {n}')
time.sleep(1)
print('-='*6, f'Boa Sorte!', '-='*6)