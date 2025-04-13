import numpy as np
import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
  
def build_similarity_matrix(sentences):
    """Builds a similarity matrix using TF-IDF and cosine similarity."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    return cosine_similarity(tfidf_matrix)


def create_graph(similarity_matrix):
    """Creates a graph from the similarity matrix using NetworkX."""
    graph = nx.Graph()
    for i in range(len(similarity_matrix)):
        for j in range(len(similarity_matrix)):
            if i != j:  # Avoid self-loops
                graph.add_edge(i, j, weight=similarity_matrix[i][j])
    return graph
