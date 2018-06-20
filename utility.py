import nltk
from nltk.corpus import wordnet as wn

def posTag(token_stream):
    return nltk.pos_tag(token_stream)

def lemmatize(token_stream, posTags):
    # Initialize the lemmatizer
    lemmatizer = nltk.WordNetLemmatizer()

    def wntag(pttag):
        if pttag in ['JJ', 'JJR', 'JJS']:
            return wn.ADJ
        elif pttag in ['NN', 'NNS', 'NNP', 'NNPS']:
            return wn.NOUN
        elif pttag in ['RB', 'RBR', 'RBS']:
            return wn.ADV
        elif pttag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']:
            return wn.VERB
        return None

    def lemmatize(lemmatizer, word, pos):
        if pos == None:
            return word
        else:
            return lemmatizer.lemmatize(word, pos)

    lemmata = [lemmatize(lemmatizer, word, wntag(pos)) for (word, pos) in posTags]
    return lemmata
