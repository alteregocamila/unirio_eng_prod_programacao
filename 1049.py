#Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo,
# da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três
# palavras fornecidas.

a = input("Digite uma das seguintes palavras (vertebrado, invertebrado):  ")
b = input("Digite uma das seguintes palavras (ave, mamífero, inseto, anelídeo):  ")
c = input("Digite uma das seguintes palavras (carnívoro, hematófago):  ")

if (a == 'vertebrado'):
    if (b == 'ave'):
        if (c == 'carnívoro'):
            x = 'aguia'
        else:
            x = 'pomba'
    else:
        if (b == 'mamífero'):
            if (c == 'carnívoro'):
                x = 'homem'
            else:
                x = 'vaca'
elif (a == 'invertebrado'):
    if (b == 'inseto'):
        if (c == 'hematófago'):
            x = 'pulga'
        else:
            x = 'lagarta'
    else:
        if (b == 'anelídeo'):
            if (c == 'hematófago'):
                x = 'sanguessuga'
            else:
                x = 'minhoca'
print(x)