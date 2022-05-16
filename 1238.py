#Implemente um programa denominado combinador, que recebe duas strings e deve combiná-las,
# alternando as letras de cada string, começando com a primeira letra da primeira string,
# seguido pela primeira letra da segunda string, em seguida pela segunda letra da primeira
# string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas
# ao fim da string resultante e retornada.
#A entrada contém vários casos de teste. A primeira linha contém um inteiro N que indica a quantidade
# de casos de teste que vem a seguir. Cada caso de teste é composto por uma linha que contém duas cadeias
# de caracteres, cada cadeia de caracteres contém entre 1 e 50 caracteres inclusive.

cnt = 0
n = int(input("Digite o número de testes: "))

while cnt < n:
    linha = input("Digite uma frase: ").split()
    p1 = linha[0]
    p2 = linha[1]
    final_palavra = ""
    cnt2 = 0

    while cnt2 < len(p1) and cnt2 < len(p2):
        final_palavra += p1[cnt2] + p2[cnt2]
        cnt2 += 1

    if cnt2 < len(p1):
        final_palavra += p1[cnt2:]

    if cnt2 < len(p2):
        final_palavra += p2[cnt2:]

    print(final_palavra)
    cnt += 1