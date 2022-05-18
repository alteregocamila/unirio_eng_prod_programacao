# Camila Teixeira
# Lista de função - exercício 4 - letra b
# Função
def ehfib(f):
    t1 = 0
    t2 = 1
    if (f == t1 or f == t2):
        return True
    else:
        t = t1 + t2
        while (t < f):
            t1 = t2
            t2 = t
            t = t1 + t2
        if (t == f):
            return True
        else:
            return False

# programa
n = int(input("Digite um número: "))
resultado = ehfib(n)
print(resultado)