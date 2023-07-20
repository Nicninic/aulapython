#Exercício 13 Escreva um programa que lido um
#número, calcule e informe o seu fatorial
#Ex 5! 5 4 3 2 1 120.


def exercicio13():

    fat = 1
    i = 1

    num = int(input(' Informe um número: '))

    while(num <= 0):
        print(' Valores negativos, decimais ou fracionados são inválidos, informe um número positivo')
        num = int(input(' Informe um número: '))

    else:
        while(i <= num):
            fat *= i
            i += 1


    print('O fatorial do número {}! é: {} '.format(num, fat))