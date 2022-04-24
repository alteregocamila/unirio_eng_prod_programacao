#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas,
# o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número
# e o salário do funcionário, com duas casas decimais.

a = int(input('Digite sua matrícula: '))
b = int(input('Digite suas horas trabalhadas: '))
c = float(input('Digite o valor da sua hora trabalhada: '))
salario = b*c
print('NUMBER = {}'.format(a))
print('SALARY = U$ {:.2f}'.format(salario))