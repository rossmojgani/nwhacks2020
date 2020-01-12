#!/usr/bin/env python3

"""
Flask API which serves the frontend of the application
and has different functionalities based on different
requests

"""

from flask import Flask
from flask import request
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'rapidserve-db'
app.config["MONGO_URI"] = "mongodb://localhost:27017/rapidserve-db"
mongo = PyMongo(app)

"""
Basic route used as a health check to see
if API is working or not
"""
@app.route("/")
def hello():
    return "Hello, World!"


"""
GET request route to return true if user
exists in mongoDB and is active and false
otherwise

"""
@app.route("/users/api/v1.0/exists/<userid>", methods=['GET'])
def check_user(userid):
    # TODO: query mongodb to see if userid exists and is active
    return "User ID {}".format(userid)


"""
GET request route to return user object from
database based on userid argument

"""
@app.route("/users/api/v1.0/<userid>", methods=['GET'])
def get_user(userid):
    # TODO: query mongodb for user object
    return "User ID Object {}".format(userid)


"""
POST request which stores user into database
with correct fields

"""
@app.route("/users/api/v1.0/register", methods=['POST'])
def register_user():
    users_collection = mongo.db.users
    user_id = request.json['user_id']
    full_name = request.json['full_name']
    phone = request.json['phone_number']
    credit = request.json['40.30']
    email = request.json['email']
    restaurant_id = request.json['restaurant_id']
    table_id = request.json['table_id']
    role = request.json['role']
    users_collection.insert({'user_id': user_id,
                             'full_name': full_name,
                             'phone_number': phone,
                             'credit': credit,
                             'email': email,
                             'restaurant_id': restaurant_id,
                             'table_id': table_id,
                             'role': role,
                             'users_collection': users_collection})
    return "Storing user! {}".format(request.json())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    #app.run(host="127.0.0.1", port=80)

