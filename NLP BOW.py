from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love Natural Language Processing.",
    "Language Processing is fun.",
    "I enjoy learning NLP.",
    "NLP is a subset of AI."
]
# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit the vectorizer on the documents and transform them into a bag-of-words representation
X = vectorizer.fit_transform(documents)

# Get the feature names (the words that form the vocabulary)
vocab = vectorizer.get_feature_names_out()
'''
vectorizer = CountVectorizer(lowercase=False)
X = vectorizer.fit_transform(documents)
vocab = vectorizer.get_feature_names_out()
'''



# Convert the sparse matrix to an array to view the word counts
bow_matrix = X.toarray()

# Display results
print("Vocabulary:", vocab)
print("Bag of Words Matrix:\n", bow_matrix)


