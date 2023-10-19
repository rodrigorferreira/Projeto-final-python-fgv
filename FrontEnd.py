import Persistencia
import limpar
import pontos

def menu():
  while True:
    # Exibe as opções disponíveis para o usuário
    print("1- Jogar")
    print("2- Ver Melhores Pontuações")
    print("3- Sair")
    print("------------------------")

    # Solicita ao usuário que escolha uma opção digitando um número
    opcao = int(input("Escolha uma opção: "))

    # Verifica a opção escolhida pelo usuário
    if opcao == 1:
        Persistencia.jogo_batalha_naval()
    elif opcao == 2:
        # Chama a função ler('ranking.txt')]
        pontos.ler('ranking.txt')
    else:
        # Chama a função sair()
        limpar.clear()
        print("Volte logo!")
        # Encerra o loop while True, finalizando a execução da função menu
        break