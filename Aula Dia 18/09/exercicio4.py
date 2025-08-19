num = []
pares = []
impares = []

while True:
    num.append(int(input(f'Digite um numero : ')))
    resp = (input('Quer continuar ? [ S/N ] : ')).upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else :
        impares.append(v)
print(f'A lista completa é : {num} ')
print(f'A lista de numeros pares é : {pares} ')
print(f'A lista de numeros impares é : {impares} ')
