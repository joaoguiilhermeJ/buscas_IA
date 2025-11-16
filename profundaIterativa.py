from collections import deque

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def gerar_vizinho(estado, balde_a, balde_b):
    a, b = estado
    vizinhos = []

    vizinhos.append(((balde_a, b), 'encher a'))
    vizinhos.append(((a, balde_b), 'encher b'))
    vizinhos.append(((0, b), 'esvaziar a'))
    vizinhos.append(((a, 0), 'esvaziar b'))

    colocar = min(a, balde_b - b)
    vizinhos.append(((a - colocar, b + colocar), 'A -> B'))

    colocar = min(b, balde_a - a)
    vizinhos.append(((a + colocar, b - colocar), 'B -> A'))

    return vizinhos

def busca_profunda(balde_a, balde_b, alvo, estado_atual, pai, acao_pai, limite, visitados_limite):
    a, b = estado_atual
    
    if limite == 0:
        return None
    
    if estado_atual in visitados_limite:
        return None
    
    visitados_limite.add(estado_atual)

    if a == alvo or b == alvo:
        caminho = []
        no = estado_atual
        while no is not None:
            caminho.append((no, acao_pai[no]))
            no = pai[no]
        caminho.reverse()
        return caminho

    for vizinho, acao in gerar_vizinho(estado_atual, balde_a, balde_b):
        if vizinho not in pai or pai[vizinho] == estado_atual:
            if vizinho not in pai:
                pai[vizinho] = estado_atual
                acao_pai[vizinho] = acao
            
            resultado = busca_profunda(balde_a, balde_b, alvo, vizinho, pai, acao_pai, limite - 1, visitados_limite)
            
            if resultado is not None:
                return resultado
    
    visitados_limite.remove(estado_atual)
    return None

def ids_jarros(balde_a, balde_b, alvo, max_depth=100):
    if alvo > max(balde_a, balde_b):
        return None
    if alvo % mdc(balde_a, balde_b) != 0:
        return None

    inicio = (0, 0)
    
    for limite in range(max_depth):
        pai = {inicio: None}
        acao_pai = {inicio: None}
        visitados_limite = set()
        
        resultado = busca_profunda(balde_a, balde_b, alvo, inicio, pai, acao_pai, limite, visitados_limite)
        
        if resultado is not None:
            return resultado
            
    return None 

if __name__ == '__main__':
    capacidade_a = 4
    capacidade_b = 3
    objetivo = 2

    solucao = ids_jarros(capacidade_a, capacidade_b, objetivo)

    if solucao is None:
        print("Sem solução encontrada")
    else:
        for estado, acao in solucao:
            if acao is None:
                print(f"Estado inicial: {estado}")
            else:
                print(f"Ação: {acao} -> Estado: {estado}")