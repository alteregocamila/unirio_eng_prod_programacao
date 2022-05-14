#Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma
# dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))

if x > y:
    a = y
    b = x
if x <= y:
    a = x
    b = y

soma = 0

while a <= b:
    if a % 13 != 0:
        soma = soma + a
    a = a + 1
print("A soma dos números entre {} e {}  é {} e não é/são múltiplo/s de 13.".format(x, y, soma))