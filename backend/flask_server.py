#!/usr/bin/env python3

"""
Flask API which serves the frontend of the application
and has different functionalities based on different
requests

"""

import json
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
    print(type(userid))
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    print(my_col.find({'user_id': userid}).count())
    print("GET request for userid: {}".format(userid))
    if my_col.find({'user_id': userid}).count() > 0:
        s = my_col.find_one({"user_id": userid})
        print("Found userid in database, returning json {}".format(s))
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
        print("Did not find userid, returning empty json")
        return ''


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
    print("Registering user")
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    print(request.json)
    req_data = request.get_json()
    full_name = req_data['full_name']
    user_id = req_data['user_id']
    phone = req_data['phone_number']
    credit = req_data['credit']
    email = req_data['email']
    restaurant_id = req_data['restaurant_id']
    table_id = req_data['table_id']
    role = req_data['role']
    return_user = {'user_id': user_id,
                   'full_name': full_name,
                   'phone_number': phone,
                   'credit': credit,
                   'email': email,
                   'restaurant_id': restaurant_id,
                   'table_id': table_id,
                   'role': role}
    my_col.insert_one(return_user)
    print("Registered user: {}".format(return_user))
    return jsonify({'user_id': user_id,
                    'full_name': full_name,
                    'phone_number': phone,
                    'credit': credit,
                    'email': email,
                    'restaurant_id': restaurant_id,
                    'table_id': table_id,
                    'role': role})


"""
PUT request which puts new table id in a user object given
a user id field

"""
@app.route("/users/api/v1.0/<userid>", methods=['PUT'])
def enter_table_id(userid):
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    req_data = request.get_json()
    print(req_data)
    myquery = {"user_id": userid}
    newvalues = {"$set": {"table_id": req_data['table_id']}}
    x = my_col.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    return jsonify({'user_id': userid,
                    'table_id': req_data['table_id']})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
    # app.run(host="127.0.0.1", port=80)

