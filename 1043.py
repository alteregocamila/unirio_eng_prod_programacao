'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo,
calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X'''


a,b,c = input("Digite três números: ").split()

a = float(a)
b = float(b)
c = float(c)

p = a+b+c
h = ((a + b) * c)/2

if a < b + c and b < a + c and c < a + b:
    print('Estes números formam um triângulo cujo o Perímetro é {:.1f}'.format(p))
else:
    print('Estes números formam um trapézio cujo a Área é {:.1f}'.format(h))