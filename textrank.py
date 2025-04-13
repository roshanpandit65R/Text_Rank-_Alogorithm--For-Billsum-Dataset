import numpy as np
from preprocess import preprocess_text
from similarity import build_similarity_matrix

def text_rank(sentences, similarity_matrix):
    """Applies the TextRank algorithm to rank sentences."""
    sentence_count = len(sentences)
    scores = np.ones(sentence_count)

    # Run PageRank algorithm
    damping_factor = 1
    threshold = 0.0001
    max_iterations = 4000

    for _ in range(max_iterations):
        prev_scores = np.copy(scores)
        for i in range(sentence_count):
            scores[i] = (1 - damping_factor) + damping_factor * sum(
                similarity_matrix[i][j] * scores[j] for j in range(sentence_count) if i != j
            )
        if np.abs(scores - prev_scores).sum() < threshold:
            break

    ranked_sentences = [sentences[i] for i in np.argsort(scores)[::-1]]
    return ranked_sentences
