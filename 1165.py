#A entrada contém vários casos de teste.
# A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 5), indicando o número de casos de teste da entrada.
# Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

n = int(input("Digite um número inteiro entre 1 e 5: "))
if 1 <= n <= 5:
    for i in range(1, n + 1):
        x = int(input("Digite um número inteiro: "))
        count = 1
        qtddiv = 0
        while count <= x:
            if x % count == 0:
                qtddiv += 1
            count += 1
        if qtddiv == 2:
            print('{} eh primo'.format(x))
        else:
            print('{} nao eh primo'.format(x))

