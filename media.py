def media(n1: float)-> str:
    ''' calcular a media final de um aluno de acordo com suas notas
    exemplos:
    >>> media(3.0)
    'D'
    >>> media(6.0)
    'C'
    >>> media(8.0)
    'B'
    >>> media(9.0)
    'A'
    '''
    if n1 <= 4.9:
        return 'D'
    elif n1 <= 6.9:
        return 'C'
    elif n1 <= 8.9:
        return 'B'
    else:
        return 'A'