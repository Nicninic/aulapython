#Exercício 11 Escreva um algoritmo que leia valores
#inteiros e encontre o maior e o menor
#deles. Termine a leitura se o usuário
#digitar zero (0)


def exercicio11():
    num = 1
    i = 0
    maior = 0
    menor = 0
    flag = false


    while (num != 0):
        num = int(input(' Informe um número: '))
#primeira vez a gente instancia a variavel somente na primeira vez. e o detalhe é q se avisa ao codigo
    #   quando é a primeira vez,
        if (num!= 0):
            if(flag == false):
                maior = num
                menor = num
                flag = true
    #definir maior e menor

            if(num > maior):
                maior = num

            if(num < menor):
                menor = num

    return 'O número maior é: {} e o número menor é {}'.format(maior, menor)
