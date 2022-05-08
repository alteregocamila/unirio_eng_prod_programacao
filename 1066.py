#Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares,
# quantos valores digitados foram ímpares, quantos valores digitados foram positivos e
# quantos valores digitados foram negativos.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

pos = 0
neg = 0
par = 0
imp = 0

t = [a,b,c,d,e]

for n in t:
    if n > 0: pos = pos + 1
    if n < 0: neg += 1
    if n % 2 == 0: par = par + 1
    if n % 2 != 0: imp = imp + 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))