
import email
from flask import Flask, render_template,request,redirect,url_for   
from bson import ObjectId    
import os
import pymongo
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.registration     
todos = db.registration_details


db= MongoEngine()
db.init_app(app)

def redirect_url():
    return request.args.get('next') or \
    request.referrer or \
    url_for('index')

@app.route("/list")    
def lists ():    
    #Display the all Tasks    
    todos_l = todos.find()    
    a1="active"    
    return render_template('admin.html',a1=a1,todos=todos_l,)  

@app.route("/")    
@app.route("/uncompleted")    
def tasks ():    
    #Display the Uncompleted Tasks    
    todos_l = todos.find({"done":"no"})    
    a2="active"    
    return render_template('index.html',a2=a2,todos=todos_l)

@app.route("/action", methods=['POST'])    
def action ():    
    name=request.values.get("name") 
    email=request.values.get("email")  
    contact=request.values.get("contact")  
    age=request.values.get("age")  
    gender=request.values.get("gender")  
    Qualification=request.values.get("Qualification")  
    internship=request.values.get("internship")  
    certificate=request.values.get("certificate")  
    resume=request.values.get("resume")     
        
    todos.insert_one({ "name": name,"email" : email,"contact": contact,"age" : age,"gender": gender, "Qualification" : Qualification, "internship": internship, "certificate" : certificate,"resume" : resume})    
    return redirect("/list") 



@app.route('/signup/')
def signup():
   return render_template('signup.html')

@app.route('/signup2/')
def signup2():
   return render_template('signup2.html')

@app.route('/admin/')
def admin():
   return render_template('admin.html')

@app.route('/checkregister/')
def checkregister():
   return render_template('checkregister.html')

@app.route('/main/')
def mainpage():
   return render_template('index.html')

@app.route("/getvalues", methods=['POST'])
def getvalues():
    y = todos.find()

@app.route('/fetch')
def query_records():
    return  render_template('/register1.html')



if __name__ == "__main__":    
     app.run(debug=True) 