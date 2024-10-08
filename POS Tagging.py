import nltk

# Download the required NLTK resources
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

# Example text for POS tagging
text = "Natural Language Processing is amazing."

# Tokenize the text into words
from nltk.tokenize import word_tokenize
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the POS tags
print("POS Tags:", pos_tags)
