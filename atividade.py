def produto_anterior_posterior(n1: int) -> int:
    '''
    Calcula o produto de n, n + 1 e n - 1

    Exemplos:
    >>> produto_anterior_posterior(3)
    24
    >>> produto_anterior_posterior(1)
    0
    >>> produto_anterior_posterior(-2)
    -6
    '''
    return n1 * (n1 + 1) * (n1 - 1)

# pede um número ao usuário
while True:
    n1 = int(input('Digite um número inteiro: '))
    print(produto_anterior_posterior(n1))