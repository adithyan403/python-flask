from flask import Flask,render_template,request
app=Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')



@app.route('/')
def hello():
    try:
        client.admin.command("ping")
        print("successfull")
    except:
        print("unseccessful")
    return render_template("html.html")

@app.route('/login')
def login():
    return render_template("login page.html")

@app.route('/loginaction',methods=['POST'])
def logindata():
    username=request.form.get('username')
    password=request.form.get('password')
    db = client['mydb']  # Access the 'mydatabase' database
    collection = db['mycollection']
    collection.insert_one({username:username,password:password})
    return render_template("html.html")