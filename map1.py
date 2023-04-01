#!/usr/bin/python3
import sys
import pandas as pd

support_threshold=200
set_threshold=support_threshold*(10000/900000)

for line in sys.stdin:
    line = line.strip()
    df = line.split(',')

#for df in pd.read_csv('/user/assignment2/DBLP_DATA'):
    a ={}
    #df.dropna(inplace=True)
    for word in df.author:
    
        if word not in a:
            a[word]=1
        else:
            c=a[word]
            a[word]=c+1
    for k,v in a.items():      
        if float(v) >= set_threshold:
            print(k,",",1)
            
    # for i in list(a.keys()):           
        
    del a

