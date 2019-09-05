"""
Created on Sat Jul 20 18:36:29 2019

@author: swarnenduchatterjee

@Datasource :  EU/OFAC
"""


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import linear_kernel
from fuzzywuzzy import fuzz
from sklearn.metrics.pairwise import pairwise_distances
from freediscovery.metrics import (cosine2jaccard_similarity,
                                       jaccard2cosine_similarity)
from sklearn import svm
from fuzzywuzzy import process
#import matplotlib.pyplot as plt
#reading the csv file ..
import os
import pickle
ths=80
tf = TfidfVectorizer(min_df=1, stop_words="english")
model_filename = 'sanction.pickle'
tf_filename='x_tf.pickle'
dataframe_fileName="dataFrame.pickle"


def get_data(df, _input_):
    # x=get_ratio(df,_input_)

    return df[df.apply(lambda row: fuzz.token_sort_ratio(row['wholeName'], _input_), axis=1) > ths]


def maching_process(entry):
    count=0
    data_list=[]
    dict={}

    data_frame=load_dataFrame(dataframe_fileName)
    #print("ENTRY 100 =   ", data_frame["wholeName"][100])
    for index, row in data_frame.iterrows():
        # print("---",row["wholeName"],row['lbl'])

        loc={}
        data=row["wholeName"]
        if data=="_NAME_" or data=="name":
            continue

        else:
            Ratio = fuzz.ratio(entry.lower(), data.lower())
            if Ratio > ths:
                #print("ENTRY =   ", data, str(Ratio))
                loc["wholeName"] = data
                loc["Fuzzy_Ratio"] = Ratio
                loc["Type"] = row["lbl"]
                loc["ref_id"] = row["lega_id"]
                data_list.append(loc)
    return data_list



















def load_dataFrame(fileName):
    path = os.path.abspath("mldic/model/")
    path = path + "/" + fileName
    return pd.read_pickle(path)





def process_filepath(fileName):
    path = os.path.abspath("mldic/model/")
    path = path + "/" + fileName
    infile = open(path, 'rb')
    return infile



def loadpickle(fileName):

    data = pickle.load(process_filepath(fileName))
    return data



def load_model():
    nbm = MultinomialNB()

    # pickle.dump("./model/"nbm, open(filename, 'wb'))

    # path = os.path.abspath("./model/")
    # path = path + "/" + tf_filename
    # infile = open(path, 'rb')
    nbm=loadpickle(model_filename)
    x_tf=tf.fit_transform(loadpickle(tf_filename))

    data_frame = load_dataFrame(dataframe_fileName)





    return  nbm,x_tf,data_frame


def process_input_data(entry):

    data_input = tf.transform([entry])
    return data_input



def perform_match(model,processInput):
    pred = model.predict(processInput)
    return pred





def predict_match(entry):
    return_db = {}
    cosine_data = []
    cosine_f_data = []

    model,xtrain_tf,dataframe=load_model()
    print("MODEL --->  ",model)
    processinput=process_input_data(entry)
    lable=perform_match(model,processinput)
    pred=lable

    # pd=pairwise_distances(xtrain_tf,processinput, metric='cosine')
    #pd = pairwise_distances(xtrain_tf.astype('bool'), processinput.astype('bool'), metric='jaccard')
    S_cos = 1 - pairwise_distances(xtrain_tf, processinput, metric='cosine')
    S_jac = cosine2jaccard_similarity(S_cos)
#    S_jac_ref = 1 - pairwise_distances(xtrain_tf.astype('bool'), processinput.astype('bool'), metric='jaccard')
    print('********************************** ',S_cos,'   @@@@@@@@@@@  ',S_jac,'  ######### ')#,S_jac_ref   )
    print(lable)
    if lable==1:
        for vector in xtrain_tf:
            # print( tf.rev)
           # print("VECTOR VALUE ------ ",vector)
            cosine = linear_kernel(vector, processinput)
           # print("COSINE VALUE ------ ", cosine)
            # print ("----^^ ----",cosine[0][0])
            if cosine[0] >= ths / 100 and cosine[0][0] >= ths / 100 and pred == 1:
                # print ("----COSINE ----",cosine)
                cosine_data.append(cosine)
                #print("---COUNT--")
               #count = count + 1
            else:
                if pred == 1 or pred == 2:
                    if not cosine_f_data:
                        cosine_f_data = cosine
                else:
                    if cosine_f_data < cosine:
                        cosine_f_data = cosine

        print("COSINE F",cosine_f_data)
        if len(cosine_data) > 0:
            print("------ I")
            if pred == 1:
                return_db["ENTRY"] = entry
                return_db["Predict_Type"] = "EU/OFAC"
                return_db["Cosine"] = round(float(cosine_data[0][0][0]) * 100)
                return_db["flag"] = "RED"
                return_db["data"] = maching_process(entry)
                print(return_db)
                return return_db

            # if pred == 2:
            #     return_db["ENTRY"] = entry
            #     return_db["Predict_Type"] = "OFAC"
            #     return_db["Cosine"] = round(float(cosine_data[0][0][0]) * 100)
            #     return_db["flag"] = "RED"
        else:
            print("------ II")
            if len(cosine_f_data) > 0:
                return_db["ENTRY"] = entry
                return_db["Predict_Type"] = "May be A SANCTION ENTRY"
                return_db["Cosine"] = round(float(cosine_f_data[0]) * 100)
                return_db["flag"] = "Orrange"
                return_db["data"] = maching_process(entry)
                return return_db

            else:
                print("------ III")
                return_db["ENTRY"] = entry
                return_db["Predict_Type"] = "NOT A SANCTION ENTRY"
                return_db["Cosine"] = round(float(0.0) * 100)
                return_db["flag"] = "Green"
                return return_db


    else:
        return_db["ENTRY"] = entry
        return_db["Predict_Type"] = "NOT A SANCTION ENTRY"
        return_db["Cosine"] = round(float(0.0) * 100)
        return_db["flag"] = "Green"

        print("RESULT ---> \n ", return_db)
        return return_db




















# if __name__ == '__main__':
#     predict_match("Saddam Hussein Al-Tikriti")
#     #maching_process("Saddam Hussein Al-Tikriti")

