from textblob import TextBlob

text = "I love this product! It's absolutely amazing."
blob = TextBlob(text)

# Get the sentiment polarity: -1 (negative) to 1 (positive)
print("Sentiment Polarity:", blob.sentiment.polarity)
