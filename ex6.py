#EXERCICIO 6 com funcao de deixar a gente doido
def sequencia(nono, num):
    for i in range(nono,num+1):
        print(i)


def coletarNono():
    nono = int(input('Informe um número inicial: '))
    return nono

def coletarNum(nono):
    num = int(input('Informe um número final: '))
    while (nono > num):
        print('ERROR! Por favor informe um numero maior que o anterior')
        num = int(input('Informe um número final: '))
    return num
#depois do if nono = coletarNono()
    #num = coletarNum(nono)

    #sequencia(nono, num)