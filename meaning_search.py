from __future__ import print_function
from gensim.models import KeyedVectors
import jieba

from color_extract.picture_things import pull_picture
from color_extract.picture_things import fill_color_demo
from color_extract.picture_things import color_extract



# Creating the model
model = KeyedVectors.load_word2vec_format('./statics/model.vec')
title_vect = KeyedVectors.load_word2vec_format('./nlp/statics/title_vect.vec_new', binary=False)  # C text format

input_sentence= '快乐的女人'

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


def input2vect(input_sentence):
    vic_list = cut_sentence(input_sentence)

    if len(vic_list) > 0:
        input_vic = sum(vic_list[j] for j in range(len(vic_list))) / len(vic_list)
        # print(model.similar_by_vector(title_vic, topn=1))
    else:
        input_vic = vic_list

    return  input_vic

vic = input2vect(input_sentence)
pictures = title_vect.similar_by_vector(vic, topn=10)







