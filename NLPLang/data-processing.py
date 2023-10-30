# %%
import nltk
import chatterbot
from nltk import *

with open('nlp-input.txt') as dataset:
    lines = str(dataset.readlines())

tokenized = word_tokenize(lines)
stop_words = stopwords.words('english')

filtered_list = []

for word in tokenized:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

# stemmer = SnowballStemmer(language = 'english')
# stemmed_words = [stemmer.stem(word) for word in filtered_list]

tagged_words = nltk.pos_tag(filtered_list)
# for word in tagged_words

lemmatizer = WordNetLemmatizer()
lemmatized_words = []
for word, tag in tagged_words:
    wntag = tag[0].lower()
    wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
    if not wntag:
        lemma = (word)
    else:
        lemma = (lemmatizer.lemmatize(word, pos = wntag))
    lemmatized_words.append(lemma)

def extract_ne(array):
    tree = nltk.ne_chunk(tagged_words, binary = True)
    return set(
        " ".join(i[0] for i in t) 
        for t in tree
        if hasattr(t, "label")
    )

# named_entities = extract_ne(tagged_words)

# new_text = nltk.Text(lemmatized_words)
# freqdist = FreqDist(good_words)
# freqdist.most_common(20)

print(tagged_words)


