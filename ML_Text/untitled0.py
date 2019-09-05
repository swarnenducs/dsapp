#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 22:05:52 2019

@author: swarnenduchatterjee
"""

from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer(min_df=1,stop_words="english")
xtrain_tf=tf.fit_transform(['aaa','bbb','ccccc'])
data_input=tf.transform(["aaa"])