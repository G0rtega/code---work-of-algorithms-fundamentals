import sys
def le_arquivo(nome: str) -> list[str]:
    '''
Le o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento
representa uma linha.
Por exemplo, se o conteúdo do arquivo for
Sao-Paulo 1 Atletico-MG 2
Flamengo 2 Palmeiras 1
a resposta produzida  ́e
['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1']
'''
    try:
        with open(nome) as f:
            return f.readlines()
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.')
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)
    if len(sys.argv) > 2:
        print('Muitos parâmetros. Informe apenas um nome de arquivo.')
        sys.exit(1)
    jogos = le_arquivo(sys.argv[1])
    partidas = transformar_em_partidas(jogos, 0, [])
    times = coletar_nomes(jogos, 0, [])
    maior = tamanho_do_maior_time(times, 0, 0)
    matriz = criar_matriz(times, partidas, 0, [])
    melhores_times, aproveitamento = pergunta_2_melhor_aproveitamento_anfitriao(times, partidas, 0, [], 0)
    print("\n📊Melhor aproveitamento como mandante:")
    for t in melhores_times:
        print(f"{t.nome} com {aproveitamento}% de aproveitamento")
    pergunta_3_melhor_defesa(times, jogos)
    remover_espacos_matriz(matriz, 0)
    matriz = ordenar_classificacao(matriz)
    ajustar_tamanho_dos_nomes(matriz, 0, maior)
    imprimir_classificacao_final(matriz, 0)

    # TODO: solucao da pergunta 1
def meu_split(palavra: str, separador: str = ' ') -> list[str]: # para não usar a função split do python
        '''Essa função divide uma string em uma lista de substrings, usando um limite especificado.
        Exemplos:
        >>> meu_split('Flamengo 2 Vasco 1', ' ')
        ['Flamengo', '2', 'Vasco', '1']
        >>> meu_split('Palmeiras 1 Corinthians 1', ' ')
        ['Palmeiras', '1', 'Corinthians', '1']
        >>> meu_split('Grêmio 0 Inter 2', ' ')
        ['Grêmio', '0', 'Inter', '2']
        '''
        lista = []
        palavra_atual = ''
        i = 0

        while i < len(palavra):
            if palavra[i] != separador:
                palavra_atual += palavra[i]
            else:
                if palavra_atual != '':
                    lista.append(palavra_atual)
                    palavra_atual = ''
            i += 1
        if palavra_atual != '':
            lista.append(palavra_atual)
        return lista

def remover_espacos_nome(nome, i):
    '''Essa função remove espaços e quebras de linha dos times, retornando ele sem esses caracteres.
    Exemplos:
    >>> remover_espacos_nome('Sao-Paulo 1', 0)
    'Sao-Paulo1'
    >>> remover_espacos_nome('Flamengo 2', 0)
    'Flamengo2'
    >>> remover_espacos_nome('Palmeiras 1', 0)
    'Palmeiras1'
    '''
    if i == len(nome):
        return ''
    if nome[i] in (' ', '\n', '\r'):
        return remover_espacos_nome(nome, i + 1)
    return nome[i] + remover_espacos_nome(nome, i + 1)
from dataclasses import dataclass
@dataclass
class Time:
    nome: str
    pontos: int = 0
    vitorias: int = 0
    saldo: int = 0
def remover_espacos_matriz(matriz:list[Time], i: int) -> list[Time]:
    '''Essa função remove espaços e quebras de linha de todos os nomes na matriz, retornando a matriz sem esses caracteres.
    Exemplos:
    >>> remover_espacos_matriz([Time(nome='Sao-Paulo 1'), Time(nome='Atletico-MG 2')], 0)
    [Time(nome='Sao-Paulo1', pontos=0, vitorias=0, saldo=0), Time(nome='Atletico-MG2', pontos=0, vitorias=0, saldo=0)]
    >>> remover_espacos_matriz([Time(nome='Flamengo 2'), Time(nome='Palmeiras 1')], 0)
    [Time(nome='Flamengo2', pontos=0, vitorias=0, saldo=0), Time(nome='Palmeiras1', pontos=0, vitorias=0, saldo=0)]
    '''
    if i == len(matriz):
        return matriz
    matriz[i].nome = remover_espacos_nome(matriz[i].nome, 0)
    remover_espacos_matriz(matriz, i + 1)
    return matriz

