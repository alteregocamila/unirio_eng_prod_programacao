#Leia quatro valores inteiros A, B, C e D.
# A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
# DIFERENCA = (A * B - C * D).

A = int(input('Digite um valor: '))
B = int(input('Digite um valor: '))
C = int(input('Digite um valor: '))
D = int(input('Digite um valor: '))
dif = (A * B) - (C * D)
print('DIFERENCA = {}'.format(dif))