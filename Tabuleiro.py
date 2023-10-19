import Exibicao

import random

# Função para criar o tabuleiro inicial
def gerar_tabuleiro():
    tabuleiro = [['\u2588' for _ in range(6)] for _ in range(6)]
    return tabuleiro

# Função para criar o tabuleiro de resultado
def gerar_tabuleiro_resultado():
    tabuleiro = [['\u2588' for _ in range(6)] for _ in range(6)]
    return tabuleiro

# Função para imprimir o tabuleiro
def mostrar_tabuleiro(tabuleiro):
    Exibicao.mostrarCaracteresUsados()
    print()
    print('---------------------')
    print()
    print('    1  2  3  4  5  6')

    c = ['A |','B |','C |','D |','E |','F |']
  
    for i in range(6):
        print(c[i] , end=' ')
        for j in range(6):
            print(tabuleiro[i][j], end='  ')
        print()
        print()
    print('---------------------')

# Função para posicionar os navios aleatoriamente no tabuleiro
def posicao_navios(tabuleiro):
    for _ in range(5):
        while True:
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            if tabuleiro[x][y] == '\u2588':
                tabuleiro[x][y] = 'N'
                break

# Função para posicionar os submarinos aleatoriamente no tabuleiro
def posicao_submarinos(tabuleiro):
    cont = 0
    while True:
        if cont == 3:
            break
        else:    
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if tabuleiro[x][y] == '\u2588' and tabuleiro[x + 1][y] == '\u2588' and posicoes_submarino(tabuleiro, x, y):
                tabuleiro[x][y] = 'S'
                tabuleiro[x + 1][y] = 'S' 
                cont += 1
    return  

# Função para verificar se é possível posicionar um submarino em uma posição
def posicoes_submarino(tabuleiro, x, y):
    if x < 5 and tabuleiro[x + 1][y] == '\u2588':
        return True
    elif x > 0 and tabuleiro[x - 1][y] == '\u2588':
        return True
    elif y < 5 and tabuleiro[x][y + 1] == '\u2588':
        return True
    elif y > 0 and tabuleiro[x][y - 1] == '\u2588':
        return True
    return False



