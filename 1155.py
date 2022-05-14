#Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:S = 1 + 1/2 + 1/3 + … + 1/100

s = 0
for i in range (1, 101):
    s = float (s + float(1)/ float(i))
print('{:.2f}'.format(s))