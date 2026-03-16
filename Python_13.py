#Radar Eletrônico
 
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO!! Voçê excedeu o limite da via')
    multa = (velocidade - 80) * 7
    print('Voçê deve pagar uma multa de {:.2f}'.format(multa))
else:
    print('Tenha um bom dia! dirija com segurança')