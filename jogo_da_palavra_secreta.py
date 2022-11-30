palavra_secreta = 'guarana'
letras_digitadas = ''
vidas = 3

while True:
    letra_user = input('Digite uma letra: ')
    

    if len(letra_user) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_user in letras_digitadas:
        print('\n\nEssa letra já foi digitada.\n\n')
        continue
    if letra_user in palavra_secreta:
        print('\n\nAcertou a letra!')
        
    else:
        vidas -= 1
        if vidas == 0:
            print('\n\nVocê perdeu todas as vidas! :(')
            print(f'A palavra era {palavra_secreta}.')
            print('Fim de jogo!\n\n')
            break
        else:
            print('\n\nEssa letra não está na palavra secreta! :(')
            print(f'Você tem ainda tem {vidas} vidas.')

    letras_digitadas += letra_user
    palavra_secreta_user = ''
    for letra in palavra_secreta:
        if letra in letras_digitadas:
            palavra_secreta_user += letra
        else:
            palavra_secreta_user += '*'
    print(f'Palavra: {palavra_secreta_user}\n\n')

    
    
    if palavra_secreta_user == palavra_secreta:
        print('\n\nVocê acertou a palavra secreta!! :)')
        print(f'A palavra era {palavra_secreta}!!\n\n')
        break