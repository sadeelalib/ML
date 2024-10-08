'''
from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Sample words
words = ["running", "jumps", "easily", "fairly"]

# Apply stemming
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed Words:", stemmed_words)


'''

from transformers import pipeline

# Load the sentiment-analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Example text
texts = [
    "I love programming!",
    "I'm not a fan of this weather.",
    "This is the best day ever!",
    "I'm feeling quite sad about the news."
]

# Analyze sentiment
results = sentiment_pipeline(texts)

# Print results
for text, result in zip(texts, results):
    print(f"Text: {text}\nSentiment: {result['label']} (Score: {result['score']:.4f})\n")
