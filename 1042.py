#Leia 3 valores inteiros e ordene-os em ordem crescente.
# No final, mostre os valores em ordem crescente, uma linha em branco e em seguida,
# os valores na sequência como foram lidos.

L1 = input().split()
x = int(L1[0])
y = int(L1[1])
z = int(L1[2])

A = x
B = y
C = z

if z < y:
    aux = z
    z = y
    y = aux
if y < x:
    aux = y
    y = x
    x = aux
if z < y:
    aux = z
    z = y
    y = aux
print(x)
print(y)
print(z)
print( )
print(A)
print(B)
print(C)

