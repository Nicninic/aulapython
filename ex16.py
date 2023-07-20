#calcular percentual de branco nulo votante
def coletarPositivoInteiro
    num = int(input())
    while (num <= 0):
        print ('Erro!! Informe um valor positivo')
        num = int(input('Informe um numero: '))
    return num

def transformarPercentual(num,total):
    percentual = (num / total) * 100
    return percentual

def Eleicao
    print('Informe o total de votos brancos:')
    brancos = coletarPositivoInteiro()
    print('Informe o total de votos nulos: ')
    nulos = coletarPositivoInteiro()
    print('Informe o total de votos validos: ')
    validos = coletarPositivoInteiro()

    total = coletarPositivoInteiro()
    #verificar se o total é igual aos votos
    if ((brancos+nulos+validos) == total):
        pBrancos = transformarPercentual(brancos, total)
        pNulos = transformarPercentual(nulos,total)
        pValidos = transformarPercentual(validos,total)
        return 'Votos Brancos: {}% \n Votos Nulos: {}% \nVotos Validos: {}%'.format(pBrancos,pNulos,pValidos)

    else:
        return 'Numero de votos é diferente do total de eleitores, digite novamente!!!!'
