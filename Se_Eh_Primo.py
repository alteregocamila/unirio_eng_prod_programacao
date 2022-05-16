#Faça um código que leia do teclado um número e verifique se é primo. Caso não seja,
# informe todos os seus divisores primos.

num = int(input('Digite um número: '))
divisores = 0
divisores = []
i = 1
while i <= num:
    if num % i == 0:
        divisores.append(i)
    i += 1

'''if len(divisores) == 2:
    print('{} é primo! Divisores {}'.format(num, ', '.join(map(str, divisores))))
else:
    print('{} não é primo!'.format(num))'''

if len(divisores) != 2:
    print('{} não é primo! Divisores {}'.format(num, ', '.join(map(str, divisores))))
else:
    print('{} é primo!'.format(num))


