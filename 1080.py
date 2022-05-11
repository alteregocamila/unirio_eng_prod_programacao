#Leia 5 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
n = int(input("Digite um número: "))
x = 0

for i in range (1,5):
    a = int(input("Digite outro número: "))
    if a > x:
        maior = a
        posicao = i + 1
        x = a
print("O maior valor é {}.".format(maior))
print("Sua posição é {}.".format(posicao))