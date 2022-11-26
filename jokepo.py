import random as ra
# CABEÇALHO DO JOGO
print('Bem vindo ao pedra,papel e tesoura.')
print('As regras são as seguintes:')
print('Você escolhe entre "Pedra" "Papel" ou "Tesoura" e eu também vou escolher um.')
print('O "Papel" ganha de "Pedra" e perde para a "Tesoura"')
print('A "Tesoura" ganha do "Papel" e perde para a "Pedra"')
print('E a "Pedra" ganha da "Tesoura" e perfe para o "Papel"')

jogadaspc = ['pedra', 'papel', 'tesoura']
escolhapc = ra.choice(jogadaspc)

# START DO JOGO
start = str(input('Preparado? Sim ou não? ')).lower().strip()

if start == 'sim':
    print('Certo, vamos lá!')
    print('Escolha uma das opções e quando estiver pronto, aperte "ENTER"')
    # ESCOLHA DE JOGADA DO USUARIO
    jogada_usuario = input('PEDRA \nPAPEL \nTESOURA\n').lower().strip()
    if jogada_usuario == 'pedra':
        if escolhapc == 'pedra':
            print('EMPATE')
        elif escolhapc == 'papel':
            print(f'Você perdeu! Eu joguei {escolhapc}')
        else:
            print(f'Você ganhou! Eu joguei {escolhapc}')
    elif jogada_usuario == 'papel':
        if escolhapc == 'pedra':
            print(f'Você ganhou! Eu joguei {escolhapc}')
        elif escolhapc == 'papel':
            print('EMPATE!')
        else:
            print(f'Você perdeu! Eu joguei {escolhapc}')
    elif jogada_usuario == 'tesoura':
        if escolhapc == 'tesoura':
            print('EMPATE!')
        elif escolhapc == 'pedra':
            print(f'Você perdeu! Eu joguei {escolhapc}')
        else:
            print(f'Você ganhou! Eu joguei {escolhapc}')
    else:
        print('Opção invalida, escolha uma das opções a cima')
else:
    print('Jogamos uma outra hora então!')
