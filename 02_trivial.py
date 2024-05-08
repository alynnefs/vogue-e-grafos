import matplotlib.pyplot as plt
import networkx as nx

# Creates the graph
G = nx.Graph()

# Creates the vertices
G.add_node(1)

# Creates the layout and draws the graph
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Edge characteristics
nx.draw_networkx(
    G,
    pos=pos,
    arrows=True,
    arrowstyle="-",
    with_labels=True,
)

plt.show()
