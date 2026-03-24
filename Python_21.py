numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Número duplicado ele não sera adicionado!')

    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
numeros.sort()
print(f"Voçê digitou os valores {numeros}")