def coletar_nomes(jogos: list[str], i: int, times: list[Time]) -> list[Time]:
    '''Essa função coleta os nomes dos times a partir das partidas, adicionando-os a uma lista se ainda não estiverem lá.
    Exemplos:   
    >>> coletar_nomes(['Sao-Paulo 1 Atletico-MG 2', 'Flamengo 2 Palmeiras 1'], 0, [])
    [Time(nome='Sao-Paulo', pontos=0, vitorias=0, saldo=0), Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=0), Time(nome='Flamengo', pontos=0, vitorias=0, saldo=0), Time(nome='Palmeiras', pontos=0, vitorias=0, saldo=0)]
    >>> coletar_nomes(['Palmeiras 1 Corinthians 1', 'Grêmio 0 Inter 2'], 0, [])
    [Time(nome='Palmeiras', pontos=0, vitorias=0, saldo=0), Time(nome='Corinthians', pontos=0, vitorias=0, saldo=0), Time(nome='Grêmio', pontos=0, vitorias=0, saldo=0), Time(nome='Inter', pontos=0, vitorias=0, saldo=0)]
    '''
    if i == len(jogos):
        return times
    partidas = meu_split(jogos[i], ' ')
    time_anfitriao = remover_espacos_nome(partidas[0], 0)
    time_visitante = remover_espacos_nome(partidas[2], 0)
    if not time_na_lista(times, time_anfitriao, 0):
        times.append(Time(nome=time_anfitriao))
    if not time_na_lista(times, time_visitante, 0):
        times.append(Time(nome=time_visitante))
    return coletar_nomes(jogos, i + 1, times)
       
def time_na_lista(lista: list[Time], item: str, i: int) -> bool:
    '''Essa função verifica se um item está na lista, retornando True ou False.
    Exemplos:
    >>> time_na_lista([Time(nome='Sao-Paulo'), Time(nome='Atletico-MG')], 'Sao-Paulo', 0)
    True
    >>> time_na_lista([Time(nome='Flamengo'), Time(nome='Palmeiras')], 'Vasco', 0)
    False
    '''
    if i == len(lista):
        return False
    if lista[i].nome == item: 
        return True
    return time_na_lista(lista, item, i + 1)
       
def tamanho_do_maior_time(times: list[Time], i: int = 0, maior: int = 0) -> int:
        '''Essa função retorna o tamanho do maior time da lista de times.
        Exemplos:
        >>> tamanho_do_maior_time([Time('Sao-Paulo'), Time('Atletico-MG')], 0, 0)
        11
        >>> tamanho_do_maior_time([Time('Flamengo'), Time('Palmeiras')], 0, 0)
        9
        >>> tamanho_do_maior_time([Time('Palmeiras'), Time('Corinthians')], 0, 0)
        11
        '''
        if i == len(times):
            return maior
        if len(times[i].nome) > maior:
            maior = len(times[i].nome)
        return tamanho_do_maior_time(times, i + 1, maior)
    
