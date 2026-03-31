def ficha(jog='<desconhecido>' , gol=0):
    print(f'O {jog} fez {gol} gol(s) no campeonato.')
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
        gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
        ficha(gol=gols)
else:
        ficha(nome , gols)