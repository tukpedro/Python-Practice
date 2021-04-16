import random

secret_words = [

    'crutch', 'abacate', 'estrume', 'candelabro', 'gaguejar', 'infinito', 'pantera', 'instinto', 'pelejar', 'rabanete'
    'lagosta', 'interruptor', 'maturidade', 'pescador', 'labirinto', 'eletrocardiograma', 'extinto', 'abobrinha'

]
secreto = secretos[random.randint(0, len(secretos)-1)]
digitado = []

while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Favor digitar apenas uma letra')
        continue

    digitado.append(letra)

    if letra in secreto:
        print('Opa! Existe essa letra na palavra! ;)\n')
    else:
        print('Não existe esta letra na palavra :(\n')
        digitado.pop()

    secreto_temp = ''

    for letra_secreta in secreto:
        if letra_secreta in digitado:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'GANHOU! Palavra secreta: {secreto}')
        sair = input('\nDeseja sair? [s]im ou [n]ao: ')

        if sair == 's':
            break
        else:
            print()
            secreto = secretos[random.randint(0, len(secretos)-1)]
            digitado = []
    else:
        print(secreto_temp)