def ajustar_tamanho_dos_nomes(times: list[Time], i: int, tamanho: int) -> list[Time]:
        '''Essa função ajusta o tamanho dos nomes dos times para que todos tenham o mesmo tamanho, adicionando espaços no final.
        Exemplos:
        >>> ajustar_tamanho_dos_nomes([Time('Sao-Paulo'), Time('Atletico-MG')], 0, 11)
        [Time(nome='Sao-Paulo  ', pontos=0, vitorias=0, saldo=0), Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=0)]
        >>> ajustar_tamanho_dos_nomes([Time('Flamengo'), Time('Palmeiras')], 0, 9)
        [Time(nome='Flamengo ', pontos=0, vitorias=0, saldo=0), Time(nome='Palmeiras', pontos=0, vitorias=0, saldo=0)]
        >>> ajustar_tamanho_dos_nomes([Time('Palmeiras'), Time('Corinthians')], 0, 11)
        [Time(nome='Palmeiras  ', pontos=0, vitorias=0, saldo=0), Time(nome='Corinthians', pontos=0, vitorias=0, saldo=0)]
        '''
        if i == len(times):
            return times
        while len(times[i].nome) < tamanho:
            times[i].nome += ' '
        return ajustar_tamanho_dos_nomes(times, i + 1, tamanho)
    
def ordenar_classificacao(matriz: list[Time], i: int = 0) -> list[Time]:
    '''Essa função ordena a matriz de classificação dos times, considerando pontos, vitorias e saldo de gols.
    Exemplos:
    >>> ordenar_classificacao([Time('Sao-Paulo', 3, 1, 2), Time('Atletico-MG', 4, 2, 1)], 0)
    [Time(nome='Atletico-MG', pontos=4, vitorias=2, saldo=1), Time(nome='Sao-Paulo', pontos=3, vitorias=1, saldo=2)]
    >>> ordenar_classificacao([Time('Flamengo', 2, 1, 1), Time('Palmeiras', 3, 2, 0)], 0)
    [Time(nome='Palmeiras', pontos=3, vitorias=2, saldo=0), Time(nome='Flamengo', pontos=2, vitorias=1, saldo=1)]
    >>> ordenar_classificacao([Time('Palmeiras', 1, 0, 0), Time('Corinthians', 1, 0, 0)], 0)
    [Time(nome='Corinthians', pontos=1, vitorias=0, saldo=0), Time(nome='Palmeiras', pontos=1, vitorias=0, saldo=0)]
    '''
    if i == len(matriz) - 1:
        return matriz
    j = i + 1
    while j < len(matriz):
        a, b = matriz[i], matriz[j]
        if (b.pontos > a.pontos) or \
           (b.pontos == a.pontos and b.vitorias > a.vitorias) or \
           (b.pontos == a.pontos and b.vitorias == a.vitorias and b.saldo > a.saldo) or \
           (b.pontos == a.pontos and b.vitorias == a.vitorias and b.saldo == a.saldo and b.nome < a.nome):
            aux = matriz[i]
            matriz[i] = matriz[j]
            matriz[j] = aux
        j += 1
    return ordenar_classificacao(matriz, i + 1)

from dataclasses import dataclass
@dataclass
class Partida:
    anfitriao: str
    ganho1: int
    visitante: str
    ganho2: int

def criar_matriz(times: list[Time], partidas: list[Partida], i: int, matriz: list[Time] = []) -> list[Time]:
    '''Cria a matriz de classificação dos times, preenchendo com pontos, vitorias e saldo de gols.
    Exemplos:
    >>> criar_matriz([Time(nome='Flamengo')], [Partida('Flamengo', 2, 'Vasco', 1)], 0, [])
    [Time(nome='Flamengo', pontos=3, vitorias=1, saldo=1)]
    >>> criar_matriz([Time(nome='Sao-Paulo'), Time(nome='Atletico-MG')], [Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, [])
    [Time(nome='Sao-Paulo', pontos=0, vitorias=0, saldo=-1), Time(nome='Atletico-MG', pontos=3, vitorias=1, saldo=1)]
    '''
    if i == len(times):
        return matriz
        
    time = times[i]
    pontos = calcular_pontos(partidas, 0, time.nome, 0)
    vitorias = calcular_numero_de_vitorias(partidas, 0, time.nome, 0)
    saldo = calcular_o_saldo_de_gols(partidas, 0, time.nome, 0)
    matriz.append(Time(nome=time.nome, pontos=pontos, vitorias=vitorias, saldo=saldo))
    return criar_matriz(times, partidas, i + 1, matriz)

