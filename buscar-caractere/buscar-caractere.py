while True:
    frase = input('Digite uma frase ou palavra: ').lower()
    buscar_caractere = input('Digite o caractere a ser procurado: ').lower()

    while len(buscar_caractere) > 1:
        print('Digite apenas um caractere')
        buscar_caractere = input('Digite o caractere a ser procurado: ').lower()

    if buscar_caractere in frase:
        print(f'\nCaractere "{buscar_caractere}" encontrado em "{frase}"')

    for i in range(len(frase)):
        if buscar_caractere == frase[i]:
            print(f'Na posição {i + 1}')  # A contagem dos caracteres da string não começa com 0 e sim com 1

    sair = input('\nDeseja sair? [s]im ou [n]ao: ')

    if sair == 's':
        break
    else:
        print()
