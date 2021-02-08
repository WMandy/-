#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:25:51 2021

@author: admin
"""
import csv

with open('gt.txt', 'r') as f1:
    data = f1.readlines()
  
with open('71_92_80.txt', 'r') as f2:
    data2 = f2.readlines()

act = []
for j in data2:
    act.append(j.split(' ')[1].strip('\n'))
   
    
for i in range(len(data)):
    line = data[i].strip('\n') + ' ' + act[i] 
    line = line.split(' ')
    print(line)
    with open('result.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(line)
  