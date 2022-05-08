#Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo,
# mostrando essas informações.

n = int(input())
dentro = 0
fora = 0
for i in range (1, n + 1):
    x = int(input())
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print('{} in'.format(dentro))
print('{} out'.format(fora))
