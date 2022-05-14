#Este programa deve ler uma variável inteira X inúmeras vezes (deve parar quando o valor no arquivo de entrada
# for igual a zero). Para cada valor lido imprima a sequência de 1 até X, com um espaço entre cada número e seu
# sucessor.

x = 1
t = []

while x != 0:
    x = int(input("Digite um número: "))
    for i in range(1, x + 1):
        t.append(i)
        t[i-1] = str(t[i-1])
        i = i + i
    t = ' '.join(t)
    if x != 0:
        print(t)
        t = []