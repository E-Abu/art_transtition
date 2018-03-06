import collections
import pickle


'''
根据词频，来更新训练用的general词汇表
根据词频，来做题目向量的加权
'''

def get_word_frequency():
    dbtext_file = '/Users/eva/Downloads/wikipedia-extractor/extracted/db.txt'
    with open(dbtext_file, 'r', encoding='utf-8') as f:
        text = f.read()

    frequency = collections.Counter(text.split())
    total = sum(frequency.values())
    probability = {k: v / total for k,v in frequency.items()}

    f2 = open('./statics/frequency','wb')
    pickle.dump(frequency,f2)
    f2.close()
    return


get_word_frequency()

