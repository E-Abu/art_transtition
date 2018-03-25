from __future__ import print_function
from gensim.models import KeyedVectors

import jieba

# Creating the model
model = KeyedVectors.load_word2vec_format('./statics/model.vec')



def cut_sentence(input_sentence):
    try:
        word_list = list(jieba.cut(input_sentence))
    except AttributeError:
        word_list = [input_sentence]

    print(word_list)

    vic_list = []
    for k in word_list:
        try:
            vic_list.append(model.wv[k])
        except KeyError:
            pass
    return vic_list, word_list

