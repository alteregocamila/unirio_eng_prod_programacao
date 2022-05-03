'''Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos
seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor
não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo '(' representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000'''

a = float(input("Digite um número: "))

if (a < 0) or (a > 100):
    print('Fora do intervalo')
elif (a >= 0) and (a <= 25):
    print('Intervalo [0,25]')
elif (a > 25) and (a <= 50):
    print('Intervalo (25,50]')
elif (a > 50) and (a <= 75):
    print('Intervalo (50,75]')
else:
    print('Intervalo (75,100]')