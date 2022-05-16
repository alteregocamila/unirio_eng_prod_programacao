#A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste,
# seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor
# que João quer montar com os leds.

n = int(input("Digite um número de testes: "))

for i in range(1, n + 1):
    led = 0
    x = input("Digite o número de leds: ")
    for j in range (0, len(x)):
        if x[j] == '1':
            led = led + 2
        if x[j] == '2':
            led = led + 5
        if x[j] == '3':
            led = led + 5
        if x[j] == '4':
            led = led + 4
        if x[j] == '5':
            led = led + 5
        if x[j] == '6':
            led = led + 6
        if x[j] == '7':
            led = led + 3
        if x[j] == '8':
            led = led + 7
        if x[j] == '9':
            led = led + 6
        if x[j] == '0':
            led = led + 6
    print('{} leds'.format(led))

