#Não há nenhuma entrada neste problema. Imprima a sequencia conforme exemplo abaixo.
# I=1 J=7 ... I=? J=0
i = 1
j = 7

while i <= 9:
    for c in range(1,4):
        print('I={} J={}'.format(i, j))
        j = j - 1
    i = i + 2
    j = j + 5