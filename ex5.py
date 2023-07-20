# construa um programa que exiba a tabuada de 1 ate n

def tabuada(num, n):
    for i in range (1, n+1):
        print ('{} * {} = {}'.format(num, i, num*i))
def coletarPositivo():
    num = int(input('Informe um número: '))
    while(num < 0):
        print('ERROR! PLEASE INFORM A POSITIVE NUMBER')
        num = int(input('Informe um número: '))
    return num
    #executa a funcao
    num = int(input('Informe um número: '))
    n = coletarPositivo()
    # passar os dois numeros na funcao
    tabuada(num, n)
    # print(somarInteiro())