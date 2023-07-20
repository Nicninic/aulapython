notas = [] # vetor global, todas as funções podem ver e usar esse vetor

def preencherVetor(fim):
    for i in range(fim):
        num = int(input('Informe a {}ª0 nota   '.format(i+1)))
        notas.append(num) #adiciona notas no vetor


def consultarVetor(fim):
    for i in range(fim):
        print('{}ª Posição: {}'.format(i+1, notas[i]))



def apagarPosicao(posicao):
    if (len(notas) < posicao):
        print ('Impossivel remover pois o tamanho é menor que a posição')
    else:
        del(notas[posicao]) #excluindo dado do vetor

