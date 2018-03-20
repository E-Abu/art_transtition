import pickle

from nlp.clear_db_text import write_general_text_article
from nlp.clear_db_text import write_general_text_artwork_info

from nlp.clear_wiki_text import get_file_derectory
from nlp.clear_wiki_text import write_general_text



artwork_info = '../data/artworkstxt.csv'
news_info = '../data/newstxt.csv'
wechat_info = '../data/wechattxt.csv'

wikitxt_path = '/Users/eva/Downloads/wikipedia-extractor/extracted'

general_file = '/Users/eva/Downloads/wikipedia-extractor/extracted/general.txt'
dbtext_file = '/Users/eva/Downloads/wikipedia-extractor/extracted/db.txt'


### db vocabulary 的写入
write_general_text_artwork_info(artwork_info,dbtext_file)
write_general_text_article(news_info,dbtext_file)
write_general_text_article(wechat_info,dbtext_file)



### genaral vocabulary 的写入
write_general_text_artwork_info(artwork_info,general_file)

write_general_text_article(news_info,general_file)
write_general_text_article(wechat_info,general_file)

derectory_wikitex = get_file_derectory(wikitxt_path,general_file)
write_general_text(derectory_wikitex,general_file)

print('finish write files')







import fasttext

train_source = general_file

# Skipgram model
model = fasttext.skipgram(train_source, './statics/model', dim=300)
print(model.words) # list of words in dictionary

print('finish fasttext train')




from nlp.vocabulary_frequence import get_word_frequency

frequency_pickle_addr = './statics/frequency'
get_word_frequency(dbtext_file,frequency_pickle_addr)


print('finish frequence pickle')





