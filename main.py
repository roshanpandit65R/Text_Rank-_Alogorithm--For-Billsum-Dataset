from preprocess import load_jsonl, preprocess_text
from textrank import text_rank
from similarity import build_similarity_matrix
from rouge_score import rouge_scorer

def summarize_text(text, num_sentences=3):
    sentences = preprocess_text(text)
    
    if not sentences:
        return "No valid sentences found."
    
    similarity_matrix = build_similarity_matrix(sentences)
    ranked_sentences = text_rank(sentences, similarity_matrix)

    # Select top-ranked sentences ensuring brevity
    summary = []
    seen_sentences = set()

    for sentence in ranked_sentences:
        if sentence not in seen_sentences and 8 <= len(sentence.split()) <= 100:  # Ensure sentence length
            summary.append(sentence)
            seen_sentences.add(sentence)
        if len(summary) >= num_sentences:
            break

    return " ".join(summary)

# Function to compute ROUGE scores
def compute_rouge_scores(reference_text, generated_summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_text, generated_summary)
    
    return {
        "ROUGE-1": scores["rouge1"].fmeasure,
        "ROUGE-2": scores["rouge2"].fmeasure,
        "ROUGE-L": scores["rougeL"].fmeasure
    }

# Load and process data
data = load_jsonl("./data/us_train_data_final_OFFICIAL.jsonl")  # Ensure file path is correct

for i, doc in enumerate(data[:1]):  # Test with first document
    text = doc["text"]
    generated_summary = summarize_text(text)

    print(f"=== Summary for Document {i+1} ===")
    print(generated_summary)

    # Compute ROUGE Scores
    rouge_scores = compute_rouge_scores(text, generated_summary)

    print("\nROUGE Scores:")
    for metric, score in rouge_scores.items():
        print(f"{metric}: {score:.4f}")
