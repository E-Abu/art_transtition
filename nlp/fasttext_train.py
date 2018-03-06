import fasttext

train_source = '/Users/eva/Downloads/wikipedia-extractor/extracted/general.txt'

# Skipgram model
model = fasttext.skipgram(train_source, 'model', dim=300)
print(model.words) # list of words in dictionary



