import matplotlib.pyplot as plt
import networkx as nx

# Creates the graph
G = nx.Graph()

# Creates the edges
G.add_edge(5, 2)
G.add_edge(5, 7)

G.add_edge(1, 2)
G.add_edge(2, 3)

G.add_edge(7, 6)
G.add_edge(7, 8)

print(nx.is_tree(G))

# Creates the layout and draws the graph
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Edge characteristics
nx.draw_networkx(
    G,
    pos=pos,
    arrows=True,
    arrowstyle="->",
    min_source_margin=15,
    min_target_margin=15,
    with_labels=True,
)

plt.show()