def transformar_em_partidas(jogos: list[str], i: int, partidas: list[Partida]) -> list[Partida]:
    '''Transforma strings de jogos em objetos Partida.
    Exemplos:
    >>> transformar_em_partidas(['Sao-Paulo 1 Atletico-MG 2'], 0, [])
    [Partida(anfitriao='Sao-Paulo', ganho1=1, visitante='Atletico-MG', ganho2=2)]
    >>> transformar_em_partidas(['Flamengo 2 Palmeiras 1'], 0, [])
    [Partida(anfitriao='Flamengo', ganho1=2, visitante='Palmeiras', ganho2=1)]
    '''
    if i == len(jogos):
        return partidas
    
    elementos = meu_split(jogos[i], ' ') 
    partidas.append(Partida(
    anfitriao=remover_espacos_nome(elementos[0], 0), 
    ganho1=int(elementos[1]),
    visitante=remover_espacos_nome(elementos[2], 0),  
    ganho2=int(elementos[3])))
    return transformar_em_partidas(jogos, i + 1, partidas)

def calcular_pontos(partidas: list[Partida], i: int, time: str, pontos: int = 0) -> int:
    '''Calcula os pontos de um time em todos os jogos.
    Exemplos corrigidos:
    >>> calcular_pontos([Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, 'Sao-Paulo', 0)
    0
    >>> calcular_pontos([Partida('Flamengo', 2, 'Palmeiras', 1)], 0, 'Flamengo', 0)
    3
    >>> calcular_pontos([Partida('Palmeiras', 1, 'Corinthians', 1)], 0, 'Palmeiras', 0)
    1
    '''
    if i == len(partidas):
        return pontos
    partida = partidas[i]
    if time == partida.anfitriao:
        if partida.ganho1 > partida.ganho2:
            pontos += 3
        elif partida.ganho1 == partida.ganho2:
            pontos += 1  
    elif time == partida.visitante:
        if partida.ganho2 > partida.ganho1:
            pontos += 3
        elif partida.ganho2 == partida.ganho1:
            pontos += 1  
    return calcular_pontos(partidas, i + 1, time, pontos)
        
def calcular_numero_de_vitorias(partidas: list[Partida], i: int, time: str, vitorias: int = 0) -> int:
    '''Essa função calcula o número de vitórias de um time em todos os jogos, retornando o total de vitórias.
    Exemplos:
    >>> calcular_numero_de_vitorias([Partida(anfitriao='Sao-Paulo', ganho1=1, visitante='Atletico-MG', ganho2=2)], 0, 'Sao-Paulo', 0)
    0
    >>> calcular_numero_de_vitorias([Partida(anfitriao='Flamengo', ganho1=2, visitante='Palmeiras', ganho2=1)], 0, 'Flamengo', 0)
    1
    >>> calcular_numero_de_vitorias([Partida(anfitriao='Palmeiras', ganho1=1, visitante='Corinthians', ganho2=1)], 0, 'Palmeiras', 0)
    0
    '''
    if i == len(partidas):
        return vitorias
        
    partida = partidas[i]
    if time == partida.anfitriao and partida.ganho1 > partida.ganho2:
        vitorias += 1
    elif time == partida.visitante and partida.ganho2 > partida.ganho1:
        vitorias += 1
    return calcular_numero_de_vitorias(partidas, i + 1, time, vitorias)
    
def calcular_o_saldo_de_gols(partidas: list[Partida], i: int, time: str, saldo: int = 0) -> int:
    '''Calcula o saldo de gols de um time.
    Exemplos:
    >>> calcular_o_saldo_de_gols([Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, 'Sao-Paulo', 0)
    -1
    >>> calcular_o_saldo_de_gols([Partida('Flamengo', 2, 'Palmeiras', 1)], 0, 'Flamengo', 0)
    1
    >>> calcular_o_saldo_de_gols([Partida('Palmeiras', 1, 'Corinthians', 1)], 0, 'Palmeiras', 0)
    0
    '''
    if i == len(partidas):
        return saldo    
    partida = partidas[i] 
    if time == partida.anfitriao:
        saldo += partida.ganho1 - partida.ganho2
    elif time == partida.visitante:
        saldo += partida.ganho2 - partida.ganho1   
    return calcular_o_saldo_de_gols(partidas, i + 1, time, saldo)

