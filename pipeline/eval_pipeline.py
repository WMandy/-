#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:30:18 2021

@author: admin
"""

import os
from sklearn.metrics import classification_report


gt = []
with open('gt.txt', 'r') as f1:
    data = f1.readlines()
for i in data:
    gt.append(i.split(' ')[1].strip('\n'))


act = []
with open('result.txt', 'r') as f2:
    data2 = f2.readlines()
    
data2 = sorted(data2, key=lambda a: int(a.split(' ')[0].strip('.jpg'))) 

for k in data2:
    with open('sort_result.txt', 'a') as f:
        f.write(k)
        
        
for j in data2:
    act.append(j.split(' ')[1].strip('\n'))

res = classification_report(gt, act)
print(res)
    




