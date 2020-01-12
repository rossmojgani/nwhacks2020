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


"""
POST request which puts a transaction into transaction database
with correct fields

"""
@app.route("/users/api/v1.0/new_transaction", methods=['POST'])
def register_transaction():
    print("Registering transaction")

    mydb = myclient['rapidserve-db']
    my_col = mydb['transaction']

    print(request.json)

    req_data = request.get_json()
    user_id = req_data['user_id']
    amount = req_data['amount']
    restraunt_id = req_data['restraunt_id']
    table_id = req_data['table_id']
    date = req_data['date']
    time = req_data['time']

    return_transaction = {'user_id': user_id,
                          'amount': amount,
                          'restraunt_id': restraunt_id,
                          'table_id': table_id,
                          'date': date,
                          'time': time}

    my_col.insert_one(return_transaction)

    print("Registered transaction: {}".format(return_transaction))

    return jsonify({'user_id': user_id,
                    'amount': amount,
                    'restraunt_id': restraunt_id,
                    'table_id': table_id,
                    'date': date,
                    'time': time})


"""
GET request to get all transactions of a user id

"""
@app.route("/users/api/v1.0/transaction_history/<userid>", methods=['GET'])
def get_transactions(userid):
    print(type(userid))

    mydb = myclient['rapidserve-db']
    my_col = mydb['transactions']

    print(my_col.find({'user_id': userid}))
    print("GET request for transactions userid: {}".format(userid))

    if my_col.find({'user_id': userid}).count() > 0:

        transactions = my_col.find({"user_id": userid})

        return jsonify(transactions)
    else:
        print("No transactions for given userid")
        return ''

"""
PUT request which puts new table id in a user object given
a user id field

"""
@app.route("/users/api/v1.0/waiter/<userid>", methods=['PUT'])
def enter_waiter_fields(userid):
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    req_data = request.get_json()
    print(req_data)
    myquery = {"user_id": userid}
    newvalues = {"$set": {"restaurant_id": req_data['restaurant_id'],
                          "phone_number": req_data['phone_number'],
                          "role": req_data['role']}}
    x = my_col.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    return jsonify({'user_id': userid,
                    'restaurant_id': req_data['restaurant_id'],
                    'phone_number': req_data['phone_number'],
                    'role': req_data['role']})


"""
POST request for an order

"""
@app.route("/users/api/v1.0/new_order", methods=['POST'])
def register_order():
    print("Registering new order...")

    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']

    print(request.json)

    req_data = request.get_json()
    table_id = req_data['table_id']
    waiter_id = req_data['waiter_id']

    order = req_data['order']
    amount = req_data['amount']
    amount_left = req_data['amount_left']

    return_order = {'table_id': table_id,
                    'waiter_id': waiter_id,
                    'order': order,
                    'amount': amount,
                    'amount_left': amount_left}

    my_col.insert_one(return_order)

    print("Registered order: {}".format(return_order))

    return jsonify({'table_id': table_id,
                    'waiter_id': waiter_id,
                    'order': order,
                    'amount': amount,
                    'amount_left': amount_left})


"""
PUT request which puts new order list into a order object

"""
@app.route("/users/api/v1.0/order/<tableid>", methods=['PUT'])
def change_order(tableid):
    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']
    req_data = request.get_json()
    print(req_data)
    myquery = {"table_id": tableid}
    newvalues = {"$set": {"order": req_data['order']}}
    x = my_col.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    return jsonify({'table_id': tableid,
                    'order': req_data['order']})


"""
PUT request which puts new order list into a order object

"""
@app.route("/users/api/v1.0/amount_left/<tableid>", methods=['PUT'])
def change_amount_left(tableid):
    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']
    req_data = request.get_json()
    print(req_data)
    myquery = {"table_id": tableid}
    newvalues = {"$set": {"amount_left": req_data['amount_left']}}
    x = my_col.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    return jsonify({'table_id': tableid,
                    'amount_left': req_data['amount_left']})


"""
GET request for an order id

"""
@app.route("/users/api/v1.0/get_order/<orderid>", methods=['GET'])
def get_order(orderid):
    print(type(orderid))

    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']

    my_order = my_col.find_one({"table_id": orderid})

    print(my_order)
    print("GET request for ordetable_id: {}".format(orderid))

    output = {'table_id': my_order['table_id'],
              'waiter_id': my_order['waiter_id'],
              'order': my_order['order'],
              'amount': my_order['amount'],
              'amount_left': my_order['amount_left']}

    return jsonify(output)


"""
PUT request to change user's credit

"""
@app.route("/users/api/v1.0/credit/<userid>", methods=['PUT'])
def change_user_credit(userid):
    mydb = myclient['rapidserve-db']
    my_col = mydb['users']
    req_data = request.get_json()
    print(req_data)
    myquery = {"user_id": userid}
    newvalues = {"$set": {"credit": req_data['credit']}}
    x = my_col.update_many(myquery, newvalues)
    print(x.modified_count, "documents updated.")
    return jsonify({'user_id': userid,
                    'credit': req_data['credit']})


"""
GET request route to return true if table exits
in mongoDB and is active and false
otherwise

"""
@app.route("/users/api/v1.0/table_exists/<tableid>", methods=['GET'])
def check_table(tableid):
    print(type(tableid))

    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']

    print(my_col.find({'table_id': tableid}).count())
    print("GET request for tableid: {}".format(tableid))

    if my_col.find({'table_id': tableid}).count() > 0:
        s = my_col.find_one({"table_id": tableid})
        print("Found tableid in database, returning json {}".format(s))
        output = {'table_id': s['table_id'],
                  'waiter_id': s['waiter_id'],
                  'order': s['order'],
                  'amount': s['amount'],
                  'amount_left': s['amount_left']}
        return jsonify(output)
    else:
        print("Did not find userid, returning empty json")
        return ''

"""
DELETE request for table_id

"""
@app.route("/users/api/v1.0/delete_table/<tableid>", methods=['DELETE'])
def delete_table(tableid):
    print(type(tableid))

    mydb = myclient['rapidserve-db']
    my_col = mydb['orders']

    myquery = {"table_id": tableid}

    x = my_col.delete_many(myquery)
    print(x.deleted_count, " documents deleted")
    return ('')

if __name__ == '__main__':
    # run the app on port 80
    app.run(host="0.0.0.0", port=80)
    # app.run(host="127.0.0.1", port=80)
