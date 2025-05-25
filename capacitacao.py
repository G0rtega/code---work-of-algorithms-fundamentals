from enum import Enum,auto
from dataclasses import dataclass

class Regiao(Enum):
    SUL= 1.0
    SUDESTE = 1.1
    CENTRO_OESTE = 1.2
    NORDESTE = 1.3
    NORTE = 1.4

@dataclass

class Produto:
    codigo: int
    nome: str
    preco: float
    categoria: str
    estoque:int
    peso: float
    altura:float
    largura:float
    comprimento:float
    volume: float
    seguro: float

def calcula_frete(produto1: Produto, regiao:Regiao):
    '''A empresa tamb ́em precisa calcular o valor do frete com base no peso e dimensões do produto.
    Regras de negócio:
    • O frete base é calculado com base no peso do produto = peso X 0.5
    • O frete por volume é calculado com base no volume do produto = volume X 0.001
    • O frete por seguro é calculado com base no valor do produto = valor do produto X 0.01
    Além disso o valor do frete varia conforme a região onde será entrega
    exemplos:
    >>> produto1 = produto(1, 'teste', 100.0, 'geral', 10, 1.0, 1000.0, 10.0)
    >>> calcula_frete(produto1, Regiao.SUL)
    1.6
    '''
    fpeso = produto1.peso * 0.5
    fvolume = produto1.volume * 0.001
    fseguro = produto1.seguro * 0.01
    base_frete = fpeso + fvolume + fseguro
    frete_total = base_frete + regiao.value
    return frete_total

def main():
    codigo = int(input('digite o codigo do produto:'))
    nome = input('digite qual o nome do produto: ')
    preco = float(input('digite o preco(rr.cc): '))
    categoria = input('digite qual a categoria do produto:')
    estoque = int(input('digite qual o estoque do produto: '))
    peso = float(input('digite qual o peso em kg(kk.gg): '))
    altura = float(input('digite a altura do produto: '))
    largura = float(input('digite a largura do produto: '))
    comprimento = float(input('digite o comprimento do produto: '))
    volume = float(input('digite o volume: '))
    seguro = float(input('digite o valor do seguro: '))
    regiao_input = input('escolha a regiao (SUL, SUDESTE, CENTRO_OESTE, NORDESTE, NORTE): ').upper()
    regiao = Regiao[regiao_input]
    produto1 = Produto(codigo, nome, preco, categoria, estoque, peso,altura, largura, comprimento, volume, seguro)
    frete = calcula_frete(produto1, regiao)

    print(f"valor do frete: R${frete:.2f}")
    return frete

if __name__ =='__main__':
    main()