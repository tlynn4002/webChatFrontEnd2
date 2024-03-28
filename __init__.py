from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rin2406m@@localhost/dbwebchat?charset=utf8mb4'
db=SQLAlchemy(app=app)

class students(db.Model):
   id = Column('student_id', Integer, primary_key = True)
   name = Column(String(100))
   city = Column(String(50))  
   addr = Column(String(200))
   pin = Column(String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin


@app.route('/')
def home():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template('home.html',result=result)

if __name__ == '__main__':
   app.run(debug = True)
   db.create_all()

   

