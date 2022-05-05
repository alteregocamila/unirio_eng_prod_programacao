#A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o
# índice reajustado, em percentual.

s = float(input("Digite o seu salário: "))

a1 = s + ((s * 15) / 100)
a2 = s + ((s * 12) / 100)
a3 = s + ((s * 10) / 100)
a4 = s + ((s * 7) / 100)
a5 = s + ((s * 4) / 100)

if (s <= 400):
    ns = a1
elif (s >= 400.01) and (s <= 800.00):
    ns = a2
elif (s >= 800.01) and (s <= 1200.00):
    ns = a3
elif (s >= 1200.01) and (s <= 2000.00):
    ns = a4
else:
    ns = a5
print('Novo salario: {:.2f}'.format(ns))

if (s <= 400):
    r = ((s * 15)/100)
elif (s >= 400.01) and (s <= 800.00):
    r = ((s * 12)/100)
elif (s >= 800.01) and (s <= 1200.00):
    r = ((s * 10)/100)
elif (s >= 1200.01) and (s <= 2000.00):
    r = ((s * 7)/100)
else:
    r = ((s * 4) / 100)
print('Reajuste ganho: {:.2f}'.format(r))

if (s <= 400):
    p = 15
elif (s >= 400.01) and (s <= 800.00):
    p = 12
elif (s >= 800.01) and (s <= 1200.00):
    p = 10
elif (s >= 1200.01) and (s <= 2000.00):
    p = 7
else:
    p = 4
print('Em percentual: {} %'.format(p))