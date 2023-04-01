#!/usr/bin/python3
from operator import itemgetter
import sys
import collections
import functools
import operator

input1={}
author=[]
for line in sys.stdin:
    line = line.strip()
    a,b = line.split(',')
    #The code below is counting the occurances of authors from all the chunks
    if a not in author:
        author.append(a)
        input1[a]=b
    else:
        c=input1[a]
        res=int(c)+int(b)
        input1[a]=str(res)

    
    
for i,j in input1.items(): #This prints the result which is them stored in a txt file in HDFS
	if int(j) >=200:
	    print(i,j)

