#Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C.
# Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

A,B,C = input('Digite três valores: ').split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
tr = (A*C)/2
ci = (pi*(C**2))
tra = ((A+B)*C)/2
qua = B**2
re = A*B
print('TRIANGULO: {:.3f}'.format(tr))
print('CIRCULO: {:.3f}'.format(ci))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(re))
