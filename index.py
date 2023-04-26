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
    return client.Authentication.users.find_one({"_id": "123456789"})

@app.route("/check")
def check():
    return "Checking Vercel 2"

# https://flask-mongo-backend-ar230500-famas.vercel.app/getuser?email=asadtariq1999%40gmail.com&password=123456789

@app.route("/getuser/", methods=['GET'])
def get_user():
    print(request.args.to_dict())
    result = request.args.to_dict()
    email = result['email']
    password = result['password']
    user =  cluster.find_one({"email": email, "password": password})
    if user:
        return "exists"
    return "does not exist"


@app.route("/adduser/", methods=['GET', 'POST'])
def add_user():
    user = request.args.to_dict()
    cluster.insert_one(user)
    return "User Added"

__name__ == "__main__" and app.run()