def Primeira_maiuscula(palavra:str)->str:
    ''' recebe uma string frase e produz a mesma frase
 mas com a primeira letra em maiúscula.
 exemplos:
 >>> Primeira_maiuscula('joao')
 'Joao'
 >>> Primeira_maiuscula('pedro')
 'Pedro'
 '''
    return palavra [0].upper() + palavra [1:]
for i in range(50):

    nome = str (input('digite um nome:'))
    print (Primeira_maiuscula(nome))