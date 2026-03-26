valores = []

while True:
     valores.append(int(input('Digite um valor: ')))
     resp = str(input('Quer continuar [S/N]')).strip().upper()[0]
     if resp in 'N':
        break
print('-=' * 30)
print(f'Voçê digitou {len(valores)} elementos')
valores.sort(reverse= True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O número 5 esta na lista')
else:
    print('O número 5 não esta na lista')
    