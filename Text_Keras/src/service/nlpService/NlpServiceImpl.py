# coding: utf-8
'''
@Date Of Creation: 
--------------------------------
@Author : Swarnendu Chatterjee
--------------------------------
@Description About File  :


--------------------------------

'''


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import re

class NlpServiceImpl:

    def __int__(self):
        pass

    def processKeyWOrd(self,sentence):
        # dataFrame=pd.DataFrame(dataFrame)
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(sentence)
        #filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for word in word_tokens:
            if word not in stop_words:
                filtered_sentence.append(word)

        print("AFTER NLP PROCESS KEY WORD EXTRACTION ---- ",self.margeString(filtered_sentence))
        return  self.margeString(filtered_sentence)


    def margeString(self,sent):
        sentence=''
        for s in sent:
            sentence=sentence+ ' '+ s
        sentence=re.sub('[^A-Za-z0-9]+', '|', sentence)
        return sentence


