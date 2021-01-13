import numpy as np
from paris import grafo_paris, heuristica_paris


def a_star(partida, destino, grafo, heuristica):
    h = heuristica[destino]
    # Lista com os nós abertos, cada elemento é (nó, f, g, caminho)
    # Inicializada com o nó de partida e f e g = 0
    abertos = [(partida, 0, 0, [partida])]
    fechados = list()
    # Enquanto houverem nós abertos
    while abertos:
        abertos = np.array(abertos)
        # Encontra o nó com menor f entre os nós abertos
        i_atual = abertos.argmin(axis=0)[1]
        # Faz dele o nó atual
        atual = abertos[i_atual]
        # Remove ele da lista de abertos
        abertos = np.delete(abertos, i_atual, axis=0)
        # Acrescenta ele na lista de fechados
        fechados.append(atual[0])
        # Se for o destino, retorna o caminho e a distância percorrida
        if atual[0] == destino:
            return atual[3], atual[2]
        # Para cada nó vizinho do nó atual
        for vizinho in grafo[atual[0]]:
            # Se o nó vizinho se encontra na lista de fechados, pular para o próximo nó
            if vizinho["para"] in fechados:
                continue
            # Calcula g, h e f do nó
            g_vizinho = atual[2] + vizinho["custo"]
            h_vizinho = h[vizinho["para"]]
            f_vizinho = g_vizinho + h_vizinho
            abertos = np.array(abertos)
            # Se o nó já está aberto e tiver custo maior que na lista de aberto, pular para o próximo nó
            if vizinho["para"] in abertos[:, 0]:
                i_vizinho = np.where(abertos[:, 0] == vizinho["para"])
                if g_vizinho > abertos[i_vizinho][0][2]:
                    continue
            # Computa o caminho até o nó
            caminho = atual[3].copy()
            caminho.append(vizinho["para"])
            abertos = list(abertos)
            # Coloca o nó na lista de abertos
            abertos.append((vizinho["para"], f_vizinho, g_vizinho, caminho))
        abertos = list(abertos)
    return False


print(a_star("E6", "E13", grafo_paris, heuristica_paris))
