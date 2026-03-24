listanum = []
maior = menor = 0
for count in range(0 , 5):
    listanum.append(int(input(f'Digite um valor para a posição {count}: '))) 

    maior =  max(listanum)
    menor = min(listanum)
  
print('-=' * 30)
print(f'Voçê digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições',end=' ')

for i, v in enumerate(listanum):
     if v == maior:
      print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {menor} nas posições', end=' ')
for i , v in enumerate(listanum):
     if v == menor:
          print(f'{i}...', end=' ')
print()
