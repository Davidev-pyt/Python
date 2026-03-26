pessoas = []
princ = []
maior = menor = 0
while True: 
    nome = (str(input('Nome: ')))
    peso = (float(input('Peso: ')))
    princ.append([nome , peso])
    if len(princ) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 20)

print(f'Ao todo voçê cadastrou {len(princ)} pessoas' )
print(f'O maior peso cadastrado foi de {maior}Kg peso de ', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]} ' , end =' ')
print()
print(f'O menor peso cadastrado foi de {menor}Kg peso de ', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'{p[0]} ', end=' ')
print()

