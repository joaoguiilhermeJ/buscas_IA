import heapq
import time

def conflitos(state):
    conflitos = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflitos += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def sem_conflito_parcial(state, nova_linha):
    nova_coluna = len(state)
    for col, linha in enumerate(state):
        if linha == nova_linha:
            return False
        if abs(linha - nova_linha) == abs(col - nova_coluna):
            return False
    return True

def sucessores(state, n):
    col = len(state)
    if col >= n:
        return []
    suces = []
    for row in range(n):
        if sem_conflito_parcial(state, row):
            suces.append(state + [row])
    return suces

def objetivo(state, n):
    return len(state) == n

def a_estrela_n_rainha(n):
    inicio_tempo = time.time()
    estado_inicio = []
    g_inicial = 0
    h_inicial = conflitos(estado_inicio)
    f_inicial = g_inicial + h_inicial
    fronteira = []
    heapq.heappush(fronteira, (f_inicial, g_inicial, estado_inicio))
    visitados = set()
    expandidos = 0

    while fronteira:
        f_atual, g_atual, estado_atual = heapq.heappop(fronteira)
        expandidos += 1

        if objetivo(estado_atual, n):
            fim_tempo = time.time()
            tempo_total = fim_tempo - inicio_tempo
            return estado_atual, expandidos, tempo_total

        chave = tuple(estado_atual)
        if chave in visitados:
            continue
        visitados.add(chave)

        for estado_sucessor in sucessores(estado_atual, n):
            g_novo = g_atual + 1
            h_novo = conflitos(estado_sucessor)
            f_novo = g_novo + h_novo
            heapq.heappush(fronteira, (f_novo, g_novo, estado_sucessor))

    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo
    return None, expandidos, tempo_total

def gulosa_n_rainhas(n):
    inicio_tempo = time.time()
    estado_inicial = []
    h_inicial = conflitos(estado_inicial)
    fronteira = []
    heapq.heappush(fronteira, (h_inicial, estado_inicial))
    visitados = set()
    expandidos = 0

    while fronteira:
        h_atual, estado_atual = heapq.heappop(fronteira)
        expandidos += 1

        if objetivo(estado_atual, n):
            fim_tempo = time.time()
            tempo_total = fim_tempo - inicio_tempo
            return estado_atual, expandidos, tempo_total

        chave = tuple(estado_atual)
        if chave in visitados:
            continue
        visitados.add(chave)

        for estado_sucessor in sucessores(estado_atual, n):
            h_novo = conflitos(estado_sucessor)
            heapq.heappush(fronteira, (h_novo, estado_sucessor))

    fim_tempo = time.time()
    tempo_total = fim_tempo - inicio_tempo
    return None, expandidos, tempo_total

if __name__ == "__main__":
    n = 10
    sol_astar, exp_astar, tempo_astar = a_estrela_n_rainha(n)
    print("A*")
    print("Solução:", sol_astar)
    print("Nós expandidos:", exp_astar)
    print("Tempo:", tempo_astar)
    sol_gulosa, exp_gulosa, tempo_gulosa = gulosa_n_rainhas(n)
    print("\nGulosa")
    print("Solução:", sol_gulosa)
    print("Nós expandidos:", exp_gulosa)
    print("Tempo:", tempo_gulosa)
