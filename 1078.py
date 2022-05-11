#Leia 1 valor inteiro N (2 < N < 1000).
# A seguir, mostre a tabuada de N:      1 x N = N      2 x N = 2N        ...       10 x N = 10N

n = int(input("Digite um número: "))
for i in range (1, 11):
    print('{} x {} = {}'.format(i, n, i * n))