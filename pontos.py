import limpar

def gravar(nome, ranking, pontos):
    # Abre o arquivo no modo de escrita (modo 'w') ou cria um novo se não existir
    with open(pontos, 'a') as file:
        # Escreve o nome e o placar no arquivo, separados por um espaço e seguidos de uma quebra de linha
        file.write(f'{nome} {ranking}\n')

def ler(pontos):
    try:
        # Abre o arquivo no modo de leitura ('r')
        file = open(pontos)
        lista = file.readlines()
        file.close()

        posicao = []  # Lista para armazenar as posições dos jogadores

        print()
        print('========= Melhores Colocados ========= ')
        print('     Nome                  # Jogadas')

        # Percorre cada linha do arquivo e extrai o nome e o placar separados por espaço
        for line in lista:
            valores = line.split()
            if len(valores) >= 2:
                nome, p = valores
                posicao.append(p + '-' + nome)  # Adiciona a posição na lista no formato "placar + nome"

        posicao.sort()  # Ordena a lista de posições em ordem crescente

        for i in range(len(posicao)):
            pt = posicao[i]
            p1 = pt[0:2]  # Extrai o placar
            p2 = pt[3:]  # Extrai o nome

            # Imprime a posição, o nome e o placar formatados
            print(f'{i+1:2} - {p2:25}   {p1:2}')
            print()

        input('Tecle Algo para continuar!')
        limpar.clear()

    except FileNotFoundError:
        print(f"O arquivo '{pontos}' não foi encontrado.")
        input('Tecle Algo para continuar!')
        limpar.clear()