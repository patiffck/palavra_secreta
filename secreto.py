import os

palavra_secreta = 'violao'
letra_acertadas = ''
numeros_tentativas = 0


while True:
    
    letra_digitada = input('Digite apenas uma letra: ')
    numeros_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('VOCÊ GANHOU! ! PARABÉNS! ')
        print('A palvra era', palavra_secreta)
        print('Tentativas', numeros_tentativas)
        letra_acertadas = ''
        numeros_tentativas = 0