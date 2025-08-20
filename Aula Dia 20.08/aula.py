
# pessoas = {
#     "Nome" : "Marcelo",
#     "Idade" : 18,
#     "Sexo" : "Masculino",
# }
# print (pessoas.items())
# print (pessoas.values())
# print (pessoas.keys())

# for k in pessoas.keys():
#     print(f'As chaves são {k}')

# for v in pessoas.values():
#     print(f'As chaves são {v}')

# for i in pessoas.items():
#     print(f'As chaves são {i}')

# del pessoas['Idade']

# pessoas["Nome"] = 'Vitin'

# brasil = []
# estado1 = {}

# for c in range(0,3):
#     estado1['UF'] = input('Digite a Unidade Federativa : ')
#     estado1['Sigla'] = input('Digite a sigla do estado : ')
#     brasil.append(estado1.copy())
    
# print(brasil)

alunos = []
aluno = {}

while True:
    aluno['Nome'] = (input('Digite O Nome Do Aluno : '))
    aluno['Media'] = float(input('Digite a Media Do Aluno : '))
    alunos.append(aluno.copy())
    for v in aluno.values():
        if type(v) == float:
            if v >= 7:
                print (f'Aluno {aluno["Nome"]} está aprovado com a media {aluno["Media"]}')
            elif v <= 4 or v >= 6.9:
                print (f'Aluno {aluno["Nome"]} está em recuparação com a media {aluno["Media"]}')