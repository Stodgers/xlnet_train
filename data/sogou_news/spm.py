#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 11:20
# @Author  : Stodgers
# @Site    : 
# @File    : spm.py
# @Software: PyCharm
import sentencepiece as spm
spm.SentencePieceTrainer.train('--input=T-news_sohusite_xml.smarty.txt --model_prefix=m_v3 --vocab_size=3000 --character_coverage=0.99995 --model_type=unigram --control_symbols=<cls>,<sep>,<pad>,<mask><eod> --user_defined_symbols=<eop>,.,(,),",-,–,£,€ --shuffle_input_sentence --input_sentence_size=10000000')

sp = spm.SentencePieceProcessor()
sp.load('m_v3.model')

# encode: text => id
print(sp.encode_as_pieces('你在家吗我要去你家吃饭'))
print(sp.encode_as_ids('你在家吗我要去你家吃饭'))
sp.load('m_v3.model')
mm = sp.EncodeAsIds('你在家吗我要去你家吃饭')
print(mm)
print(sp.decode_ids([41, 190, 20, 146, 1254, 134, 108, 151, 190, 146, 407, 1287]))
for i in range(1000):
    print(sp.decode_ids([i]))