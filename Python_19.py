from random import randint
v = 0 
print('=' * 25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=' * 25)
escolha = ' '
while True:
    jogador = int(input('Digite um valor: '))
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    total = jogador + computador
    print('-' * 25)
    print(f'Voçê jogou {jogador} e o computador jogou {computador} e o total foi de {total}')
    print('-' * 25)
    if escolha == 'P':
        if total %2 == 0:
            print('Voçê ganhou!!')
            v += 1
        else:
            print('Voçê Perdeu!!')
            break
    elif escolha == 'I':
        if total %2 != 0:
            print('Voçê Venceu!!')
            v += 1
        else:
            print('Voçê Perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER voçê venceu {v} vezes')