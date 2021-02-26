#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:19:53 2021

@author: admin
"""

import os

p = '0'
files = os.listdir(p)
print(files)

count = 167
for file in files:
    os.rename(os.path.join(p, file), os.path.join(p, str(count) + '.jpg'))
    with open('gt.txt', 'a') as f:
        f.write(str(count) + '.jpg' + ' ' + '0' + '\n')
    count += 1