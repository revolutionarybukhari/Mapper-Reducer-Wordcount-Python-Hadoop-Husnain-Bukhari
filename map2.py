#!/usr/bin/python3
with open("f1.txt", 'r') as f:
    unique_authors = [line.rstrip(' \n') for line in f]
import pandas as pd

a={}
for line in sys.stdin:
    line = line.strip()
    author = line.split()

    if author not in unique_authors:
        continue
    else:
        if author not in a:
            a[author]=1
        else:
            c=a[author]
            a[author]=c+1

    for i,j in a.items(): 
        if j>=1:
            print(i,',',j)
del a
    
