#Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

a,b,c = input('Digite três valores: ').split()
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a + b + abs(a-b))/2
maiorABC = (maiorAB + c + abs(maiorAB-c))/2

print('{:.0f} eh o maior'.format(maiorABC))