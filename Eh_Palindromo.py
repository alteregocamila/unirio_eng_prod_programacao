#Faça um código que leia do teclado um texto e verifique se é palíndromo.
# Caso não seja, transforme-o num palíndromo espelhando a primeira metade do seu conteúdo.

def eh_palindromo(texto):
    for i in range(0, len(texto)):
        if (texto[i] != texto[-i-1]):
            return False
    return True

def espelha_texto(texto):
    texto2 = texto[0:((len(texto) // 2)+(len(texto) % 2))]+texto[(len(texto) // 2)-1::-1]
    return texto2

texto = input('Digite uma frase: ')
texto = texto.strip().replace(' ', '').upper()

if eh_palindromo(texto):
    print('É palíndromo!')
else:
    print('Não é palíndromo!')
    print(espelha_texto(texto))