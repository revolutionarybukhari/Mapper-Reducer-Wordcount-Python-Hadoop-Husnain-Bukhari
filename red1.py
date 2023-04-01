#!/usr/bin/python3
from operator import itemgetter
import sys


b={}
l3=[]
l5=[]
# with open('readme.txt', 'r') as testwritefile:
#     Lines = testwritefile.readlines()
l3=[]
for line in sys.stdin:
    line = line.strip()
    words = line.split(',')
    
    if words[0] not in l3:
    	l3.append(words[0])
    
#for item1 in range(0,len(l3)):
 # print(l3[item1])
 # for item2 in range(item1,len(l3)):
  #  if l3[item1]!=l3[item2]:
   #   l4=(l3[item1]+','+l3[item2])
    #  l5.append(l4)
    #else:
     # continue 
      
      
#f=open('f1.txt','a')
for ele in l3:
	print(l3) #it will output the results that will be stored in a txt file in HDFS
 #   f.write(ele+'\n')

#f.close()
