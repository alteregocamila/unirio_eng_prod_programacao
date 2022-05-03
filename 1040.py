#Calculadora de aprovação em disciplina.

p1 = input("Digite as suas quatro notas: ").split()

n1 = float(p1[0])
n2 = float(p1[1])
n3 = float(p1[2])
n4 = float(p1[3])

media1 = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print('Media: {:.1f}'.format(media1))

if (media1 >= 7.0):
    print('Aluno aprovado.')
elif (media1 < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: {:.1f}'.format(n5))
    media2 = (media1 + n5) / 2
    if (media2 >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media2))