numeros = []
while True:
    n = (int(input('Digite o numero : ')))
    if n not in numeros:
        numeros.append(n)
        print ("Valor Adicionado")
    else:
        print ('Valor ja existe')
    escolha = str(input('Deseja continuar S/N ')).upper()
    if escolha == 'N':
        break
print (f"Os numeros digitados foram {numeros}")
numeros.sort()
print (f"Os numeros em ordem crescente ficam {numeros}")
numeros.sort(reverse=True)
print (f"Os numeros em ordem decrescente ficam {numeros}")