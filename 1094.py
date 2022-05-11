#A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir.
# Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas
# e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

t = int(input("Digite um número: "))
c = 0
r = 0
s = 0

for i in range(1, t + 1):
    x = (input("Digite outro número e a letra correspondente ao tipo de cobaia: ")).split()
    a, b = x
    if b == 'C':
        c = c + int(a)
    if b == 'R':
        r = r + int(a)
    if b == 'S':
        s = s + int(a)

soma = c + r + s

pc = (c/soma)*100
pr = (r/soma)*100
ps = (s/soma)*100

print('Total: {} cobaias'.format(soma))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))

