import Tabuleiro
import limpar
import pontos

# Função principal do jogo
def jogo_batalha_naval():

    tabuleiro = Tabuleiro.gerar_tabuleiro()
    resultado = Tabuleiro.gerar_tabuleiro_resultado()
    Tabuleiro.posicao_navios(tabuleiro)
    Tabuleiro.posicao_submarinos(tabuleiro)
    
    tentativas = 0
    acertos = 0
    chutes = []
    
    print("Bem-vindo ao Jogo de Batalha Naval!")
    navios = 0
    submarinos = 0
    a = 0

    while True:

        # Chama a função "sair()" para limpar a tela antes de mostrar o tabuleiro    
        limpar.clear()

        ch = len(chutes)

        Tabuleiro.mostrar_tabuleiro(tabuleiro) # Imprime o tabuleiro do jogo

        Tabuleiro.mostrar_tabuleiro(resultado) # Imprime o tabuleiro de resultado

        print()
        print('Jogadas até agora: {}'. format(ch))
        print("Afundados até agora = Navios {} de 5 | Submarinos {} de 3 ".format(navios, submarinos))
        print('tecle -1 para desistir')
        print()
        palpite = input("Digite a posição de ataque (exemplo: B2): ").upper()
        
        print('----------------')
        print()

        # Chama a função "sair()" para limpar a tela antes de encerrar o jogo
        if palpite == '-1':
            limpar.clear()
            break

        
        if len(palpite) != 2 or palpite[0] not in 'ABCDEF' or palpite[1] not in '123456':
            print("===> Por favor, insira um palpite válido.")
            input()  
            continue
          
        elif palpite in chutes:
            print("===> Palpite repetido! Outro por favor!")
            input()  
            continue

        y = int(palpite[1]) - 1
        x = ord(palpite[0]) - ord('A')
        
        chutes.append(palpite)
        ch = len(chutes)

        # Atualiza o tabuleiro de resultado com um traço para indicar um chute na água
        if tabuleiro[x][y] == '\u2588':
            resultado[x][y] = '_'
            tentativas += 1
            a = 1
        
        elif tabuleiro[x][y] == 'N':
            
            resultado[x][y] = 'X'   # Atualiza o tabuleiro de resultado com um 'X' para indicar um acerto em um navio   
            tentativas += 1
            acertos += 1
            navios +=1
            a= 2
        
        elif tabuleiro[x][y] == 'S':
            
                if x == 5:
                    
                    if resultado[x-1][y] == '\u2316':
                        
                        resultado[x][y]   = 'X' # Atualiza o tabuleiro de resultado com um 'X' para indicar um acerto em um submarino
                        resultado[x-1][y] = 'X'
                        submarinos += 1
                        acertos +=1
                        tentativas +=1
                        a = 3
                        
                    else:
                        resultado[x][y] = '\u2316'  # Atualiza o tabuleiro de resultado com um símbolo para indicar um acerto em um submarino
                        tentativas += 1
                        acertos += 1
                        a = 4
                    
                elif resultado[x-1][y] == '\u2316':
                        
                        resultado[x][y]   = 'X'
                        resultado[x-1][y] = 'X'
                        submarinos += 1
                        acertos +=1
                        tentativas +=1
                        a = 3

                elif resultado[x+1][y] == '\u2316':
                        resultado[x][y]   = 'X'
                        resultado[x+1][y] = 'X'
                        submarinos += 1
                        acertos +=1
                        tentativas +=1
                        a = 3

                else:
                        resultado[x][y] = '\u2316'
                        tentativas += 1
                        acertos += 1
                        a = 4
           
        if a == 0:
            pass
        elif a ==1:
            print("===> Água! Tente novamente. {} Jogadas!".format(ch) )     
        elif a == 2:
            print("===> Afundou um navio! {} Jogadas!".format(ch))  
        elif a == 3:              
            print("===> Afundou um submarino! {} Jogadas!".format(ch))
        elif a == 4:
            print("===> Acertou parte de um submarino! {} Jogadas!".format(ch))

        input()  # Aguarda a entrada do usuário para continuar a execução

        # Verifica se o número de navios é igual a 5 e o número de submarinos é igual a 3. Se for verdadeiro, mostra o tabuleiro,     
        # imprime uma mensagem de parabéns com o número de jogadas (ch),
        if navios ==5 and submarinos ==3:
            ch = len(chutes)
            Tabuleiro.mostrar_tabuleiro(tabuleiro)
            print("Parabéns! Você afundou todos os navios e submarinos, com {} Jogadas! ".format(ch))

            # solicita ao jogador que digite seu primeiro nome, grava o recorde no arquivo 'ranking.txt', lê o arquivo 'ranking.txt',                  limpa a tela e encerra o loop com o comando break. Caso contrário, não faz nada.
            nome = input('Vamos Gravar seu Recorde, digite seu primeiro Nome: ')

            pontos.gravar(nome, tentativas, 'ranking.txt')

            pontos.ler('ranking.txt')
          
            limpar.clear()
          
            break
        else:
             pass
