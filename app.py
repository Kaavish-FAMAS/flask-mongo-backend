from flask import Flask, request
from pymongo import MongoClient



app = Flask(__name__)
uri = "mongodb+srv://asadtariq1999:virtyou@testingvirtyou.ner4fbz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client.Authentication
cluster = db.users

@app.route("/")
def home():
    print(client.Authentication.users.find_one({"_id": "123456789"}))
    return "Hello, Flask!"

@app.route("/getuser/", methods=['GET', 'POST'])
def get_user():
    result = request.args.to_dict()
    email = result['email']
    password = result['password']
    user =  cluster.find_one({"email": email, "password": password})
    return user['_id']

@app.route("/adduser/", methods=['GET', 'POST'])
def add_user():
    user = request.args.to_dict()
    cluster.insert_one(user)
    return "User Added"

if __name__ == "__main__":
    app.run(port=5000)
