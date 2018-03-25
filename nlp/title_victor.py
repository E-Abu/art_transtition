from __future__ import print_function
from gensim.models import KeyedVectors

import pandas as pd
import pickle
import jieba

#from nlp.tool import cut_sentence



#load in the genaral modle
model = KeyedVectors.load_word2vec_format('./statics/model.vec')

#load in the artwork info
file_name = '../data/artworkstxt_info_west.csv'
artworks = pd.read_csv(file_name, error_bad_lines=False)

#title vector file addr
file_title_vect = './statics/title_vect_west.vec'

#artworks = artworks[:100]

artworks = artworks.fillna('无')


#load in word frequency
frequency_pickle_addr = './statics/frequency'
f = open(frequency_pickle_addr,'rb')
frequency = pickle.load(f)
f.close()


#title vector
def title_victor(artworks):
    artworks_vict = [0] * len(artworks)
    for i in range(len(artworks)):
        if i % 100 == 0: print("{}/{}".format(i, len(artworks)))
        text = artworks[i]

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

        #vic_list,word_list = cut_sentence(text)

        if len(vic_list) > 0:
            title_vic = sum(vic_list[j] * 1000/ (frequency[word_list[j]] + 1000) for j in range(len(vic_list))) / len(vic_list)
            artworks_vict[i] = title_vic
            #print(model.similar_by_vector(title_vic, topn=1))
        else:
            title_vic = vic_list
            artworks_vict[i] = title_vic

    return artworks_vict, word_list

artworks_vict, word_list = title_victor(artworks.title)
print(len(artworks_vict))

'''
这个东西太大了不能pickle，可以尝试将它存成gensim的那种.vec,看一看那样行不行
f = open('./statics/artworks_vict','wb')

pickle.dump(title_vict,f)
f.close()
'''




def write_title_vect(artwork_vector, file_title_vect):
    error_num = 0
    with open(file_title_vect, 'w', encoding='utf-8') as f:
        f.write(str(len(artwork_vector)) + ' ' +'300' + '\n')
        for v in range(len(artwork_vector)):
            if v % 100 == 0: print("{}/{}".format(v, len(artwork_vector)))

            if not len(artwork_vector[v]) == 300:
                error_num += 1
                continue

            array_text = ''

            for vect in artwork_vector[v]:
                array_text = array_text + ' ' + str(vect)

            text_word = str(v) + array_text + '\n'

           # with open(file_title_vect,'a',encoding='utf-8') as f:
            f.write(text_word)
        print('error num:{}'.format(error_num))
    return error_num


error_num = write_title_vect(artworks_vict, file_title_vect)



# 第一排总数改掉
import shutil

from_file = open(file_title_vect)
line = from_file.readline()

line_s = line.split(' ')
line_s[0] = str(int(line_s[0]) - error_num)
line = line_s[0] + ' ' + line_s[1]


to_file = open(file_title_vect + '_new', mode="w")
to_file.write(line)
shutil.copyfileobj(from_file, to_file)

