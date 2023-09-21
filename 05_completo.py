import matplotlib.pyplot as plt
import networkx as nx

# Cria o grafo
G = nx.Graph()

# Cria as arestas
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3, 4)

# Cria o layout e desenha o grafo
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Características das arestas
nx.draw_networkx(
    G,
    pos=pos,
    arrows=True,
    arrowstyle="-",
    min_source_margin=15,
    min_target_margin=15,
    with_labels=True
)

plt.show()
