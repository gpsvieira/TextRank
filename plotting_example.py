import matplotlib.pyplot as plt
import networkx as nx
import operator

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


def histogram(pageRank):
    #sorted_pr = sorted(pageRank.items(), key=operator.itemgetter(1))
    #sorted_pr = sorted_pr[::-1]

    hist = {}
    for word in pageRank:
        score = round(word[1], 3)
        if score not in hist.keys():
            hist[score] = 0

        hist[score] += 1

    x = sorted(hist)
    x = x[::-1]
    y = []
    for i in x:
        y.append(hist[i])

    plt.plot(x, y)
    plt.show()