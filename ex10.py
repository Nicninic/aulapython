#Exercicio 10 Escreva um algoritmo que calcule a
#média dos números digitados pelo
#usuário, se eles forem pares. Termine a
#leitura se o usuário digitar zero 0

def exercicio10():
    contador = 1
    num = 1
    soma = 0

    while(num != 0):
         num = int(input(' Informe um número: '))
#verifico se o no é par ou impar
         if (num % 2 == 0):
             soma += num #soma os pares
             contador += 1 #contando os pares


    return 'A soma é {} e a média é {}'.format(soma/contador)
