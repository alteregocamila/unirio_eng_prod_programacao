#Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

x = int(input())
y = int(input())

if x <= y:
    ini = x
    fin = y
else:
    ini = y
    fin = x

soma = 0
ini += 1
while ini < fin:
    if ini % 2 != 0:
        soma += ini
    ini += 1
print(soma)