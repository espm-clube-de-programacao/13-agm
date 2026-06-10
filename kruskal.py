def kruskal(n, arestas):
    # arestas: lista de (peso, u, v)
    pai = list(range(n))
 
    def find(x):
        while pai[x] != x: # enquanto o x não for a raiz (é raiz qd ele for igual ao pai dele)
            pai[x] = pai[pai[x]]   # x passa a apontar para o avô
            x = pai[x] # sobe um nível
        return x # achou a raiz
 
    def union(a, b):
        pai[find(a)] = find(b)
 
    agm, custo = [], 0
    for peso, u, v in sorted(arestas):
        if find(u) != find(v):     # nao forma ciclo
            union(u, v)
            agm.append((u, v, peso))
            custo += peso
    return agm, custo

# (peso, u, v)
arestas = [
            (7,0,1),(3,0,2),(4,1,2),
            (2,1,3),(5,2,3),(6,2,4),
            (4,3,4),(5,3,5),(8,4,5)
          ]

# o valor 6 indica o total de vértices no grafo
print(kruskal(6, arestas)) # custo = 18
