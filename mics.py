import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')  # Optional, for more word translations

from nltk.corpus import wordnet as wn
'''
# Get synsets for the word "dog"
synsets = wn.synsets('good')
print(synsets)

# Get the first synset and its definition
dog_synset = synsets[1]
print(dog_synset.definition())

# Get the lemmas (synonyms)
synonyms = dog_synset.lemmas()
for lemma in synonyms:
    print(lemma.name())
    
    
'''
# Get antonyms of the word "good"
good = wn.synsets('good')[0]
antonyms = good.lemmas()[0].antonyms()
if antonyms:
    print("Antonyms of 'good':", [antonym.name() for antonym in antonyms])

