from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import networkx as nx
import operator

# file = "p&p.txt"
file = "corpora/none.txt"

def score(sentence):
    line = sentence
    words = word_tokenize(line)
    score = [0] * 10
    for word in words:
        if word in mainDict:
            for i in range(len(score)):
                score[i] += mainDict[word][i]
    return score


def preprocess(list_of_strings):
    clean_strings = [x for x in list_of_strings if x not in
    [',', ':', '.', '\n', '--']]
    clean_strings = [x for x in clean_strings if x not in stopwords.words("english")]
    return clean_strings


def sim(a, b):
    from sys import maxsize
    words_a = word_tokenize(a)
    words_b = word_tokenize(b)
    return sum(1 for word1 in words_a
                 for word2 in words_b
                 if word1==word2)/maxsize


def create_graph(sentences):
    G = nx.Graph()
    for i, string in enumerate(sentences):
        try:
            a, b = string, sentences[i + 1]
            G.add_edge(a, b, weight=sim(a, b))
        except IndexError:
            pass
    return G


with open(file) as fp:
    # Read the text
    text = fp.read().lower()
    # Work on sentences
    sentences = sent_tokenize(text)

sentences = preprocess(sentences)

G = create_graph(sentences)
pr = nx.pagerank(G)
sorted_pr = {}

sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))[::-1]

for sent in sorted_pr[0:10]:
    print(sent)



# sentences[1]
# sentences[2]
#
# score(sentences[2])
# score(sentences[3])
# sim(sentences[2],sentences[3])


# import matplotlib.pyplot as plt
# pos=nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=2)
# nx.draw_networkx_edges(G, pos)
# plt.axis("off")
# plt.savefig("weighted_graph.png") # save as png
# plt.show()
#
# pos=nx.shell_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=2)
# nx.draw_networkx_edges(G, pos)
# plt.axis("off")
# plt.savefig("weighted_graph_shell.png") # save as png
# plt.show()
