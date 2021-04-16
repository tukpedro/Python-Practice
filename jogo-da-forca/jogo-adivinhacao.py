import random

palavras_secretas = [

    'perfume', 'abacate', 'estrume', 'candelabro', 'gaguejar', 'infinito', 'pantera', 'instinto', 'pelejar', 'rabanete'
    'lagosta', 'interruptor', 'maturidade', 'pescador', 'labirinto', 'eletrocardiograma', 'extinto', 'abobrinha'

]
palavra_selecionada = palavras_secretas[random.randint(0, len(palavras_secretas)-1)]
digitado = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Favor digitar apenas uma letra')
        continue

    digitado.append(letra)

    if letra in palavra_selecionada:
        print('Opa! Existe essa letra na palavra! ;)\n')
    else:
        print('Não existe esta letra na palavra :(\n')
        digitado.pop()

    secreto_temp = ''

    for letra_secreta in palavra_selecionada:
        if letra_secreta in digitado:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == palavra_selecionada:
        print(f'GANHOU! Palavra secreta: {palavra_selecionada}')
        sair = input('\nDeseja sair? [s]im ou [n]ao: ')

        if sair == 's':
            break
        else:
            print()
            palavra_selecionada = palavras_secretas[random.randint(0, len(palavras_secretas)-1)]
            digitado = []
    else:
        print(secreto_temp)
