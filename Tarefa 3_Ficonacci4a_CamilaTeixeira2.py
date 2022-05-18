# Camila Teixeira
# Lista de função - exercício 4 - letra a

#função
def fibonacci(n):
    u = 1
    p = 0

    if (n == 1) or (n == 2):
        print('1')
    else:
        count = 3
        while count <= n:
            termo = u + p
            p = u
            u = termo
            count += 1
        print(termo)

#Principal
n = int(input("Digite um número: "))
m = fibonacci(n)
if m == True:
    print(m)
