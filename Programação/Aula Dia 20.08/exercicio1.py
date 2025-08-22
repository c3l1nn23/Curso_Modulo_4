
alunos = []

while True:
    aluno = {}
    aluno['Nome'] = (input('Digite O Nome Do Aluno : '))
    aluno['Media'] = float(input('Digite a Media Do Aluno : '))
    alunos.append(aluno)
    
    for v in aluno.values():
        if type(v) == float:
            if v >= 7:
                print (f'-='*30)
                print (f'\nAluno {aluno["Nome"]} está aprovado com a media {aluno["Media"]}\n')
                print (f'-='*30)
            elif 4 <= v < 7:
                print (f'-='*30)
                print (f'\nAluno {aluno["Nome"]} está em recuperação com a media {aluno["Media"]}\n')
                print (f'-='*30)
            else:
                print (f'-='*30)
                print (f'\n,Aluno {aluno["Nome"]} foi reprovado com a media {aluno["Media"]}\n')
                print (f'-='*30)
    escolha = input('Deseja verificar mais alunos ? [S/N] ').upper()
    if escolha == 'N':
        break
    
print("\n📋 Lista final de alunos:")
for a in alunos:
    print(f'Nome: {a["Nome"]}, Média: {a["Media"]}')