#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
# caso haja uma divisão por 0 ou raiz de numero negativo.

import math
a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = ((b ** 2) - (4 * a * c)) ** (1/2)

if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
