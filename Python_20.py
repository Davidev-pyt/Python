listanum = []
maior = menor = 0
for count in range(0 , 5):
    listanum.append(int(input(f'Digite um valor para a posição {count}: '))) 

    maior =  max(listanum)
    menor = min(listanum)
  
pos_maior = [ i for i , v in enumerate(listanum) if v == maior]
pos_menor = [i for i, v in enumerate(listanum) if v == menor]

print(f'O maior valor foi {maior} nas posições{pos_maior}')
print(f'O menor valor foi {menor} nas posições {pos_menor}')