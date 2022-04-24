#Faça um programa que leia o nome de um vendedor, o seu salário fixo
# e o total de vendas efetuadas por ele no mês (em dinheiro).
# Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber
# no final do mês, com duas casas decimais.

nome = str(input('Digite seu nome: '))
salario = float(input('Digite o seu salário: '))
vendas = float(input('Digite a quantidade de vendas: '))
comissao = (vendas*0.15)
sfinal = comissao+salario
print('TOTAL = R$ {:.2F}'.format(sfinal))