def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return (f'com {idade} anos: Não VOTA.')
    elif 16 <= idade <18:
        return (f'com {idade} anos: voto OPCIONAL.')
    elif idade >= 18 and idade < 65:
        return(f'Com {idade} anos: voto OBRIGATÓRIO.')
    else:
        return('com {idade} anos: voto OPCIONAL')
    
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))