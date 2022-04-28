#Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano,
# p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula,
# segundo a fórmula: Distancia = raiz quadrada de X2 - X1 elevado ao quadrado + y2 - y1 elevado ao quadrado

import math

p1 = input('Digite um valor: ').split()
x1 = float(p1[0])
y1 = float(p1[1])
p2 = input('Digite um valor: ').split()
x2 = float(p2[0])
y2 = float(p2[1])

x = (x2-x1)*(x2-x1)
y = (y2-y1)*(y2-y1)
dist = math.sqrt(x+y)

print("%.4f" % dist)