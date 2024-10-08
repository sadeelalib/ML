import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary resources
nltk.download('punkt_tab')
nltk.download('stopwords')

# Example sentence
sentence = "This is an example sentence demonstrating stopword removal."

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Get the list of stopwords in English
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

print("Original Tokens:", tokens)
print("Filtered Tokens (without stopwords):", filtered_tokens)
