def Matriz(tamanho,vazio): #Construção do Tabuleiro segundo o valor informado pelos os jogadores.
    matriz = []
    colunas = []
    lista = []
    for i in range(tamanho):
        matriz.append([])
        colunas.append(i)

    for i in range(len(matriz)):
       for j in range(len(matriz)):
           matriz[i].append(vazio)
    lista.append(matriz)
    lista.append(colunas)
    return lista

def Jogada(tabuleiro,coluna,jogador,tam,vazio): #Faz a alteração de nenhum elemento para o elemento do jogador.
    linha_compara = 1
    linha_posicao = -1
    while linha_compara < tam:
        for i in range(tam):
            if tabuleiro[linha_posicao][coluna] == vazio:
                tabuleiro[linha_posicao][coluna] = jogador
                return tabuleiro
            else:
                linha_compara += 1
                linha_posicao -= 1
    return tabuleiro

def Linha_usada(tabuleiro,coluna,tam): #Função para obter a linha usada na jogada.
    linha_usada = tam
    linha_compara = 1
    linha_posicao = -1
    while linha_compara < tam:
        for i in range(tam):
            if tabuleiro[linha_posicao][coluna] == vazio: #Onde for encontrado o primeiro espaço vazio, obterá a linha.
                return linha_usada
            else:
                linha_compara += 1
                linha_posicao -= 1
                linha_usada -= 1
    return linha_usada

def Coluna_cheia(coluna,vazio):
    if tabuleiro[0][coluna] == vazio:
        return False #Se o primeiro elemento da coluna não for vazio, indica que a coluna está cheia
    else:
        return True #Se ainda houver espaço na coluna.

def Linha(tabuleiro,tam,jogador,pecas_acaba):
    linha = 0
    for i in range(tam): #Conta se tem a quantidade que o jogador definiu de 'O' ou 'X' seguidos na linha.
        for j in range(tam):
            if tabuleiro[i][j] == jogador:
                linha += 1
                if linha == pecas_acaba: #Se tiver os a quantidade que o jogador definiu, já retorna o valor pois o jogador venceu.
                    return pecas_acaba
            else: #Se o caractere não for igual ao anterior, zera a sequência.
                linha = 0
    return linha

def Coluna(tabuleiro,tam,jogador,pecas_acaba):
    coluna = 0
    for i in range(tam): #Conta se  tem a quantidade que o jogador definiu de 4 'O' ou 'X' seguidos na coluna.
        for j in range(tam):
            if tabuleiro[j][i] == jogador:
                coluna += 1
                if coluna == pecas_acaba: #Se tiver os a quantidade que o jogador definiu, já retorna o valor pois o jogador venceu.
                    return pecas_acaba
            else: #Se o caractere não for igual ao anterior, zera a sequência.
                coluna = 0
    return coluna

def Emapte(tabuleiro,vazio): #Verifica se ainda existe jogadas.
    cont = 0
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro)):
            if tabuleiro[i][j] == vazio:
                cont += 1
    return cont

def Diagonais_Subindo_Principal(tabuleiro,jogador,linha,coluna,pecas_acaba): #Nesta função ela recebe a posiçao que o jogador pois sua peça e verifia as diagonais.
    diagonal = 1 #Começa com um pois vamos verificar apartir do movimento do jogador.
    nova_linha = linha
    nova_coluna = coluna
    for i in range(pecas_acaba-1): #Como já temos uma peça, iremos verificar as outras três posições para ver se tem o elemento do jogador.
        nova_linha -= 1
        nova_coluna -= 1
        if nova_linha < 0 or nova_coluna < 0: #Essa condição é para não ultrapassar o tamanho do tabuleiro, o que iria ocasionar 'List index out of the range'.
            return diagonal
        else:
            if tabuleiro[nova_linha][nova_coluna] == jogador: #Verifica se os caracteres nas diagonais são iguais a 'O' ou 'X'.
                diagonal += 1
            else: #Se o caractere não for igual ao anterior, a sequência fica com 1 novamente.
                diagonal = 1
    return diagonal
