import matplotlib.pyplot as plt

def plot_a_graph(G):
    """
    look up: https://networkx.github.io/documentation/stable/index.html
    """
    pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=2)
    nx.draw_networkx_edges(G, pos)
    plt.axis('off')
    plt.savefig("weighted_graph.png") # save as png
    plt.show()
