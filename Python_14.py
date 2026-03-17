num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para converção
      [1] Coverter para BINÁRIO
      [2] Converter para OCTAL
      [3] converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num , bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num , hex(num)[2:]))
else :
    print( 'opção invalida!')