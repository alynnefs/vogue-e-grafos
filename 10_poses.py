import matplotlib.pyplot as plt
import networkx as nx
import PIL

poses = {
    "1": "1.jpeg",
    "2": "2.jpeg",
    "3": "3.jpeg",
}

# Carrega imagens
images = {k: PIL.Image.open(fname) for k, fname in poses.items()}


# Cria o grafo
G = nx.Graph()

# Adiciona as fotos nos nós
G.add_node(1, image=images["1"])
G.add_node(2, image=images["2"])
G.add_node(3, image=images["3"])

# Cria as arestas
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(3, 1)
G.add_edge(2, 3)
G.add_edge(2, 2)


# Cria o layout e desenha o grafo
pos = nx.spring_layout(G)
fig, ax = plt.subplots()

# Características das arestas
nx.draw_networkx(
    G,
    pos=pos,
    arrows=True,
    arrowstyle="->",
    min_source_margin=15,
    min_target_margin=15,
    with_labels=True,
    node_size=2500
)

# Transformação de coordenadas de dados (escaladas entre xlim e ylim) para coordenadas de visualização
tr_figure = ax.transData.transform
# Transformar a visualização em coordenadas de figuras
tr_axes = fig.transFigure.inverted().transform

# Selecionar o tamanho da imagem (relativamente ao eixo X)
icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
icon_center = icon_size / 2.0

# Adicionar a respectiva imagem a cada nó
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    # obter eixos sobrepostos e ícone do gráfico
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")

plt.show()
