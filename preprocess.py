import json
import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

def preprocess_text(text):
    sentences = sent_tokenize(text)  # Proper sentence splitting
    clean_sentences = [s.strip().lower() for s in sentences if len(s.split()) > 3]  # Remove short fragments
    return clean_sentences

 # Ensure it returns a list of sentences

def load_jsonl(file_path):
    """Loads JSONL file and returns a list of dictionaries."""
    data = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data

def extract_texts(data):
    """Extracts text from JSON data."""
    return [item["text"] for item in data]
