galera = list()
dado = list() 
totmaio = totmeno = 0
for c in range(0 , 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
    for p in galera:
        if p[1] >= 21:
            print(f'{p[0]} maior de idade')
            totmaio += 1
        else:
            print(f'{p[0]} menor de idade')
            totmeno += 1
print(f'Temos {totmaio} maiores {totmeno} menores de idade')
