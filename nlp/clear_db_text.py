import pandas as pd
import jieba

artwork_info = '../data/artworkstxt.csv'
news_info = '../data/newstxt.csv'
wechat_info = '../data/wechattxt.csv'

general_file = '/Users/eva/Downloads/wikipedia-extractor/extracted/general.txt'



def write_general_text_artwork_info(file_name, file_wt):
    artworks_painting = pd.read_csv(file_name, error_bad_lines=False)
    for i in range(len(artworks_painting)) :
        text_tit = artworks_painting.title[i]
        text_dsc = artworks_painting.description[i]
        if type(text_tit) == str and type(text_dsc) == str:
            text = text_tit + ' ' + text_dsc
            #text = text.replace(' ', '')
            seg_list = jieba.cut(text)
            text_word = ' '.join(seg_list)
            text_word = text_word + ' '
            with open(file_wt,'a',encoding='utf-8') as f2:
                f2.write(text_word)
    return

write_general_text_artwork_info(artwork_info,general_file)


def write_general_text_article(file_name,file_wt):
    artical = pd.read_csv(file_name, error_bad_lines=False)
    for i in range(len(artical)):
        text_tit = artical.title[i]
        text_con = artical.content[i]
        if type(text_tit) == str and type(text_con) == str:
            text = text_tit + text_con
            #text = text.replace(' ', '')
            seg_list = jieba.cut(text)
            text_word = ' '.join(seg_list)
            text_word = text_word + ' '
            with open(file_wt,'a',encoding='utf-8') as f2:
                f2.write(text_word)
    return

write_general_text_article(news_info,general_file)
write_general_text_article(wechat_info,general_file)


