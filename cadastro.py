from enum import Enum, auto
from dataclasses import dataclass

class cadastro_secao(Enum):
    LOGISTICA=auto()
    FINANCEIRO=auto()
    MANUTENCAO=auto()

from dataclasses import dataclass

@dataclass
class informacao:
    nome: str
    cpf: str
    data_de_nascimento: str
    setor: cadastro_secao

def main():
    nome = input("Digite o nome do funcionario: ")
    cpf = input("Digite o CPF do funcionario: ")
    data_de_nascimento = input("Digite a data de nascimento do funcionario: ")
    setor = int(input("Digite o setor do funcionario 1-LOGISTICA, 2-FINANCEIRO, 3-MANUTENCAO: ")) 
    setorx = atribui_setor(setor)
    funcionario = informacao(nome, cpf, data_de_nascimento, setorx)
    funcionario_trabalha = atribui_funcionario(nome, cpf, data_de_nascimento, setorx)
    print('funcionario trabalha nessa secao: ',funcionario_trabalha)
    print('setor do funcionario cadastrado: ',retorna_setor(funcionario))

def atribui_setor(setor:int) -> cadastro_secao:
    '''Atribui o setor do funcionario de acordo com o número digitado pelo usuário
    exemplos:
    >>> atribui_setor(2).name
    'FINANCEIRO'
    >>> atribui_setor(3).name
    'MANUTENCAO'
    >>> atribui_setor(1).name
    'LOGISTICA'
    '''
    if setor == 1:
        return cadastro_secao.LOGISTICA
    elif setor == 2:
        return cadastro_secao.FINANCEIRO
    else:
        return cadastro_secao.MANUTENCAO
    
def atribui_funcionario(nome:str, cpf:str, data_de_nascimento:str, setor:cadastro_secao) -> bool:
    '''informar se o funcionario trabalha ou não nessa secao
    exemplos:
    >>> atribui_funcionario('João', '12345678900', '01/01/1990', cadastro_secao.LOGISTICA)
    True
    >>> atribui_funcionario('Maria', '98765432100', '02/02/1985', cadastro_secao.FINANCEIRO)
    True
    >>> atribui_funcionario('carlos', '45678912300', '03/03/1995', cadastro_secao.MANUTENCAO)
    True
    '''
    funcionario = informacao(nome, cpf, data_de_nascimento, setor)
    if funcionario.setor == setor:
        return True
    else:
        return False

def retorna_setor(funcionario:informacao) -> str:
    '''retorna o setor do funcionario
    exemplos:
    >>> retorna_setor(informacao('João', '12345678900', '01/01/1990', cadastro_secao.LOGISTICA))
    'LOGISTICA'
    >>> retorna_setor(informacao('Maria', '98765432100', '02/02/1985', cadastro_secao.FINANCEIRO))
    'FINANCEIRO'
    >>> retorna_setor(informacao('Carlos','98272738291' '03/03/1995', cadastro_secao.MANUTENCAO))
    'MANUTENCAO'
    '''
    return funcionario.setor.name

if __name__ == "__main__":
    main()  
