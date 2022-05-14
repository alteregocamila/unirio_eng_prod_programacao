#Escreva um programa que repita a leitura de uma senha até que ela seja válida.
# Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Inválida".
# Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido"
# e o algoritmo encerrado. Considere que a senha correta é o valor 2002.
senha = 1
while senha != 2002:
    senha = int(input("Infome a senha: "))
    if senha != 2002:
        print('Senha inválida')
    else:
        print('Acesso Permitido')
        break