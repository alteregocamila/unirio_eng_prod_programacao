#Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos,
# pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em
# benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.
# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida,
# calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda.

s = float(input("Informe o seu salário: "))

if (s <= 2000.00):
    print('Isento')
else:
    if (s <= 3000.00):
        x = (s - 2000.00) * 0.08
    elif (s <= 4500.00):
        x = (1000.00 * 0.08) + (s - 3000.00) * 0.18
    else:
        x = 1000.0 * 0.08 + 1500.0 * 0.18 + (s - 4500.0) * 0.28
    print('Você deve pagar R$ {:.2f} de Imposto de Renda.'.format(x))
