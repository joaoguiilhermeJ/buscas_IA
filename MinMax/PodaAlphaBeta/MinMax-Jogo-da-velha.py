import math
import time

HUMANO = 'O'
COMPUTADOR = 'X'

def mostrar_tabuleiro(tab):
    print()
    for i in range(3):
        linha = tab[3*i : 3*i+3]
        print(' | '.join(c if c != ' ' else ' ' for c in linha))
        if i < 2:
            print('--+---+--')
    print()

def movimentos_possiveis(tab):
    return [i for i, v in enumerate(tab) if v == ' ']

def vencedor(tab):
    linhas_vitoria = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for a, b, c in linhas_vitoria:
        if tab[a] != ' ' and tab[a] == tab[b] == tab[c]:
            return tab[a]
    if ' ' not in tab:
        return 'EMPATE'
    return None

def utilidade(tab):
    v = vencedor(tab)
    if v == COMPUTADOR:
        return 1
    if v == HUMANO:
        return -1
    if v == 'EMPATE':
        return 0
    return None

def minimax(tab, jogador_atual, contar):
    u = utilidade(tab)
    if u is not None:
        contar['nos'] += 1
        return u

    if jogador_atual == COMPUTADOR:  # max
        melhor_valor = -math.inf
        for movimento in movimentos_possiveis(tab):
            tab[movimento] = COMPUTADOR
            valor = minimax(tab, HUMANO, contar)
            tab[movimento] = ' '
            if valor > melhor_valor:
                melhor_valor = valor
        return melhor_valor
    else:  # min
        melhor_valor = math.inf
        for movimento in movimentos_possiveis(tab):
            tab[movimento] = HUMANO
            valor = minimax(tab, COMPUTADOR, contar)
            tab[movimento] = ' '
            if valor < melhor_valor:
                melhor_valor = valor
        return melhor_valor

def melhor_jogada_minimax(tab):
    melhor_valor = -math.inf
    melhor_mov = None
    contar = {'nos': 0}
    inicio = time.time()

    for movimento in movimentos_possiveis(tab):
        tab[movimento] = COMPUTADOR
        valor = minimax(tab, HUMANO, contar)
        tab[movimento] = ' '
        if valor > melhor_valor:
            melhor_valor = valor
            melhor_mov = movimento

    fim = time.time()
    tempo = fim - inicio
    return melhor_mov, melhor_valor, contar['nos'], tempo

def jogar_humano_x_computador():
    tab = [' '] * 9
    turno = input("Quem começa? h para humano, c para computador ").strip().lower()
    jogador_atual = HUMANO if turno == 'h' else COMPUTADOR

    while True:
        mostrar_tabuleiro(tab)
        v = vencedor(tab)
        if v is not None:
            if v == 'EMPATE':
                print("Empate")
            else:
                print(f"Vitória de {v}!")
            break

        if jogador_atual == HUMANO:
            while True:
                try:
                    pos = int(input("Sua jogada (0-8): "))
                    if pos in movimentos_possiveis(tab):
                        tab[pos] = HUMANO
                        break
                    else:
                        print("Posição inválida.")
                except ValueError:
                    print("Digite um número entre 0 e 8.")
            jogador_atual = COMPUTADOR
        else:
            print("Computador Minimax pensando")
            mov, valor, nos, tempo = melhor_jogada_minimax(tab)
            tab[mov] = COMPUTADOR
            print(f"Computador jogou na posição {mov}.")
            print(f"Avaliação: {valor}, nós avaliados: {nos}, tempo: {tempo:.6f} s")
            jogador_atual = HUMANO

def jogar_computador_x_computador():
    tab = [' '] * 9
    jogador_atual = COMPUTADOR

    while True:
        mostrar_tabuleiro(tab)
        v = vencedor(tab)
        if v is not None:
            if v == 'EMPATE':
                print("Empate!")
            else:
                print(f"Vitória de {v}!")
            break

        print(f"Vez de {jogador_atual} Minimax")
        mov, valor, nos, tempo = melhor_jogada_minimax(tab)
        tab[mov] = jogador_atual
        print(f"Jogada na posição {mov}. Avaliação: {valor}, nós: {nos}, tempo: {tempo:.6f} s")

        jogador_atual = HUMANO if jogador_atual == COMPUTADOR else COMPUTADOR

if __name__ == "__main__":
    print("1 - Humano x Computador ")
    print("2 - Computador x Computador ")
    opc = input("Escolha uma opção: ").strip()
    if opc == '1':
        jogar_humano_x_computador()
    elif opc == '2':
        jogar_computador_x_computador()
    else:
        print("Opção inválida")
