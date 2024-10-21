from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "NLP is fun and exciting.",
    "Natural Language Processing is fun.",
    "I love learning about NLP."
]

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the vectorizer on the documents and transform them into TF-IDF vectors
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Get the feature names (the words that form the vocabulary)
vocab = tfidf_vectorizer.get_feature_names_out()

# Convert the TF-IDF matrix to an array to view the TF-IDF values
tfidf_array = tfidf_matrix.toarray()

# Display results
print("Vocabulary:", vocab)
print("TF-IDF Matrix:\n", tfidf_array)
