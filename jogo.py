def jogo(horas: int, nivel: int) -> int:
    ''' receber o nivel atual de um jogador de um jogo qualquer e a 
    quantidade de horas jogadas em uma semana e calcular o novo nível dos jogadores
    exemplos:
    >>> jogo(3,4)
    3
    >>> jogo(4,12)
    12
    >>> jogo (6, 21)
    22'''
    if  horas <4:
        novo_nivel = nivel - (4 - horas)
    elif horas <=5:
        novo_nivel = nivel
    else:
        if horas -5 >= 7:
            novo_nivel = nivel + 7
        else:
            novo_nivel = (nivel + (horas - 5))
    if novo_nivel >= 25:
        return 25
    if novo_nivel <0:
        return 0
    
    return novo_nivel
