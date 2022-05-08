#Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X,
# um valor por linha, inclusive o X, se for o caso.

x = int(input())
y = 1

while y <= x:
    if y % 2 != 0:
        print(y)
    y = y + 1