def ordem_alfabética_clubes(matriz: list[Time], j: int, limite: int) -> list[Time]:
    '''Essa função define a ordem de desempate da matriz de times em ordem alfabética, considerando pontos, vitorias e saldo de gols.
    Exemplos:
    >>> ordem_alfabética_clubes([
    ...     Time(nome='Sao-Paulo', pontos=3, vitorias=1, saldo=1),
    ...     Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=-1)
    ... ], 0, 1)
    [Time(nome='Sao-Paulo', pontos=3, vitorias=1, saldo=1), Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=-1)]
    '''
    if j == limite:
        return matriz
    a = matriz[j]
    b = matriz[j + 1]
    aux = False  
    if a.pontos < b.pontos:
        aux = True
    elif a.pontos == b.pontos:
        if a.vitorias < b.vitorias:
            aux = True
        elif a.vitorias == b.vitorias:
            if a.saldo < b.saldo:
                aux = True
            elif a.saldo == b.saldo:
                nome_a = a.nome
                nome_b = b.nome
                i = 0
                while i < len(nome_a) and i < len(nome_b):
                    posicao_a = nome_a[i]
                    posicao_b = nome_b[i]
                    if posicao_a != posicao_b:
                        if posicao_a > posicao_b:
                            aux = True
                        else:
                            aux = False
                    i += 1
                if not aux and len(nome_a) > len(nome_b):
                    aux = True
    if aux:
        troca = matriz[j]
        matriz[j] = matriz[j + 1]
        matriz[j + 1] = troca
    return ordem_alfabética_clubes(matriz, j + 1, limite)
    
def imprimir_classificacao_final(matriz: list[Time], i: int, espacamento: int = None) -> list[Time]:
    '''Essa função imprime a classificação final dos times no campeonato.
    Exemplos:
    >>> imprimir_classificacao_final([Time(nome='Sao-Paulo', pontos=3, vitorias=1, saldo=2), 
    ...                             Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=-1)], 0)
    <BLANKLINE>
    ========================================
    🏆 Classificação Final do Campeonato
    ========================================
    <BLANKLINE>
    Sao-Paulo    : 3 pontos, 1 vitórias, saldo de gols: 2
    Atletico-MG  : 0 pontos, 0 vitórias, saldo de gols: -1
    <BLANKLINE>
    [Time(nome='Sao-Paulo', pontos=3, vitorias=1, saldo=2), Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=-1)]
    '''
    if i == 0:
        espacamento = tamanho_do_maior_time(matriz) + 2  
        print("\n" + "="*40)
        print("🏆 Classificação Final do Campeonato")
        print("="*40 + "\n")
    
    if i < len(matriz):
        time = matriz[i]
        print(f"{time.nome:<{espacamento}}: {time.pontos} pontos, {time.vitorias} vitórias, saldo de gols: {time.saldo}")
        return imprimir_classificacao_final(matriz, i + 1, espacamento)  
    else:
        print()
        return matriz

# TODO: solucao da pergunta 2

def pontos_como_anfitrião(partidas: list[Partida], i: int, time: str, pontos: int = 0) -> int:
    '''Essa função calcula os pontos de um time como anfitrião em todos os jogos, retornando o total de pontos.
    Exemplos:
    >>> pontos_como_anfitrião([Partida(anfitriao='Sao-Paulo', ganho1=1, visitante='Atletico-MG', ganho2=2)], 0, 'Sao-Paulo', 0)
    0
    >>> pontos_como_anfitrião([Partida(anfitriao='Flamengo', ganho1=2, visitante='Palmeiras', ganho2=1)], 0, 'Flamengo', 0)
    3
    >>> pontos_como_anfitrião([Partida(anfitriao='Palmeiras', ganho1=1, visitante='Corinthians', ganho2=1)], 0, 'Palmeiras', 0)
    1
    '''
    if i == len(partidas):
        return pontos
    
    partida = partidas[i]
    if time == partida.anfitriao:
        if partida.ganho1 > partida.ganho2:
            pontos += 3
        elif partida.ganho1 == partida.ganho2:
            pontos += 1
    
    return pontos_como_anfitrião(partidas, i + 1, time, pontos)

