'''Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de
teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um
exercício com objetivo de testar raciocínio matemático simples.'''

n = int(input('Quantos dias você tem de vida: '))
a = int(n // 365)
m = int((n % 365) / 30)
d = int((n % 365) % 30)

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))