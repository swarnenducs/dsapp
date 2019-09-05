# coding: utf-8

'''
@Date Of Creation: 01-09-19
--------------------------------
@Author : Swarnendu Chatterjee
--------------------------------
@Description About File  :
Application for creating ORM model class defination
--------------------------------

'''
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, Index, Integer, Numeric, String, Table, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

'''
pip install flask-sqlacodegen
flask-sqlacodegen --flask --outfile models.py mysql+pymysql://root:example@localhost:3306/smqdML
'''





db = SQLAlchemy()


class Dataclassified(db.Model):
    __tablename__ = 'dataclassified'

    ProblemID = db.Column(db.BigInteger, primary_key=True)
    Link = db.Column(db.Text)
    Title = db.Column(db.Text)
    Contexts = db.Column(db.Text)
    Source = db.Column(db.Text)
    Sentence = db.Column(db.Text)
    MachineClassification = db.Column(db.Text)
