from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import utility
import networkx as nx

"""
TODO:
-remove further words like 'mr.' or 'mrs.'
-optimize the windowsize
-maybe further preprocessing on top of lemmatization
-test other filters than Noun/Adjective
"""

def textRank(file):
    with open(file) as fp:
        # Read the text
        text = fp.read().lower()
        # Work on words
        words = word_tokenize(text)
        # Work on sentences
        #sentences = sent_tokenize(text) (not used)

    def preprocess(list_of_strings):
        #Clean strings from punctuation and stopwords
        clean_strings = [x for x in list_of_strings if x not in [',',':','.','?']]
        clean_strings = [x for x in clean_strings if x not in stopwords.words("english")]
        #remove additional words
        clean_strings = [x for x in clean_strings if x not in ['mr.', 'mrs.']]

        #get the pos tags of the words
        posTags = utility.posTag(clean_strings)
        #stem the words using the pos tags
        stemmed_strings = utility.lemmatize(clean_strings, posTags)

        #zip the result into  [[word1, tag],[word2, tag]...]
        result = []
        for i in range(len(stemmed_strings)):
            result.append([stemmed_strings[i], posTags[i][1]])

        return result


    def sim(word_pos_stream):
        """"
        This might be a more general solution for our structure--------------
        the similarity function return a dictionary of form:
        {
            "sourceWord": [["destinationWord", similarity],...],
            ...
        }
        """

        similarities = {}
        windowsize = 5
        i = 0
        while i < len(word_pos_stream) - windowsize - 1:
            #get the sliding window
            window = word_pos_stream[i: i + windowsize]
            #filter the sliding window
            window = [x[0] for x in window if x[1] in ['NN', 'NNP', 'NNS', 'NNPS', 'JJ', 'JJR', 'JJS']]

            for word in window:
                if word not in similarities.keys():
                    similarities[word] = []

                for otherWord in window:
                    if word != otherWord:
                        if otherWord not in similarities[word]:
                            similarities[word].append([otherWord, 1])
            i += 1

        return similarities

    def create_graph(list_of_edges):
        """
        This function receives a list of edges and
        returns a networkx graph
        """
        G = nx.Graph()
        for src, destinations in list_of_edges.items():
            for dest in destinations:
                try:
                    G.add_edge(src, dest[0], weight=dest[1])
                except IndexError:
                    pass
        return G

    print("prepocess...")
    preprocessedText = preprocess(words)#[0:500])
    print("find similarities...")
    similarities = sim(preprocessedText)
    print("create graph...")
    G = create_graph(similarities)

    pr = nx.pagerank(G)
    return G, pr
    # print(sorted(pr))
