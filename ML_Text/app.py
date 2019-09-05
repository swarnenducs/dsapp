# -*- coding: utf-8 -*-

"""
Created on Sun Jul 21 10:03:49 2019

@author: swarnenduchatterjee

@Datasource :  EU/OFAC
"""

"""
Importing support Liberies

"""

import warnings
import flask
import nltk
from elasticsearch import Elasticsearch
from flask import Flask , render_template, request
from werkzeug import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask import request
from fuzzywuzzy import fuzz
import os
from mldic.complianceML import predict_match
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from  Model import PortList
from flask_sqlalchemy import SQLAlchemy
UPLOAD_FOLDER = './store'
ALLOWED_EXTENSIONS = set('*.csv')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:example@localhost/gtx_cc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app_db=SQLAlchemy(app)

#app.config.from_object('config')







@app.route("/test", methods=['GET'])
def test_db():
    prot=PortList.query.all()
    print("XXX--- ",prot)





@app.route("/upload", methods=['GET'])
def _upload_file():
    return render_template('upload.html')



@app.route('/_process_model', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #f.save(secure_filename("/uplod/"+f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return 'file uploaded successfully'




@app.route("/validateEntity", methods=['POST'])
#@measure_processing_time
def _validate_Entity_for_sanction_data_():
    if  request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            print("RESPONSE >>>> ", request.get_json())
            entry = request.get_json()['attrval']

            process=predict_match(entry)
            print("PROCESS",process)

            return flask.jsonify({"result": process})







@app.route("/validate_VESS",methods=['POST'])
def _validate_VESS_DATA():
    return ""








@app.route("/", methods=['POST'])
def mainWeb():
    return flask.jsonify({"status":"200"})









"""
main method to run the flask app over 1097 port 
"""


if __name__ == "__main__":
    # app.run()
    #app.run()
    # http_server = HTTPServer(WSGIContainer(app))
    # http_server.listen(5000)
    # IOLoop.instance().start()
    app.run(host='0.0.0.0', port=5000 ,threaded=True)
    # app.run(host='localhost', port=802)
    #http://localhost:9200/_cat/indices?v




