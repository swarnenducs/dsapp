# coding: utf-8
'''
@Date Of Creation: 
--------------------------------
@Author : Swarnendu Chatterjee
--------------------------------
@Description About File  :


--------------------------------

'''


import  pandas as pd



'''
[5 rows x 7 columns]
DATA IN DFB  problemID
DATA IN DFB  Link
DATA IN DFB  Title
DATA IN DFB  Contexts
DATA IN DFB  Source
DATA IN DFB  Sentence
DATA IN DFB  MachineClassification
'''



class ProcessData:


    def _processDataForBusiness(self,dataFrame):
        dfB=pd.DataFrame(dataFrame)
        print ("HEAD OF DATA START PROCESSING  ",dfB.head())



        # for data in dfB:
        #      print("DATA IN DFB ",data)
        processData=pd.DataFrame()
        problemid=''
        problemIDList=[]
        Linklist=[]
        ContextsList=[]
        Sentencelist=[]
        TitleList=[]
        SourceList=[]
        MachineClassificationList=[]
        i=0




        for ind in dfB.index:

            print("INDEX VALUE ind :  ",ind)
            if problemid == dfB['problemID'][ind] :
                     problemid = dfB['problemID'][ind]
                     if i==0:
                         Sentencelist.insert(i, dfB['Sentence'][ind - 1])
                         i = i + 1
                     else:
                         print("INDEX  -- i - ", i)
                         print("ENTERING UPDATE  ENTRY ")
                         print("ENTERING UPDATE  ENTRY ",SourceList[0])
                         i=i-1


                         # Sentencelist.append(i - 1, str(Sentencelist[i-1])+str(dfB['Sentence'][ind - 1]))
                         SourceList[i]=str(SourceList[i])+str(dfB['Sentence'][ind - 1])
                         i = i + 1



            else:

                #print("ENTERING NEW ENTRY index : " ,i)
                problemid = dfB['problemID'][ind]
                problemIDList.insert(i, dfB['problemID'][ind])
                ContextsList.insert(i, dfB['Contexts'][ind])
                Sentencelist.insert(i, dfB['Sentence'][ind])
                Linklist.insert(i, dfB['Link'][ind])
                MachineClassificationList.insert(i, dfB['MachineClassification'][ind])
                TitleList.insert(i, dfB['Title'][ind])
                SourceList.insert(i, dfB['Source'][ind])
                i = i + 1





        print("SENTENCE  ----",Sentencelist)
        dataDict={
            'problemID':problemIDList,
            'Link':Linklist,
            'Title':TitleList,
            'Contexts':ContextsList,
            'Source':SourceList,
            'Sentence':Sentencelist,
            'MachineClassification':MachineClassificationList
        }

        processData= pd.DataFrame.from_dict(dataDict)
        processData.to_csv('file1.csv',index=False)


        return None















