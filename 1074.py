#Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida.
# Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN),
# ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0),
# embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá
# imprimir apenas NULL.

n = int(input("Digite um número: "))

ns = []
for i in range(1, n + 1):
    x = int(input("Digite outro número: "))
    ns += [x]

for i in ns:
    atxt = []
    if i == 0:
        atxt += ['NULL']
    else:
        if i % 2 == 0:
            atxt += ['EVEN']
        if i % 2 != 0:
            atxt += ['ODD']
        if i > 0:
            atxt += ['POSITIVE']
        if i < 0:
            atxt.append('NEGATIVE')
    print(' '.join(atxt))