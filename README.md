
# Text Summarization using TextRank + ROUGE Evaluation

This project demonstrates a simple yet effective extractive text summarization system using the TextRank algorithm and evaluates its performance using the ROUGE metric. It works on the `us_train_data_final_OFFICIAL.jsonl` dataset and includes pre-processing, similarity matrix computation, and sentence ranking.

## Features
- Preprocessing of raw text data
- TextRank algorithm for unsupervised extractive summarization
- Sentence similarity matrix using cosine similarity
- ROUGE-1, ROUGE-2, and ROUGE-L evaluation
- Easily extendable and modular

## How It Works
1. **Preprocessing**: Clean and split the document into sentences.
2. **Build Similarity Matrix**: Compute sentence-to-sentence similarity using cosine similarity.
3. **TextRank Algorithm**: Construct a graph and apply PageRank to score sentences.
4. **Summary Generation**: Select top-scoring sentences.
5. **Evaluation**: Compute ROUGE scores comparing generated summary with reference.

## ROUGE Score Sample Output
```
ROUGE-1: 0.2881
ROUGE-2: 0.2830
ROUGE-L: 0.1833
```

These scores indicate a decent extractive summary quality with room for improvement using more advanced models like BERT.

## Project Structure
```
.
├── data/
│   └── us_train_data_final_OFFICIAL.jsonl     # Input dataset
├── preprocess.py                               # Text cleaning and sentence splitting
├── textrank.py                                 # TextRank implementation
├── similarity.py                               # Similarity matrix computation
├── Main.py                                     # Main script for summarization and evaluation
├── README.md                                   # This file
```

## Installation
1. Clone the repository:
   ```
   git clone 
   cd folder path
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the summarizer:
   ```
   python Main.py
   ```

## Input Format
JSONL format:
```
{"text": "Your document text goes here."}
```

## Evaluation Metrics
| Metric    | Description                                 |
|-----------|---------------------------------------------|
| ROUGE-1   | Unigram (word-level) overlap                 |
| ROUGE-2   | Bigram (2-word phrase) overlap               |
| ROUGE-L   | Longest common subsequence for fluency check |

## Future Improvements
- Use BERT for better semantic understanding
- Add abstractive summarization
- Deploy as a web-based tool

## Author
- Your Name :- Roshan Pandit
- Email:roshanpandit9922@gmail.com
- GitHub : roshanpandit65R

## License
This project is licensed under the MIT License.
