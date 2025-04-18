import numpy as np
from random import randint, choice
from time import sleep

def jogada_maquina(): # jogada da máquina
    escolha_maquina = randint(resto[0],resto[-1])-1
    while escolha_maquina in jogadas:
        escolha_maquina = randint(resto[0],resto[-1])-1
    
    print(f'Escolha da máquina: posição {escolha_maquina+1}')
    sleep(1)
    print()
    if escolha_maquina not in jogadas:
        jogadas.append(escolha_maquina)
        resto.remove(escolha_maquina+1)
    for i in range(0, 1):
        if escolha_maquina <= 2: 
            c = escolha_maquina
            cont = 0
        elif escolha_maquina <= 5:
            c = escolha_maquina-3
            cont = 1
        else:
            c = escolha_maquina-6
            cont = 2
        array[cont][c] = 'X'
    
def jogada_jogador(): # jogada do jogador
    print()
    escolha_jogador = int(input(f'Escolha uma posição {resto}: '))-1
    while escolha_jogador in jogadas or escolha_jogador > 9 or escolha_jogador < 0:
        print('Escolha uma posição válida!')
        escolha_jogador = int(input(f'Escolha uma posição {resto}: '))-1

    if escolha_jogador not in jogadas:
        jogadas.append(escolha_jogador)
        resto.remove(escolha_jogador+1)

    print(f'Escolha jogador: posição {escolha_jogador+1}')
    sleep(1)
    for y in range(0,1):
        if escolha_jogador <= 2: 
            c = escolha_jogador
            cont = 0
        elif escolha_jogador <= 5:
            c = escolha_jogador-3
            cont = 1
        else:
            c = escolha_jogador-6
            cont = 2
        array[cont][c] = 'O'

def verificar_horizontal(array, nome, simbolo): # verificação apenas na horizontal
    simb = simbolo
    cont = 0
    while True:
        contagem = 0
        for i in range(0, 3):
            if array[cont][i] != simb:
                continue
            else:
                contagem += 1
        if contagem == 3:
            return True
        if cont == 2:
            break
        cont += 1
    
def verificar_diagonal(array, nome, simbolo): # verificação apenas na diagonal
    simb = simbolo
    cont = 0 
    while True:
        contagem = 0
        for i in range(0, 3): # superior esquerdo para o inferior direito
            if array[cont][i] != simb:
                break
            else:
                cont += 1
                contagem += 1
        if contagem == 3:
            return True
        break

    cont = 2
    while True:
        contagem = 0
        for i in range(0, 3): # inferior esquerdo para o superior direito
            if array[cont][i] != simb:
                break
            else:
                cont -= 1
                contagem += 1
        if contagem == 3:
            return True
        break

def verificar_vertical(array, nome, simbolo): # verificção apenas na vertical
    simb = simbolo
    geral = 0
    while True:
        conti = 0
        contagem = 0

        for i in range(0, 3): 
            if array[conti][geral] != simb:
                break
            else:
                conti += 1
                contagem += 1
        if contagem == 3:
            return True
        
        if geral == 2:
            break
        geral += 1

array = np.zeros((3, 3)).astype(int)
array = array.astype(str)

jogadas = []
resto = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fim = 1
jogadores = ['Maquina', 'Jogador']
comecar = choice(jogadores)
print(f'{comecar} irá começar!')
print()

while True:
    print(f'{array}\n')

    comecar = comecar
    if comecar == 'Maquina':
        jogada_maquina()
    if comecar == 'Jogador':
        jogada_jogador()

    if comecar == 'Maquina':
        c = 'X'
    else:
        c = 'O'
    print()
    verificacao = verificar_horizontal(array, comecar, c)
    if verificacao == True:
        print(f'{comecar} ganhou!')
        break
    verificacao = verificar_diagonal(array, comecar, c)
    if verificacao == True:
        print(f'{comecar} ganhou!')
        break
    verificacao = verificar_vertical(array, comecar, c)
    if verificacao == True:
        print(f'{comecar} ganhou!')
        break
        
    if comecar == 'Maquina':
        comecar = 'Jogador'
    else:
        comecar = 'Maquina'
    
    if fim == 9:
        print('Empate!')
        break
    fim += 1

print(array)
