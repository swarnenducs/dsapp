#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 18:36:29 2019

@author: swarnenduchatterjee

@Datasource :  https://archive.ics.uci.edu/ml/machine-learning-databases/
"""

import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB


#reading the csv file ..

data_frame=pd.read_csv('SMSSpamCollection',sep='\t',names=['status','message'])


#CHanging the Status in integer 

data_frame.loc[data_frame['status']=='ham','status']=1
data_frame.loc[data_frame['status']=='spam','status']=0

df_x=data_frame["message"]
df_y=data_frame["status"]




#Modeling portion 

tf=TfidfVectorizer(min_df=1,stop_words="english")


x_train,x_test,y_train,y_test =train_test_split(df_x,df_y,test_size=0.2,random_state=42)

xtrain_tf=tf.fit_transform(x_train)
array_x=xtrain_tf.toarray()
y_train_tf=y_train.astype('int')

nbm=MultinomialNB()

nbm.fit(xtrain_tf,y_train_tf)

data_input=tf.transform(["So there's a ring that comes with the guys costumes. It's there so they can gift their future yowifes. Hint hint"])

pred=nbm.predict(data_input)
print("PREDICT",pred)