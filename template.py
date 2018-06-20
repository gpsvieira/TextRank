from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import networkx as nx
import editdistance
import operator


def textRank(file):
    with open(file) as fp:
        # Read the text
        text = fp.read().lower()
        # Work on words
        words = word_tokenize(text)
        # Work on sentences
        sentences = sent_tokenize(text)

    def preprocess(list_of_strings):
        """
        Clean your strings (words or sentences)
        """
        clean_strings = [re.sub('\"|\n|\!|,|-|[0-9]|“|\'', "", line)
                         for line in list_of_strings]
        clean_strings = [word for word in clean_strings if word not in
                         set(stopwords.words("english"))]
        return clean_strings

    sentences = preprocess(sentences)

    def sim(a, b):
        """
        This is the core of the similarity measure
        """
        return 1 / (editdistance.eval(a, b) + 0.000000000001)

    def create_graph(list_of_strings):
        """
        This function receives a list of strings (words or sentences)
        returns a networkx graph
        """
        G = nx.Graph()
        for i, string in enumerate(list_of_strings):
            try:
                a, b = string, list_of_strings[i + 1]
                G.add_edge(a, b, weight=sim(a, b))
            except IndexError:
                pass
        return G

    G = create_graph(sentences)

    pr = nx.pagerank(G)
    sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
    return sorted_pr[::-1]
    # print(sorted(pr))
