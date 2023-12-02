from pymongo import MongoClient,errors
from flask import jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import pprint

connection_string = "mongodb+srv://vidhyotha:1sjl12qa43qJfR3x@cluster0.tsc3uwi.mongodb.net/"
client = MongoClient(connection_string)
db = client.get_database("ContactsManager")
collection = db.get_collection("contacts")

def add_contact(fname,lname,phone,email,city):
    try:
        result = collection.insert_one({ 'FirstName':fname,'LastName': lname,'PhoneNo': phone, "emailID": email, 'CityName': city, 'Deleted': 0})
        resp = jsonify('Contact Added Successfully!')
        resp.status_code = 200
        return resp
        
    except errors.OperationFailure as e:
        resp = jsonify('Error: Duplicate number')
        resp.status_code = 401
        return resp
    
def contact(uid):
    contact = collection.aggregate([{'$match':{'_id':ObjectId(uid)}},{'$project':{'_id':0,'Deleted':0}}])
    return dumps(contact)

def get_contacts():
    contacts = collection.aggregate([{'$match':{'Deleted':0}},{'$project':{'_id':0,'Deleted':0}}])
    resp = dumps(contacts)
    return resp

def get_search(searchterm):
    contact = collection.aggregate([{'$match':{'$or':[{'FirstName':searchterm,'Deleted':0},{'LastName':searchterm,'Deleted':0},{'PhoneNo':searchterm,'Deleted':0},{'City':searchterm,'Deleted':0}]}},{'$project':{'_id':0,'Deleted':0}}])
    return dumps(contact)

def put_update(uid,fname,lname,phone,email,city):
    try:
            result = collection.update_one({'_id': ObjectId(uid)},{'$set':{'FirstName':fname,'LastName': lname,'PhoneNo': phone, "emailID": email, 'CityName': city}})
            resp = jsonify('Contact Edited Successfully!')
            resp.status_code = 200
            return resp
    except errors.OperationFailure as e:
            resp = jsonify('Error: Duplicate number or Contact doesnt exist')
            resp.status_code = 401
            return resp
    
def del_contact(uid):
    try:
        result= collection.update_one({'_id': ObjectId(uid)},{'$set':{'Deleted':1}})
        resp = jsonify('Contact Deleted Successfully!')
        resp.status_code = 200
        return resp
    except errors.OperationFailure as e:
        resp = jsonify('Error: contact doesnt exist')
        resp.status_code = 404
        return resp
    