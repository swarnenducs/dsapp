# coding: utf-8
'''
@Date Of Creation: 05-09-19
--------------------------------
@Author : Swarnendu Chatterjee
--------------------------------
@Description About File  :
Application for DataAccess processing any DB realated Oparation
--------------------------------

'''

from src.model.models import Dataclassified,db


class Dataclassified_dao():


    def _inser_(self,dataModel):
        try:
            # Dataclassified dataModel = dataModel
            db.session.add(dataModel)
            db.session.flush()
            db.session.refresh(dataModel)

           # print("ID ----", id)
            db.session.commit()
        except:
            pass








