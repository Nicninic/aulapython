#Exercício 14 Escreva um programa que leia um valor
#correspondente ao número de jogadores de
#um time de vôlei. O programa deverá ler
#uma altura para cada um dos jogadores e, ao
#final, informar a altura média do time.


def exercicio14():
    media = 0
    somaAltura = 0
    quantidade = int(input('Informe a quantidade de jogadores do time: '))
    num = 1

    for i in range(quantidade):
        num = float(input(' Informe a altura do {}º jogador: '.format(i+1)))
        somaAltura += num


    media = somaAltura / quantidade
    return( 'A média da altura dos jogadores é {}'.format( media))