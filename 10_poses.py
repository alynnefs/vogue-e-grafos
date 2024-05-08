import matplotlib.pyplot as plt
import networkx as nx
import PIL

poses = {
    "1": "1.jpeg",
    "2": "2.jpeg",
    "3": "3.jpeg",
}

# Load images
images = {k: PIL.Image.open(fname) for k, fname in poses.items()}


# Creates the graph
G = nx.Graph()

# Add photos to nodes
G.add_node(1, image=images["1"])
G.add_node(2, image=images["2"])
G.add_node(3, image=images["3"])

# Creates the edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(3, 1)
G.add_edge(2, 3)
G.add_edge(2, 2)


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
    node_size=2500,
)

# Transformation of data coordinates (scaled between xlim and ylim) to visualization coordinates
tr_figure = ax.transData.transform
# Transform visualization into figure coordinates
tr_axes = fig.transFigure.inverted().transform

# Select the image size (relative to the X axis)
icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
icon_center = icon_size / 2.0

# Add the respective image to each node
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    # get overlapping axes and graph icon
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")

plt.show()
