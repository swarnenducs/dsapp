'''
@Author : Swarnendu Chatterjee

Process Description :
ETL PROCESS IN TERMS OF  PROCESSING DATA CREATING CLEAN DATA SET
FOR CLASIFICATION USING DEEP NURAL NETWORAK BASE ON KERAS

'''
import glob
import os
import pandas as pd
from src.service.processETL import ProcessData

class MainETLProcess:


    def _processData_(self):
        #file_list = [f for f in os.listdir('./src/Source') if os.path.isfile(os.path.join('./src/Source',f))]
        path = "./src/Source"
        allFiles = glob.glob(os.path.join(path, "*.csv"))

        print("FILES --- ", allFiles)
        dfs =[]
        for file in allFiles:
            dfs.append(pd.read_csv(file))

        big_frame = pd.concat(dfs, ignore_index=True)
        #print(" HEAD --- ",big_frame.head())
        process = ProcessData()

        process._processDataForBusiness(big_frame)
        # df = pd.read_csv('')
        return ""



