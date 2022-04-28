#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica,
# e informe-o expresso no formato horas:minutos:segundos.

n = int(input('Digite a quantidade de segundos: '))

h = n // 60 ** 2
n = n - h * 60 ** 2
m = n // 60
n = n - m * 60
s = n

print('{}:{}:{}'.format(h,m,s))