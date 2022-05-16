#Seu amigo precisa aumentar o número de variações de sua senha, e pediu sua ajuda.
# Dada a senha que ele escolheu, diga o número de diferentes variações que é possível montar.
# A primeira linha contém um inteiro T, indicando o número de casos de teste a seguir. Cada caso
# de teste contém uma sequência de caracteres S, indicando a senha de seu amigo. Para cada senha,
# haverá no mínimo 1 e no máximo 16 caracteres, os quais podem ser uma das 26 letras do alfabeto,
# minúsculas ou maiúsculas.

n = int(input("Digite o número testes: "))
l = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 's', 'S']

while n > 0:
    n -= 1
    c = input("Informe sua senha com no máximo 16 letras: ")
    var = 1
    for i in range(len(c)):
        if c[i] in l:
            var *= 3
        else:
            var *= 2

    print(var)