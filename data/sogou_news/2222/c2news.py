import pandas as pd
import numpy as np
import random
k=0
h = []
while(k<=10000):
    tt = random.randint(20000, 30001)
    if tt not in h:
        h.append(tt)
        k+=1
path = 'val.txt'
with open(path,errors='ignore',encoding='utf-8') as f:
    k1=0
    for i in f.readlines():
        tt = i.split("	")[0]
        yy = "".join(i.strip().split("	")[1:])
        with open(u"D:\pyProject\\xlnet_train\data\sogou_news\\2222\\unsup\\"+str(h[k1])+'.txt','a',encoding='utf-8') as ft:
            ft.write(yy+'\n')
        k1+=1
