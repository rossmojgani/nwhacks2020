#!/usr/bin/env python3

"""
Flask API which serves the frontend of the application
and has different functionalities based on different
requests

"""

from flask import Flask

app = Flask(__name__)


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
@app.route("/users/api/v1.0/register/<info>", methods=['POST'])
def register_user(info):
    return "Storing users! {}".format(info)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=80)
    app.run(host="127.0.0.1", port=80)

