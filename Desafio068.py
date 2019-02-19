from random import randint
#pc = randint(0,100) #pc escolhe um valor
player = 0 #player
par = 2
cont = 0
while True:
    pc = randint(0,100)
    player = str(input('você quer par ou ímpar?')).upper().strip()[0]
    if player in 'Pp':
        player = int(input('Você escolheu par, digite seu valor:'))
        if (pc + player) % 2 == 0:
            print(f'A soma dos valores foi {pc + player}')
            print('Você venceu, tente novamente.')
            cont += 1
        else:
            print('Você perdeu')
            break
    if player in 'IiÍí':
        player = int(input('Você escolheu ímpar, digite seu valor:'))
        if (pc + player) % 2 != 0:
            print(f'A soma dos valores foi {pc+player}')
            print('Você venceu, tente novamente.')
            cont += 1
        else:
            print('Você perdeu')
            break
print(f'Você teve {cont} vitórias consecutivas.')