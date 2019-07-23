#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 11:26
# @Author  : Stodgers
# @Site    : 
# @File    : tesn.py
# @Software: PyCharm
import jieba

txt = '同心县地处宁夏中部干旱带的核心区，　冬寒长，春暖迟，夏热短，秋凉早，干旱少雨，蒸发强烈，风大沙多。'

lt = open('233.txt',errors='ignore', encoding='gb18030')

k = 0
with open('cst.txt','a',encoding='utf-8') as f:

    for i in lt.readlines():
        f.write(i)
        k+=1
        if k==2000:break
