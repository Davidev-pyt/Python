matriz = [[0, 0, 0] for _ in range(3)]
spar = scol = mai = 0
for l in range(3):
    for c in range(3):
        valor = int(input(f'Digite um valor para [{l}, {c}]: '))
        matriz[l][c] = valor 

        if valor % 2 == 0:
            spar += valor

        if c == 2:
            scol += valor

        if l == 1:
            if c == 0 or valor > mai:
                mai = valor
print('-=' * 23)
for linha in matriz:
    for item in linha:
        print(f'[{item:^5}]', end=' ')
    print()
print('-=' * 23)
print(f'A soma dos pares é {spar}')
print(f'A soma da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')