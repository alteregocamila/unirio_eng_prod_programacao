#Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
# Escreva para cada X e Y uma mensagem que indique se estes valores foram
# digitados em ordem crescente ou decrescente.

x = 100
y = 1000

while x != y:
    x, y = map(int, input('Digite um número: ').split())
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    else:
        print('Fim')
        break