num = soma = 0 
valores = 0
while True:
    num = int(input('Digite uma valor (999 para parar): '))     
    if num == 999: 
            break
    soma += num
    valores += 1
print(f'A soma dos {valores} valores digitados é igual a {soma}')