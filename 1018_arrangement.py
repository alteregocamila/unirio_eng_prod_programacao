#Leia um valor inteiro. A seguir, calcule o menor número de nota possíveis (cédulas) no qual o valor pode ser
# decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação
# de notas necessárias.

n = int(input('Digite um valor até 1000000: '))
if n < 0 or n > 1000000:
    print("erro")
else:
    print(n)

n1 = n // 100
print("{} nota(s) de R$ 100,00".format(n1))

n = n % 100
n2 = n // 50
print("{} nota(s) de R$ 50,00".format(n2))

n = n % 50
n3 = n // 20
print("{} nota(s) de R$ 20,00".format(n3))

n = n % 20
n4 = n // 10
print("{} nota(s) de R$ 10,00".format(n4))

n = n % 10
n5 = n // 5
print("{} nota(s) de R$ 5,00".format(n5))

n = n % 5
n6 = n // 2
print("{} nota(s) de R$ 2,00".format(n6))

n = n % 2
n7 = n // 1
print("{} nota(s) de R$ 1,00".format(n7))

