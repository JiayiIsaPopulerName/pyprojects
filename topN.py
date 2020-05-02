# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
data = [10,20,30,40,50,60,70,80,90]
n = 5
topn = data[:n]
print(data)
print(topn)
topn.sort(reverse = True)
print(topn)
for i in range (n,len(data)):
    if topn[n-1] < data[i]:
        topn[n-1]= data[i]
        topn.sort(reverse = True)
print(topn)