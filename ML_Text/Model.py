from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:example@localhost/gtx_cc'
# #app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:example@localhost/gtx_cc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app_db=SQLAlchemy(app)






'''

Column	Type	Comment
UID	int(11) Auto Increment	
Name	varchar(70) NULL	
ContainerCode	varchar(10) NULL	
ExtCode	varchar(10) NULL	
NameNoDiacritics	varchar(100) NULL	
DryPort	varchar(10) NULL [N]	
'''

class PortList (app_db.Model):
    __tablename__ = 'PortList'
    UID = app_db.Column(app_db.Integer, primary_key=True)
    Name= app_db.Column(app_db.String(70),nullable=False )
    ContainerCode= app_db.Column(app_db.String(10),nullable=False )
    ExtCode= app_db.Column(app_db.String(10),nullable=False )
    NameNoDiacritics= app_db.Column(app_db.String(100),nullable=False )
    DryPort = app_db.Column(app_db.String(10),nullable=False )

    def __init__(self,UID,Name,ContainerCode,ExtCode,NameNoDiacritics,DryPort):
        self.UID=UID
        self.Name=Name
        self.ContainerCode=ContainerCode
        self.ExtCode=ExtCode
        self.NameNoDiacritics=NameNoDiacritics
        self.DryPort=DryPort






@app.route("/test", methods=['GET'])
def _test_db_():
    prot=PortList.query.all()
    print("XXX--- ",prot)
    list=PortList.query.filter_by(Name='EsnnadXX').first()
    if list is None:
        print("NOT A VALID PORT_____ ")
    else:
        print("VALID POSRT  ____", list.Name)




if __name__ == "__main__":
    # app.run()
    #app.run()
    # http_server = HTTPServer(WSGIContainer(app))
    # http_server.listen(5000)
    # IOLoop.instance().start()
    app.run(host='0.0.0.0', port=5000 ,threaded=True)
    # app.run(host='localhost', port=802)
    #http://localhost:9200/_cat/indices?v




