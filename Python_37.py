def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[031mTivemos um problema com os tipos de dados que voçê digitou! Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031m O usuário preferiu não informar os dados!\033[m')
            return 0 
        else:      return n 

def leiafloat(msg):
     while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[031mTivemos um problema com os tipos de dados que voçê digitou! Tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[031m O usuário preferiu não informar os dados!\033[m')
            return 0 
        else:      return n 

n1= leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Voçê digitou o número {n1}')
print(f'Voçê digitou o número {n2}')