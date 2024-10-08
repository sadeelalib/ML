import string
from nltk.tokenize import word_tokenize

# Example sentence
sentence = "Hello! This is a sample sentence, with punctuation marks."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Remove punctuation from tokens
tokens_without_punctuation = [word for word in tokens if word not in string.punctuation]

print("Original Tokens:", tokens)
print("Tokens without Punctuation:", tokens_without_punctuation)
