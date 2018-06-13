from nltk.tokenize import sent_tokenize, word_tokenize
import re
import networkx as nx
import editdistance


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
        clean_strings = [re.sub('"\n\!\'', '', line)
                         for line in list_of_strings]
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

    G = create_graph(words)

    pr = nx.pagerank(G)
    return pr
    # print(sorted(pr))
