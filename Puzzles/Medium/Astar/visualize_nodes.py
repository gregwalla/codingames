import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('examples/slightlylargernodes.txt', nodetype=int, data=(('cost',int),))

G.nodes()
G.edges(data = True)

pos = nx.spring_layout(G)
nx.draw(G, with_labels=1, pos=pos)
labels = nx.get_edge_attributes(G,'cost')
nx.draw_networkx_edge_labels(G, edge_labels=labels, pos=pos )

plt.show()