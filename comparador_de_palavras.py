#Faça um código que leia do teclado um texto em português e a sua tradução em outra língua.
# Compare o número de ocorrências de cada palavra em ambos os textos e as imprima em ordem
# decrescente de frequência.

import string
def count_palavra(texto):
    palavras = texto.split(' ')
    count = {}
    for palavra in palavras:
        if palavra in count:
           count[palavra] += 1
        else:
           count[palavra] = 1
    return count

def pp_sorted(dic):
    for i in sorted(dic, key=dic.get, reverse=True):
        print(i, dic[i])

texto_pt = str(input('Digite um texto em português: '))
texto_en = str(input('Digite um texto em inglês: '))

a = string.punctuation
for palavra in a:
    texto_pt = texto_pt.replace(palavra, "")

b = string.punctuation
for palavra in b:
    texto_en = texto_en.replace(palavra, "")

a = count_palavra(texto_pt)
b = count_palavra(texto_en)

print('===================')
print('Pt:')
pp_sorted(a)

print('===================')
print('En:')
pp_sorted(b)