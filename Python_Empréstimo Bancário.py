#Empréstimo Bancário

casa = float(input('Digite o valor da casa R$'))
salario =  float(input('Qual é o salário mensal:'))
anos = int(input('Quantos anos de financiamento voçê deseja:'))
minimo = salario * 30 / 100
 
prestaçao =  casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa , anos), end=' ')
print('a prestação será de R${:.2f} '.format(prestaçao))

if prestaçao <= minimo:
    print('O Empréstimo pode ser Concedido')
else:
    print('Impréstimo Negado')