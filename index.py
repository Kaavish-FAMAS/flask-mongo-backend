from flask import Flask, request
from bson import json_util
import pymongo

app = Flask(__name__)
uri = "mongodb+srv://asadtariq1999:virtyou@testingvirtyou.ner4fbz.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

users_db = client.Authentication
users_cluster = users_db.users

relay_db = client.sensors
relay_cluster = relay_db.relay

sensor_db = client.sensors
sensor_cluster = sensor_db.readings

@app.route("/")
def home():
    print(users_cluster.find_one({"_id": "123456789"}))
    return "Yo wasssup?"

# https://flask-mongo-backend-ar230500-famas.vercel.app/getuser?email=asadtariq1999%40gmail.com&password=123456789

@app.route("/getuser/", methods=['GET'])
def get_user():
    print(request.args.to_dict())
    result = request.args.to_dict()
    email = result['email']
    password = result['password']
    user =  users_cluster.find_one({"email": email, "password": password})
    if user:
        return "exists"
    return "does not exist"

@app.route("/adduser/", methods=['GET', 'POST'])
def add_user():
    user = request.args.to_dict()
    users_cluster.insert_one(user)
    return "User Added"

@app.route("/addrelayout/", methods=['GET', 'POST'])
def add_relayout():
    relay = request.args.to_dict()
    relay_cluster.insert_one(relay)
    return "Relay Outputs Configured"

@app.route("/getsensor/", methods=['GET'])
def get_sensor():
    readings = sensor_cluster.find({}).sort('_id', pymongo.DESCENDING)
    return json_util.dumps(readings)

__name__ == "__main__" and app.run()