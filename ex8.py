
def somarInt():
    soma = 0 #instanciar variavel
    for i in range (1, 11,1):
        num = int(input('{}ºnumero:'.format(i)))
        soma += num

    return 'A soma dos inteiros é: {}'.format(soma)


