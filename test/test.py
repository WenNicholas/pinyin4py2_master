# -*- coding: utf-8 -*-
import codecs
from anjuke import pinyin

converter = pinyin.Converter()
converter.load_word_file('words.txt')
print converter.convert('中华有为',fmt='fl', sc=False, pp=True, fuzzy=0)
print converter.convert('中华有为',fmt='df', sc=False, pp=True, fuzzy=0)


f = open('read.txt','r')
f1 = open('writedic.txt','w')

for line in f.readlines():
    content = line.strip() # 把末尾的'\n'删掉
    result = converter.convert('%s'%content,fmt='fl', sc=False, pp=True, fuzzy=0)
    # result = converter.convert('%s'%content,fmt=[df,fl], sc=False, pp=True)
    f1.write(result+'\n')
    # print result



#fmt=[tn,fl], sc=False, pp=True