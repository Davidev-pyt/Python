aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'A média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'

for k , v in aluno.items():
    print(f'{k} é igual a {v}')