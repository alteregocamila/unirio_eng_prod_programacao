#Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem,
# ao utilizar um automóvel que faz 12 Km/L. Para isso, ele gostaria que você o auxiliasse através
# de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas)
# e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida,
# calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

tempo = int(input('Digite um valor: '))
velocidade = int(input('Digite um valor: '))

#automóvel que faz 12 Km/L
carro = 12

distancia = tempo * velocidade
litros = distancia / carro

print('Foram gastos {:.3f} L de combustível.'.format(litros))