def jogos_como_anfitrião(partidas: list[Partida], i: int, time: str, total: int = 0) -> int:
    '''Essa função conta o número de jogos que um time jogou como anfitrião, retornando o total de jogos.
    Exemplos:
    >>> jogos_como_anfitrião([Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, 'Sao-Paulo', 0)
    1
    >>> jogos_como_anfitrião([Partida('Flamengo', 2, 'Palmeiras', 1)], 0, 'Flamengo', 0)
    1
    >>> jogos_como_anfitrião([Partida('Palmeiras', 1, 'Corinthians', 1)], 0, 'Palmeiras', 0)
    1
    '''
    if i == len(partidas):
        return total
    partida = partidas[i]
    if time == partida.anfitriao:
        total += 1
    return jogos_como_anfitrião(partidas, i + 1, time, total)

def pergunta_2_melhor_aproveitamento_anfitriao(times: list[Time], partidas: list[Partida], i: int, melhores_times: list[Time], melhor_aproveitamento: int):
    '''Essa função encontra o time com o melhor aproveitamento como anfitrião, retornando o nome do time e o aproveitamento.
    Exemplos:
    >>> pergunta_2_melhor_aproveitamento_anfitriao([Time('Sao-Paulo'), Time('Atletico-MG')], [Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, [], 0)
    ([Time(nome='Sao-Paulo', pontos=0, vitorias=0, saldo=0), Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=0)], 0)
    >>> pergunta_2_melhor_aproveitamento_anfitriao([Time('Flamengo'), Time('Palmeiras')], [Partida('Flamengo', 2, 'Palmeiras', 1)], 0, [], 0)
    ([Time(nome='Flamengo', pontos=0, vitorias=0, saldo=0)], 100)
    >>> pergunta_2_melhor_aproveitamento_anfitriao([Time('Palmeiras'), Time('Corinthians')], [Partida('Palmeiras', 1, 'Corinthians', 1)], 0, [], 0)
    ([Time(nome='Palmeiras', pontos=0, vitorias=0, saldo=0)], 33)
    '''
    if i == len(times):
        return melhores_times, melhor_aproveitamento
    
    time_atual = times[i]
    pontos = pontos_como_anfitrião(partidas, 0, time_atual.nome, 0)
    total_jogos = jogos_como_anfitrião(partidas, 0, time_atual.nome, 0)
    if total_jogos > 0:
        aproveitamento = (pontos * 100) // (total_jogos * 3)
    else:
        aproveitamento = 0
    if aproveitamento > melhor_aproveitamento:
        melhores_times = [time_atual]
        melhor_aproveitamento = aproveitamento
    elif aproveitamento == melhor_aproveitamento:
        melhores_times.append(time_atual)
    
    return pergunta_2_melhor_aproveitamento_anfitriao(times, partidas, i + 1, melhores_times, melhor_aproveitamento)
    
    # TODO: solucao da pergunta 3
def gols_sofridos(partidas: list[Partida], i: int, time: str, total: int = 0) -> int:
    '''Essa função calcula o número de gols sofridos por um time em todos os jogos, retornando o total de gols sofridos.
    Exemplos:
    >>> gols_sofridos([Partida('Sao-Paulo', 1, 'Atletico-MG', 2)], 0, 'Sao-Paulo', 0)
    2
    >>> gols_sofridos([Partida('Flamengo', 2, 'Palmeiras', 1)], 0, 'Flamengo', 0)
    1
    >>> gols_sofridos([Partida('Palmeiras', 1, 'Corinthians', 1)], 0, 'Palmeiras', 0)
    1
    '''
    if i == len(partidas):
        return total
    partida = partidas[i]

    if time == partida.anfitriao:
        total += partida.ganho2
    elif time == partida.visitante:
        total += partida.ganho1
    return gols_sofridos(partidas, i + 1, time, total)
