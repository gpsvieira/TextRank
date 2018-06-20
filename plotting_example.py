import matplotlib.pyplot as plt
import networkx as nx

def plot_a_graph(G):
    """
    look up: https://networkx.github.io/documentation/stable/index.html
    """
    options = {
        'node_color': 'red',
        'node_size': 100,
        'width': 2,
    }
    nx.draw_networkx(G, **options)
    plt.axis('off')
    plt.show()
