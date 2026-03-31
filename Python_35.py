# Codigo Principal
import teste

p = float(input("Digite o valor do produto R$ "))
print(f'A metade de R${p} é R${teste.metade(p)}')
print(f'O dobro de R${p} é R${teste.dobro(p)}')
t = float(input('Digite a taxa de aumento: '))
print(f'Aumentando {t}% temos R${teste.aumentar(p , t)}')
t = float(input('Digite a taxa de redução: '))
#print(f'Reduzindo {t}% temos R${teste.diminuir(p , t)}')