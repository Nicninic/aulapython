15.#Emumconcursodemiss,osjuradosprecisamdigitaronomedas16candidatasesuasrespectivasnotas(0a10).
#Crieumprogramaqueleiaestasinformaçõeseque,
#aofinaldoprograma,apresenteapenasonomeeanotadavencedora.


def validacaoNotas():
    nota = float(input('Informe uma nota: '))
    while ((nota < 0) or (nota > 10)):
        print ('Erro!!! Informe uma nota entre 0 e 10')
        nota = float(input('Informe uma nota: '))
    return nota

def miss():
    nomeVencedor = ''
    notaVencedora = 0
    for i in range(16):
        nome = input('Informe a {}ª nome   '.format(i))
        nota = validacaoNotas()

        if (nota > notaVencedora):
            notaVencedora = nota
            nomeVencedor = nome

    return 'Vencedora {} \nNota {}'.format(nomeVencedor, notaVencedora)





