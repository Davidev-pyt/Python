try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que voçê digitou')

except(ZeroDivisionError):
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
else:  print(f'O resultado é {r:.1f}')

finally:  print('Volte sempre! Muito obrigado!')