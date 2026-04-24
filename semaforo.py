from enum import Enum, auto
from dataclasses import dataclass

class Cordosemaforo (Enum):
    VERDE = auto ()
    AMARELO = auto ()
    VERMELHO = auto()

def main(semaforo: Cordosemaforo)->Cordosemaforo:
    '''calcular a cor do semaforo do transito, informando a cor atual e devolver
    a próxima cor
    exemplos:
    >>> main(Cordosemaforo.VERDE).name
    'AMARELO'
    >>> main(Cordosemaforo.AMARELO).name
    'VERMELHO'
    >>> main(Cordosemaforo.VERMELHO).name
    'VERDE'
    '''
    if semaforo == Cordosemaforo.VERDE:
        return Cordosemaforo.AMARELO
    
    elif semaforo == Cordosemaforo.AMARELO:
        return Cordosemaforo.VERMELHO
    
    else:
        return Cordosemaforo.VERDE