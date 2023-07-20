
from ex1 import dobro
from ex1 import triplo
from ex2 import reajuste
from ex3 import parImpar
from ex3 import positivoNegativo
from ex4 import somarInteiro
from ex5 import tabuada
from ex5 import coletarPositivo
from ex6 import sequencia
from ex7 import Impar
from ex8 import somarInt
from ex9 import somarNumero
from ex10 import exercicio10
from ex11 import exercicio11
from ex12 import exercicio12
from ex13 import exercicio13
from ex14 import exercicio14
from ex15 import miss

from vetores import apagarPosicao
from vetores import preencherVetor
from vetores import consultarVetor






def mostrarMenu():
    print(' Escolha uma das opções abaixo: ' +
            '\n0 SAIR '              +
            '\n01. Ex1 ' +
            '\n02. Ex2 ' +
            '\n03. Ex3'  +
            '\n04. Ex4'  +
            '\n05. Ex5'  +
            '\n06. Ex6'  +
            '\n07. Ex7'  +
            '\n08. Ex8'  +
            '\n09. Ex9'  +
            '\n10. Ex10'  +
            '\n11. Ex11'  +
            '\n12. Ex12'  +
            '\n13. Ex13'  +
            '\n14. Ex14'  +
            '\n15. Ex15'  +
            '\n16. Ex16'  +
            '\n17. Ex17'  +
            '\n18. Ex18'  +
            '\n19. Ex19'  +
            '\n20. Ex20'  +
            '\n21. Preencher vetor'  +
            '\n22. Consultar vetor'  +
            '\n23. Apagar posição Vetor')



def operacao(): #Chamar o método de cima
    opcao = 1
    while( opcao != 0):
        mostrarMenu()
        opcao = int(input(' Digite aqui o número da opção escolhida: '))           #Coletar a opção do usuário
        if(opcao == 0):
            print (' Obrigado! ')
        elif(opcao == 1):
            print('\nEx1')
            num = int(input('Informe um número: '))
            print(dobro(num))
            print(triplo(num))
        elif(opcao == 2):
            print('\nEx2')
            num = int(input('Informe um número: '))
            print(reajuste(num))
        elif (opcao == 3):
            print('\nEx3')
            num = int(input('Informe um número: '))
            print(parImpar(num))
            print(positivoNegativo(num))
        elif (opcao == 4):
            print('\nEx4')
            print(' A soma do número um ao cem é: {}'.format(somarInteiro()))
        elif (opcao == 5):
            print('\nEx5')
            num = int(input(' Informe um número: '))
            n = coletarPositivo()
            tabuada(num, n)
        elif (opcao == 6):
            print('\nEx6')
            num = int(input(' Informe o número inicial: '))
            n = int(input('Informe o número final: '))
            sequencia(num, n)
        elif (opcao == 7):
            print('\nEx7')
            print('\n Lista dos números ímpares de 100 a 200 completa!'.format(Impar()))
        elif (opcao == 8):
            print('\nEx8')
            print(' A soma entre 1 a 10 é: {}'.format(somarInt()))
        elif (opcao == 9):
            print('\nEx9')
            print(' O resultado da soma dos números digitados é: {}'.format(somarNumero()))
            print(' O resultado da soma dos números digitados é: {}'.format(somarNumero()))
        elif (opcao == 10):
            print('\nExercicio10')
            print(exercicio10())
        elif (opcao == 11):
            print('\nEx11')
            print(exercicio11())
        elif (opcao == 12):
            print('\nEx12')
            print (exercicio12())
        elif (opcao == 13):
            print('\nEx13')
            exercicio13()
        elif (opcao == 14):
            print('\nEx14')
            print (exercicio14())
        elif (opcao == 15):
            print('\nEx15')
            print(miss())
        elif (opcao == 16):
            print ('\nEx16')
            print(eleicao())
        elif (opcao == 17):
            return
        elif (opcao == 18):
            return
        elif (opcao == 19):
            return
        elif (opcao == 20):
            return
        elif (opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
            return
        elif (opcao == 22):
            int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif (opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar'))
            apagarPosicao(posicao-1)

        else:
            print(' Opção escolhida não é válida, digite novamente! ')