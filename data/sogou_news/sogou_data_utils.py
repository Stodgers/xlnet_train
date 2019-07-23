#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 9:26
# @Author  : Stodgers
# @Site    : 
# @File    : sogou_data_utils.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import jieba
#ss = open('news_sohusite_xml.smarty.dat',encoding='utf-8')
with open('smarty-t233.txt','a', encoding='utf-8') as f: # 'a'表示append,即在原来文件内容后继续写数据（不清楚原有数据）
    data = open('news_sohusite_xml.smarty.dat', errors='ignore', encoding='gb18030')
    k = 1
    str = ''
    kline= ''
    lst = []
    flag = 0
    for i in data.readlines():
        if k % 6 == 4:
            str += i[14:-16]
            str = str.replace("　", "")
            str = str.replace("", "")
        elif k % 6 == 5:
            str += '。' + i[9:-11]
            str = str.replace("　", "")
            str = str.replace("", "")
            if len(str)<=30:
                k+=1
                continue
            f.write(kline + str)
            if flag==0:
                flag=1
                kline = '\n\n'
        else:
            #lst.append(str)
            str = ''
        k += 1
