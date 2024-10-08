from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Example sentence
sentence = "running runs easily run"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Initialize the stemmer
stemmer = PorterStemmer()

# Apply stemming
stemmed_tokens = [stemmer.stem(word) for word in tokens]

print("Original Tokens:", tokens)
print("Stemmed Tokens:", stemmed_tokens)
