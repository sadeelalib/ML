from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

# Example documents
documents = [
    "I love natural language processing and machine learning.",
    "Natural language processing is a field of artificial intelligence.",
    "Machine learning is fun and exciting.",
    "Artificial intelligence and machine learning go hand in hand."
]

# Tokenize the sentences into words
tokenized_docs = [word_tokenize(doc.lower()) for doc in documents]

# Initialize and train the Word2Vec model
model = Word2Vec(tokenized_docs, vector_size=100, window=5, min_count=1, sg=1)  # sg=1 for Skip-gram model

# Get the vector for a word (e.g., 'machine')
word_vector = model.wv['machine']
print("Vector for 'machine':\n", word_vector)

# Find the most similar words to 'machine'
similar_words = model.wv.most_similar('machine', topn=10)
print("\nMost similar words to 'machine':\n", similar_words)

# Find analogy: 'king' - 'man' + 'woman' = ?
# Here we'll substitute with related words like 'learning' - 'fun' + 'exciting'
result = model.wv.most_similar(positive=['learning', 'exciting'], negative=['fun'], topn=1)
print("\nAnalogy ('learning' - 'fun' + 'exciting') result:\n", result)
