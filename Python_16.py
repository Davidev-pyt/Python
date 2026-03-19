from random import randint
computador = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Sera que consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?  '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
         print('Mais....Tente Novamente')
        elif jogador > computador:
           print('Menos...Tente Novamente')
print('Acertou com {} tentativas parabéns'.format(palpites))