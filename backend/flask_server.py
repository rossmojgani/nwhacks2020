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
import pymongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'rapidserve-db'
app.config["MONGO_URI"] = "mongodb://localhost:27017/rapidserve-db"
mongo = PyMongo(app)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

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
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    if my_col.find({'user_id': int(userid)}).count() > 0:
        s = my_col.find({"user_id": userid})
        print(s)
        output = {'user_id': s['user_id'],
                  'full_name': s['full_name'],
                  'phone_number': s['phone_number'],
                  'credit': s['credit'],
                  'email': s['email'],
                  'restaurant_id': s['restaurant_id'],
                  'table_id': s['table_id'],
                  'role': s['role']}
        return jsonify(output)
    else:
        return jsonify({})


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
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    user_id = request.json['user_id']
    full_name = request.json['full_name']
    phone = request.json['phone_number']
    credit = request.json['credit']
    email = request.json['email']
    restaurant_id = request.json['restaurant_id']
    table_id = request.json['table_id']
    role = request.json['role']
    return_user = {'user_id': user_id,
                   'full_name': full_name,
                   'phone_number': phone,
                   'credit': credit,
                   'email': email,
                   'restaurant_id': restaurant_id,
                   'table_id': table_id,
                   'role': role}
    my_col.insert_one(return_user)
    return jsonify(return_user)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    #app.run(host="127.0.0.1", port=80)

