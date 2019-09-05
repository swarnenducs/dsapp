#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 13:21:25 2019

@author: swarnenduchatterjee
"""

import re
import pandas as pd
import numpy as np
file=open (r'Document-2.txt')
lines_list=file.readlines()
clean_lines_list=[]
for line in lines_list:
    clean_line=line.replace('\n','')
    clean_lines_list.append(clean_line)
for line in clean_lines_list:
    if line==' ':
        del clean_lines_list[clean_lines_list.index(line)]

#print(clean_lines_list)
#Splitting the data which is left side of ' : '
Bill=[]
subheading=[]
Des=[]
for line in clean_lines_list:
    if ':' in line:
        string=line
        index=string.index(':')
        Des=string[index+1:]
        subheading=string[:index]
        print(subheading)
#Splitting the data which is right side of     '   :   '
Bill=[]
subheading=[]
Des=[]
for line in clean_lines_list:
    if ':' in line:
        string=line
        index=string.index(':')
        Des=string[index+1:]
        subheading=string[:index]
        print(Des)
Report=[
    {'Documentary Credit Number':'155518020446'},
    {'Date of Issue':'171102'},
    {'Applicable Rules':'UCP LATEST VERSION'},
    {'Currency Code':'36412,27'}
]
df=pd.DataFrame(Report)
df = df.fillna('')
print("OUTPUT---->")
print (df[['Applicable Rules','Documentary Credit Number','Date of Issue','Currency Code']])