from dataclasses import dataclass
@dataclass
class ResultadoDefesa:
    melhores_times: list[Time]
    gols_sofridos: int

def defesa_menos_vazada(times: list[Time], partidas: list[Partida], i: int, resultado: ResultadoDefesa) -> ResultadoDefesa:
    '''Essa função encontra o time com a defesa menos vazada, retornando o time com melhor defesa.
    Exemplos:
    >>> times = [Time(nome='Sao-Paulo'), Time(nome='Atletico-MG')]
    >>> partidas = [Partida(anfitriao='Sao-Paulo', ganho1=1, visitante='Atletico-MG', ganho2=2)]
    >>> resultado = defesa_menos_vazada(times, partidas, 0, ResultadoDefesa([], -1))
    >>> resultado.gols_sofridos
    1
    >>> len(resultado.melhores_times)
    1
    >>> resultado.melhores_times[0].nome
    'Atletico-MG'
    
    >>> times = [Time(nome='Flamengo'), Time(nome='Palmeiras')]
    >>> partidas = [Partida(anfitriao='Flamengo', ganho1=2, visitante='Palmeiras', ganho2=1)]
    >>> resultado = defesa_menos_vazada(times, partidas, 0, ResultadoDefesa([], -1))
    >>> resultado.gols_sofridos
    1
    '''
    if i == len(times):
        return resultado
    time_atual = times[i]
    sofridos = gols_sofridos(partidas, 0, time_atual.nome, 0)
    if resultado.gols_sofridos == -1 or sofridos < resultado.gols_sofridos:
        resultado.gols_sofridos = sofridos
        resultado.melhores_times = [time_atual]
    elif sofridos == resultado.gols_sofridos:
        resultado.melhores_times.append(time_atual)
    return defesa_menos_vazada(times, partidas, i + 1, resultado)

def pergunta_3_melhor_defesa(times: list[Time], jogos: list[str]) -> list[Time]:
    '''Essa função encontra o time com a defesa menos vazada.
    Exemplos:
    >>> pergunta_3_melhor_defesa([Time(nome='Sao-Paulo'), Time(nome='Atletico-MG')], ['Sao-Paulo 1 Atletico-MG 2'])
    <BLANKLINE>
    ----------------------------------------
    🛡️ Defesa menos vazada do campeonato
    ----------------------------------------
    Atletico-MG com 1 gols sofridos
    [Time(nome='Atletico-MG', pontos=0, vitorias=0, saldo=0)]
    >>> pergunta_3_melhor_defesa([Time(nome='Flamengo'), Time(nome='Palmeiras')], ['Flamengo 2 Palmeiras 1'])
    <BLANKLINE>
    ----------------------------------------
    🛡️ Defesa menos vazada do campeonato
    ----------------------------------------
    Flamengo com 1 gols sofridos
    [Time(nome='Flamengo', pontos=0, vitorias=0, saldo=0)]
    '''
    print("\n" + "-"*40)
    print("🛡️ Defesa menos vazada do campeonato")
    print("-"*40)
    partidas = transformar_em_partidas(jogos, 0, [])
    resultado = defesa_menos_vazada(times, partidas, 0, ResultadoDefesa([], -1))
    for time in resultado.melhores_times:
        print(f"{time.nome} com {resultado.gols_sofridos} gols sofridos")
    return resultado.melhores_times
if __name__ == '__main__':
    main()
# Trabalho de implementação fundamentos de algoritmos-
# professor:  Flavio Uber 
# aluno: Gabriel Ortega


