# -*- coding: utf-8 -*-


"""
Created on Sat Jul 20 18:36:29 2019

@author: swarnenduchatterjee

@Datasource :  EU/OFAC
"""
from itertools import count

import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#import matplotlib.pyplot as plt
#reading the csv file ..
import os
import pickle
input_data="Product containes ALL QREINAWI Huda Naaim"
ths=80



def get_ratio(row,_input_):
    name = row['wholeName']
    return fuzz.token_sort_ratio(name, _input_)

def get_data(df,_input_):
    #x=get_ratio(df,_input_)
    
    return df[df.apply(lambda row: fuzz.token_sort_ratio(row['wholeName'], _input_), axis=1) > ths]
    


'''
Pleace give input .....

'''






return_db={}
cosine_data=[]
cosine_f_data=[]

data_frameI=pd.read_csv('eu_data.csv',sep=',',names=['add','lbl','lega_id','wholeName'],skiprows=[0])
data_frameII=pd.read_csv('ofac_data.csv',sep=',',names=['add','lbl','lega_id','wholeName'],skiprows=[0])
#data_frameII=data_frameII.drop(data_frameII.tail().index,inplace=True)
data_frameII=data_frameII.dropna()
# print(data_frameII.tail())
data_frame=pd.concat([data_frameI,data_frameII.dropna()])
#data_frame=pd.merge(data_frameI,data_frameII)
#CHanging the Status in integer 


filename = 'dataFrame.pickle'
# pickle.dump("./model/"nbm, open(filename, 'wb'))
path= os.path.abspath("mldic/model/")
path=path+"/"+filename
print(path)
with open(path, 'wb') as f:
    pickle.dump(data_frame, f)




data_frame.loc[data_frame['lbl']=='EU','lbl']=1
data_frame.loc[data_frame['lbl']=='OFAC','lbl']=1
data_frame.loc[data_frame['lbl']=='NonEU','lbl']=0
data_frame.loc[data_frame['lbl']=='NONOFAC','lbl']=0
data_frame.loc[data_frame['lega_id']=='XXX','lega_id']=0
data_frame.loc[data_frame['add']=='EU','add']=111
data_frame.loc[data_frame['add']=='OFAC','add']=101



#data_frame.loc[data_frame['id']=='XXX','id']=0
#data_frame.loc[data_frame['status']=='spam','status']=0

df_x=data_frame["wholeName"]
#print("DATA --- ",data_frame["lbl"])
#df_y=data_frame["lbl]
df_y=data_frame['lbl']


#print("df_x",df_x)

#Modeling portion 

tf=TfidfVectorizer(min_df=1,stop_words="english")


x_train,x_test,y_train,y_test =train_test_split(df_x,df_y,test_size=0.2,random_state=42)

xtrain_tf=tf.fit_transform(df_x)
array_x=xtrain_tf.toarray()
y_train_tf=df_y.astype(int)

#y_train_tf=df_y.to_numeric(df_y, errors='coerce')







nbm=MultinomialNB()

nbm.fit(xtrain_tf,y_train_tf)
filename = 'sanction.pickle'
# pickle.dump("./model/"nbm, open(filename, 'wb'))
path= os.path.abspath("mldic/model/")
path=path+"/"+filename
print(path)
with open(path, 'wb') as f:
    pickle.dump(nbm, f)


path= os.path.abspath("mldic/model/")
path=path+"/x_tf.pickle"

'''
xtrain_tf
'''

with open(path, 'wb') as f:
    pickle.dump(df_x, f)


data_input=tf.transform([input_data])
#plt.plot(y_train_tf)
pred=nbm.predict(data_input)
print("____****__PREDICTION_****______ ---> ",pred)
#cosine_similarities = linear_kernel(xtrain_tf[0:1], data_input)
#print("----",cosine_similarities)
#lst=list(xtrain_tf.toarray())
#print("LIST ----- ",lst)
feature_names = tf.get_feature_names()
#print("---> ",feature_names)
count=0

for vector in xtrain_tf:
   #print( tf.rev)
    cosine = linear_kernel(vector, data_input)
    #print ("----^^ ----",cosine[0][0])
    if cosine[0]>ths/100  and cosine[0][0]>ths/100 and pred==1 :
         #print ("----COSINE ----",cosine)
         cosine_data.append(cosine)
         print("---COUNT--")
         count=count+1
    else:
         if pred==1 or pred==2 :
             if not cosine_f_data:
               cosine_f_data=cosine
         else:
             if cosine_f_data < cosine:
                 cosine_f_data=cosine
         
#print("COSINE F",cosine_f_data)         
if len(cosine_data)> 0 :
    if pred == 1:
        return_db["ENTRY"]=input_data
        return_db["Predict_Type"]="EU/OFAC"
        return_db["Cosine"]=round(float(cosine_data[0][0][0])*100)
        return_db["flag"]="RED"
        return_db["data"]=get_data(data_frame,input_data)[['lega_id','wholeName']]
        
   
    if pred == 2:
         return_db["ENTRY"]=input_data
         return_db["Predict_Type"]="OFAC"
         return_db["Cosine"]=round(float(cosine_data[0][0][0])*100)
         return_db["flag"]="RED"
    
    
   
    
else:
    if len(cosine_f_data) >0 :
        return_db["ENTRY"]=input_data
        return_db["Predict_Type"]="May be A SANCTION ENTRY"
        return_db["Cosine"]=round(float(cosine_f_data[0])*100)
        return_db["flag"]="Orrange"
        return_db["data"]=get_data(data_frame,input_data)[['lega_id','wholeName']]
    else:
        return_db["ENTRY"]=input_data
        return_db["Predict_Type"]="NOT A SANCTION ENTRY"
        return_db["Cosine"]=round(float(0.0)*100)
        return_db["flag"]="Green"
    
print("RESULT ---> \n ",return_db)    
            
   
   
        