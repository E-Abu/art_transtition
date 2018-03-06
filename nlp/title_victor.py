from __future__ import print_function
from gensim.models import KeyedVectors

import pandas as pd
import pickle

import jieba



#load in the genaral modle
model = KeyedVectors.load_word2vec_format('./statics/model.vec')

#load in the artwork_sample
file_name = '../data/artwork_sample.csv'
artworks = pd.read_csv(file_name)

artworks['title'] = artworks['title'].fillna('无')
artworks['description'] = artworks['description'].fillna('无')

#load in word frequency
f = open('./statics/frequency','rb')
frequency = pickle.load(f)
f.close()

#title vector
def title_victor(artworks):
    artworks_vict = [0] * len(artworks)
    for i in range(len(artworks)):
        text = artworks.title[i]

        try:
            word_list = list(jieba.cut(text))
        except AttributeError:
            word_list = [text]
        word_list = [i for i in word_list if i != ' ']

        print(word_list)

        vic_list = []
        for k in word_list:
            try:
                vic_list.append(model.wv[k])
            except KeyError:
                pass

        if len(vic_list) > 0:
            title_vic = sum(vic_list[j] / (frequency[word_list[j]] + 1000) for j in range(len(vic_list))) / len(vic_list)
            artworks_vict[i] = title_vic
            print(model.similar_by_vector(title_vic, topn=1))
        else:
            title_vic = vic_list
            artworks_vict[i] = title_vic
            print(word_list)
