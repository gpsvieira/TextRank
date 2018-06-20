from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import networkx as nx
import operator

from csv import DictReader
from scipy.spatial.distance import cosine as cossim

dictFile  = "dict.csv"
file = "corpora/p&p.txt"
mainDict = {}
cols = ["anger", "anticipation", "disgust", "fear",
        "joy", "negative", "positive", "sadness", "surprise", "trust"]


def score(word):
    score = [0] * 10
    if word in mainDict:
        for i in range(len(score)):
            score[i] += mainDict[word][i]
    return score


def preprocess(sentences):
    sentences = [re.sub('\"|\!|,|-|[0-9]|“|\'|\^', "", line).replace("\n", " ")
                 for line in sentences]
    sentences = [word for word in sentences if word not in
                 set(stopwords.words("english"))]
    return sentences


def sim(a, b):
    x = score(a)
    y = score(b)
    if sum(x) > 0 and sum(y) > 0:
        return cossim(x, y)
    return 0


def create_graph(sentences):
    G = nx.Graph()
    for i, string in enumerate(sentences):
        try:
            a, b = string, sentences[i + 1]
            G.add_edge(a, b, weight=sim(a, b))
        except IndexError:
            pass
    return G


with open(dictFile) as csvFile:
        reader = DictReader(csvFile)
        for row in reader:
            mainDict[row["Word"]] = [int(row[i]) for i in cols]

with open(file) as fp:
    # Read the text
    text = fp.read().lower()
    # Work on sentences
    sentences = sent_tokenize(text)
    # Work on words
    words = word_tokenize(text)

words = preprocess(words)

G = create_graph(words)
pr = nx.pagerank(G)
sorted_pr = {}

sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))[::-1]

for sent in sorted_pr[0:20]:
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
