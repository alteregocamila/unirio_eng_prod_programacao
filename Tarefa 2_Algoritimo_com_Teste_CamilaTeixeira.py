'''Dado um número inteiro de 3 algarismos, construir outro número de 4 algarismos de acordo com a seguinte
regra:

os três primeiros algarismos, contados da esquerda para a direita, são iguais aos do número dado

o quarto algarismo é um dígito de controle calculado da seguinte forma:

primeiro algarismo + (segundo algarismo x 3) + (terceiro algarismo x 5).

O dígito de controle é igual ao resto da divisão dessa soma por 7.'''

num = int(input('Digite um número inteiro com 3 algarismos: '))

if num < 99:
    print('O número informado não tem 3 algarismos!')
else:
    u = int(num % 10)
    print(u)
    d = int(((num % 100) - u) / 10)
    print(d)
    c = int(num/100)
    print(c)
    n = int((c + (d * 3) + (u * 5)) % 7)
    resultado = int((c * 1000) + (d * 100) + (u * 10) + n)

    print('O novo número é {}.'.format(resultado))