def Diagonais_Descendo_Principal(tabuleiro,jogador,linha,coluna,pecas_acaba): #Nesta função ela recebe a posiçao que o jogador pois sua peça e verifia as diagonais.
    diagonal = 1 #Começa com um pois vamos verificar apartir do movimento do jogador.
    nova_linha = linha
    nova_coluna = coluna
    for i in range(pecas_acaba-1): #Como já temos uma peça, iremos verificar as outras três posições para ver se tem o elemento do jogador.
        nova_linha += 1
        nova_coluna += 1
        if nova_linha > (len(tabuleiro)-1) or nova_coluna > (len(tabuleiro )-1): #Essa condição é para não ultrapassar o tamanho do tabuleiro, o que iria ocasionar 'List index out of the range'.
            return diagonal
        else:
            if tabuleiro[nova_linha][nova_coluna] == jogador: #Verifica se os caracteres nas diagonais são iguais a 'O' ou 'X'.
                diagonal += 1
            else: #Se o caractere não for igual ao anterior, a sequência fica com 1 novamente.
                diagonal = 1
    return diagonal

def Diagonais_Subindo_Secundaria(tabuleiro,jogador,linha,coluna,pecas_acaba): #Nesta função ela recebe a posiçao que o jogador pois sua peça e verifia as diagonais.
    diagonal = 1 #Começa com um pois vamos verificar apartir do movimento do jogador.
    nova_linha = linha
    nova_coluna = coluna
    for i in range(pecas_acaba-1): #Como já temos uma peça, iremos verificar as outras três posições para ver se tem o elemento do jogador.
        nova_linha -= 1
        nova_coluna += 1
        if nova_linha < 0 or nova_coluna > (len(tabuleiro) - 1): #Essa condição é para não ultrapassar o tamanho do tabuleiro, o que iria ocasionar 'List index out of the range'.
            return diagonal
        else:
            if tabuleiro[nova_linha][nova_coluna] == jogador:
                diagonal += 1
            else: #Se o caractere não for igual ao anterior, a sequência fica com 1 novamente.
                diagonal = 1
    return diagonal
def Diagonais_Descendo_Secundaria(tabuleiro,jogador,linha,coluna,pecas_acaba): #Nesta função ela recebe a posiçao que o jogador pois sua peça e verifia as diagonais.
    diagonal = 1
    nova_linha = linha
    nova_coluna = coluna
    for i in range(pecas_acaba-1):
        nova_linha += 1
        nova_coluna -= 1
        if nova_linha > (len(tabuleiro)-1) or nova_coluna < 0: #Essa condição é para não ultrapassar o tamanho do tabuleiro, o que iria ocasionar 'List index out of the range'.
            return diagonal
        else:
            if tabuleiro[nova_linha][nova_coluna] == jogador:
                diagonal += 1
            else:
                diagonal = 1
    return diagonal

tamanho_do_jogo = input('O tamanho vai de 4 até 12.\nTamanho do Tabuleiro: ')
while tamanho_do_jogo.isdigit() == False: #Caso o valor fornecido não seja um número.
    print('Apenas numeros\nInsira o tamanho:')
    tamanho_do_jogo = input()

tamanho_do_jogo = int(tamanho_do_jogo)
while tamanho_do_jogo < 4 or tamanho_do_jogo>12: #Caso o tamanho do jogo não seja suficiente.
    print('O tamanho do seu tabuleiro tem que ser maior ou igual a 4 e menor ou igual a 12.\nInsira novo tamanho:')
    tamanho_do_jogo = input()
    while tamanho_do_jogo.isdigit() == False:  # Caso o valor fornecido não seja um número. #Caso o valor fornecido não seja um número.
        print('Apenas numeros\nInsira o tamanho:')
        tamanho_do_jogo = input()
    tamanho_do_jogo = int(tamanho_do_jogo)


if tamanho_do_jogo == 4:
    print('O jogo acaba quando um jogador juntar 4 peças.')

elif tamanho_do_jogo == 5:
    pecas_acaba = input('Com quantas peças o jogo finaliza?\nOpções: 4 ou 5 peças.')
    while pecas_acaba.isdigit() == False:  # Caso o valor fornecido não seja um número.
        print('Apenas numeros\nInsira a quantidade que encerra:')
        pecas_acaba = input()
    pecas_acaba = int(pecas_acaba)
    while pecas_acaba <4 or pecas_acaba>5:
        print('Apenas opções dada. Opções: 4 ou 5 peças.')
        pecas_acaba = input()
        pecas_acaba = int(pecas_acaba)
