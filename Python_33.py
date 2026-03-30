def fatorial(num=1, show=False):
    """Calcula o fatorial de um número.
    :param num: O número a ser calculado o fatorial (padrão é 1).
    :param show: (opcional) Se True, mostra a conta."""
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
        return f 








print(fatorial(5, show=True))