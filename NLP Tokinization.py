import nltk
nltk.download('punkt_tab')  # Ensure 'punkt' is downloaded

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Natural Language Processing is exciting. Let's explore it!"

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)

'''
# Example sentence
sentence = "Natural Language Processing is FUN!"

# Converting to lowercase
lowercase_sentence = sentence.lower()

print(lowercase_sentence)
'''