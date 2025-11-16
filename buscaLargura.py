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

def busca_largura(balde_a, balde_b, alvo):
    if alvo > max(balde_a, balde_b):
        return None
    if alvo % mdc(balde_a, balde_b) != 0:
        return None
    
    inicio = (0, 0)
    fila = deque([inicio])
    pai = {inicio: None}
    acao_pai = {inicio: None}

    while fila:
        atual = fila.popleft()
        a, b = atual

        if a == alvo or b == alvo:
            caminho = []
            no = atual
            while no is not None:
                caminho.append((no, acao_pai[no]))
                no = pai[no]
            caminho.reverse()
            return caminho
        
        for vizinho, acao in gerar_vizinho(atual, balde_a, balde_b):
            if vizinho not in pai:
                pai[vizinho] = atual
                acao_pai[vizinho] = acao
                fila.append(vizinho)
    
    return None  

if __name__ == '__main__':
    capacidade_a = 4
    capacidade_b = 3
    objetivo = 2

    solucao = busca_largura(capacidade_a, capacidade_b, objetivo)

    if solucao is None:
        print('não tem solução')
    else:
        for estado, acao in solucao:
            if acao is None:
                print(f'estado inicial: {estado}')
            else:
                print(f'ação: {acao} -> estado: {estado}')
