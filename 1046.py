#Leia a hora inicial e a hora final de um jogo.
# A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro,
# tendo uma duração mínima de 1 hora e máxima de 24 horas.

a,b = input().split()

a = int(a)
b = int(b)

if (a < b):
    t = b - a
elif (a > b):
    t = (24 - a) + b
elif (a == b):
    t = 24
else:
    t = b - a

print('O JOGO DUROU {} HORA(S)'.format(t))
