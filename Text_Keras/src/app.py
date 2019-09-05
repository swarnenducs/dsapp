import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask , render_template, request
from src.model.models import Dataclassified,db
from src.service.mainETL import MainETLProcess




app = Flask(__name__)

'''
DB CONFIG 
'''

# app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:example@localhost/smqdML'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:example@localhost/smqdML'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#app_db=SQLAlchemy(app)
db.init_app(app)





app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/app/info')
def process():
    #Creating ETL PROCESS OBJECT
    etl = MainETLProcess()
    etl._processData_()
    return "status:200"








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1099, threaded=True)
