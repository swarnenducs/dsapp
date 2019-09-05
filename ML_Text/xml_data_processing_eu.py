"""
Created on Sat Jul 20 18:36:29 2019

@author: swarnenduchatterjee

@Datasource :  https://archive.ics.uci.edu/ml/machine-learning-databases/
"""
# -*- coding: utf-8 -*-



import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np 

def parseXML(xmlfile): 
    data_wh=[]
    data_id=[]
    data_lbl=[]
    data_add=[]
    #df=pd.DataFrame()
    tree = ET.parse(xmlfile) 
    root = tree.getroot()
    print(root)
    
    for item in tree.findall('./'): 
        print("-----")
        print(item)
        for child in item:
           # print('---->',child)
            if child.tag == '{http://eu.europa.ec/fpi/fsd/export}nameAlias': 
                 print('@$---->',child.attrib['wholeName'])
                 data_wh.append(child.attrib['wholeName'])
                 data_id.append(child.attrib['logicalId'])
                 data_lbl.append("EU")
                 data_add.append("EU")
            '''
             else:
                  data_wh.append('name')
                  data_lbl.append("NonEU")
                  data_id.append('XXX')
                  data_add.append("EU")
            '''

                 
                 #data[child.attrib['logicalId']]=child.attrib['wholeName']
                 #df['wholeName']=child.attrib['wholeName']
    print(data_wh)
                 
    df=pd.DataFrame({'lega_id':data_id,'wholeName':data_wh,'lbl':data_lbl,'add':data_add})
    print(df)  
    df.to_csv('eu_data_19.csv',index=False)
           


def process_SDNcsv(csv_file):
    data_name=[]
    data_id_=[]
    data_lbl_=[]
    data_add_=[]
    data_frameII=pd.read_csv(csv_file,sep=',')
   # print('ZZZZ   ----- >',data_frameII)
    for data in data_frameII.values :
         if data[1] == 'NaN' :
             data_name.append("_NAME_")
             data_id_.append('XXX')
             data_lbl_.append("NONOFAC")
             data_add_.append("OFAC")
         else:
             print('ZZZZ   ----- >',data[1])
             strt=str(data[1]).replace(',', '')
             data_name.append(strt)
             data_id_.append(data[0])
             data_lbl_.append("OFAC")
             data_add_.append("OFAC")
             data_name.append("_NAME_")
             data_id_.append('XXX')
             data_lbl_.append("NONOFAC")
             data_add_.append("OFAC")
    
    dff=pd.DataFrame({'lega_id':data_id_,'wholeName':data_name,'lbl':data_lbl_,'add':data_add_}) 
    dff.to_csv('ofac_data.csv',index=False)    
         

           
    
    
    

#process_SDNcsv('cons_prim.csv')
parseXML('eu.xml')    