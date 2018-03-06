from os import listdir
import jieba
import zhconv


wikitxt_path = '/Users/eva/Downloads/wikipedia-extractor/extracted'
general_file = '/Users/eva/Downloads/wikipedia-extractor/extracted/general.txt'

def get_file_derectory(path):
    file_paths = []
    for folder in listdir(path):
        if folder != '.DS_Store' and folder != 'general.txt':
            path_2nd = path + '/' + folder
            for file_name in listdir(path_2nd):
                path_3rd = path_2nd + '/' + file_name
                file_paths.append(path_3rd)
    return file_paths

derectory_wikitex = get_file_derectory(wikitxt_path)
#print(derectory_wikitex)


def write_general_text(derectory,file_wt):
    for path in derectory:
        with open(path,'r',encoding='utf-8') as f:
            text =  f.read()
            seg_list = jieba.cut(text)


            text_word = ' '.join(seg_list)
            text_word = zhconv.convert(text_word, 'zh-cn')
            text_word = text_word + ' '
            with open(file_wt,'a',encoding='utf-8') as f2:
                f2.write(text_word)
    return

write_general_text(derectory_wikitex,general_file)
# general.text 是经过
# 分词的文件，以' '隔开