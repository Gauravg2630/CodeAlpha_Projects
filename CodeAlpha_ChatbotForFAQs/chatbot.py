import json
import nltk
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Download necessary NLTK data safely
# -----------------------------
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# -----------------------------
# Load FAQs from JSON file
# -----------------------------
def load_faq_data(path="data/faqs.json"):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Could not find the file at {path}")
        return []
    except json.JSONDecodeError:
        print("Error: JSON format is invalid.")
        return []

# -----------------------------
# Preprocess user/FAQ text:
# 1. Lowercase
# 2. Tokenize
# 3. Remove punctuation
# 4. Remove stopwords
# -----------------------------
def preprocess(text):
    try:
        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t not in string.punctuation]
        tokens = [t for t in tokens if t not in stopwords.words('english')]
        return " ".join(tokens)
    except Exception as e:
        print(f"Preprocessing error: {e}")
        return ""

# -----------------------------
# Get Best Matching Answer
# -----------------------------
def get_answer(user_input, faqs):
    if not faqs:
        return "Sorry, the FAQ database is empty or not loaded."

    corpus = [faq['question'] for faq in faqs]
    corpus.append(user_input)  # Add user input to compare

    # Preprocess all questions including user input
    processed_corpus = [preprocess(q) for q in corpus]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    try:
        vectors = vectorizer.fit_transform(processed_corpus)
    except ValueError:
        return "Error processing the input. Please ask a valid question."

    # Cosine similarity of user input with all FAQ questions
    sim_scores = cosine_similarity(vectors[-1], vectors[:-1])
    best_match_idx = np.argmax(sim_scores)
    best_score = sim_scores[0, best_match_idx]

    if best_score > 0.2:
        return faqs[best_match_idx]['answer']
    else:
        return "Sorry, I couldn't find a matching answer."
