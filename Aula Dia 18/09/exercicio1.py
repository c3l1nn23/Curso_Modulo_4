numeros = []

for i in range(0, 5):
    numeros.append(int(input(f"Digite o número na posição {i}: ")))
maior = max(numeros)
menor = min(numeros)

print(f"A lista dos números digitados é: {numeros}")
print(f"O maior número é {maior} e ele está nas posições: ", end='')

for ind, num in enumerate(numeros):
    if num == maior:
        print(f'{ind}...', end='')
print() 

print(f"O menor número é {menor} e ele está nas posições: ", end='')
for ind, num in enumerate(numeros):
    if num == menor:
        print(f'{ind}...', end='')
print()
