from plotting_example import plot_a_graph
import operator

#from template import textRank
from slidingWindow import textRank

G, pr = textRank(file="corpora/hp.txt")

sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
sorted_pr = sorted_pr[::-1]
print(sorted_pr[0:10])
plot_a_graph(G)
