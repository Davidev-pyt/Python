import random 

print('-----Bem vindo ao jogo de adivinhação------')

computador = random.randint(1 , 5)
print('VOU PENSAR EM UM NUMERO...')

usuario = int(input('Digite um número entre (1 e 5): '))
if computador == usuario:
    print('Parabéns voçê acertou o numero!!')
    print('O número escolhido era {}'.format(computador))
else:
    print('Infelizmente voçê errou tente novamente!')
    print('O número escolhido era {}'.format(computador))

