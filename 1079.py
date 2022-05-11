#Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir.
# Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal.
# Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o
# primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    x = input("Digite três números com espaços entre eles: ").split()
    a,b,c = x
    a = float(a)
    b = float(b)
    c = float(c)
    media1 = ((a * 2) + (b * 3) + (c * 5)) / 10
    print('{:.1f}'.format(media1))

