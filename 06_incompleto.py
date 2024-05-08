import matplotlib.pyplot as plt
import networkx as nx

# Creates the graph
G = nx.Graph()

# Creates the edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)

# Creates the layout and draws the graph
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Edge characteristics
nx.draw_networkx(
    G,
    pos=pos,
    arrows=True,
    arrowstyle="-",
    min_source_margin=15,
    min_target_margin=15,
    with_labels=True,
)

plt.show()