else:
    pecas_acaba = input('Com quantas peças o jogo finaliza?\nOpções: 4 a 6 peças')
    while pecas_acaba.isdigit() == False:  # Caso o valor fornecido não seja um número.
        print('Apenas numeros\nInsira a quantidade que encerra:')
        pecas_acaba = input()
    pecas_acaba = int(pecas_acaba)
    while pecas_acaba < 4 or pecas_acaba > 6:
        print('Apenas opções dada. Opções: 4 ou 5 peças.')
        pecas_acaba = input()
        pecas_acaba = int(pecas_acaba)


pecas_acaba = int(pecas_acaba)
vazio = '\033[30;47m-\033[m'
tabuleiro = Matriz(tamanho_do_jogo,vazio)[0]
colunas_jogaveis = Matriz(tamanho_do_jogo,vazio)[1]

for i in range(tamanho_do_jogo): #Para imprimir as colunas.
    print(colunas_jogaveis[i], end=' ')
print()

for i in range(tamanho_do_jogo): #Para imprimir o tabuleiro sem peças.
    for j in range(tamanho_do_jogo):
        print(tabuleiro[i][j], end=' ')
    print()

vez = 0
while True: #Jogadas.
    if vez % 2 == 0: #Se for par, quem mexe é o primeiro jogador.
        numero_jogador,jogador = 1,'\033[0;30;41mO\033[m'
    else:
        numero_jogador,jogador = 2,'\033[0;30;44mX\033[m'

    print('Vez do Jogador',numero_jogador)
    coluna = input('informe a coluna:')
    while coluna.isdigit() == False:  # Verifica se é um numero.
        print('Apenas numeros\nInsira Coluna:')
        coluna = input()

    coluna = int(coluna)
    while (coluna >= tamanho_do_jogo):  # Verifica se é maior que o tabuleiro.
        print('Coluna inexistente')
        coluna = input('informe a coluna:')
        while coluna.isdigit() == False:  # Verifica se a novo coluna é numero.
            print('Apenas numeros\nInsira Coluna:')
            coluna = input()
        coluna = int(coluna)

    coluna_cheia = Coluna_cheia(coluna,vazio)
    while coluna_cheia == True:  # Verifica se a coluna já está toda preenchida.
        print('Coluna cheia\nInsira nova coluna:')
        coluna = input()
        while coluna.isdigit() == False:  # Verifica se a novo coluna é numero.
            print('Apenas numeros\nInsira Coluna:')
            coluna = input()

        coluna = int(coluna)
        coluna_cheia = Coluna_cheia(coluna,vazio)
        if coluna_cheia == False:
            break

    novo_tabuleiro = Jogada(tabuleiro, coluna, jogador, tamanho_do_jogo,vazio)  # Tabuleiro formado depois da jogada.
    linha_usada = Linha_usada(tabuleiro, coluna, tamanho_do_jogo)
    tabuleiro = novo_tabuleiro  # Substuindo no Tabuleiro principal.

    for i in range(tamanho_do_jogo):  # Para imprimir as colunas.
        print(colunas_jogaveis[i], end=' ')
    print()

    for i in range(tamanho_do_jogo):  # Imprime o Tabuleiro.
        for j in range(tamanho_do_jogo):
            print(novo_tabuleiro[i][j], end=' ')
        print()

    dia_sub_prin = Diagonais_Subindo_Principal(novo_tabuleiro, jogador, linha_usada, coluna,pecas_acaba)
    dia_desc_prin = Diagonais_Descendo_Principal(novo_tabuleiro, jogador, linha_usada, coluna,pecas_acaba)
    dia_sub_sec = Diagonais_Subindo_Secundaria(novo_tabuleiro, jogador, linha_usada, coluna,pecas_acaba)
    dia_desc_sec = Diagonais_Descendo_Secundaria(novo_tabuleiro, jogador, linha_usada, coluna,pecas_acaba)
    linha = Linha(novo_tabuleiro, tamanho_do_jogo, jogador,pecas_acaba)
    coluna = Coluna(novo_tabuleiro, tamanho_do_jogo, jogador,pecas_acaba)

    if linha == pecas_acaba or coluna == pecas_acaba or dia_sub_prin == pecas_acaba or dia_desc_prin == pecas_acaba or dia_sub_sec == pecas_acaba or dia_desc_sec == pecas_acaba:  # Verifica se o jogador venceu.
        print('Jogador',numero_jogador,'é o vencedor')
        # print('Desenvolvido por João Carlos e Matheus Matos.')
        break

    elif Emapte(novo_tabuleiro,vazio) == 0:
        print("Empate")
        break

    else:
        vez += 1
