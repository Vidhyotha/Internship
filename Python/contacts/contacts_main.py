from flask import Flask, request, jsonify
from flask_restful import Api
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient, errors
from contacts_dao import *

connection_string = "mongodb+srv://vidhyotha:1sjl12qa43qJfR3x@cluster0.tsc3uwi.mongodb.net/"
client = MongoClient(connection_string)
db = client.get_database("ContactsManager")
collection = db.get_collection("contacts")

app = Flask(__name__)
api = Api(app)

@app.route('/addcontact', methods=['POST'])
def add_contact():
    _json = request.json
    fname = _json['FirstName']
    lname = _json['LastName']
    phone = _json['PhoneNo']
    email = _json['emailID']
    city  = _json['CityName']
    if fname and lname and email and phone and city and request.method == 'POST':
        return (add_contact(fname,lname,phone,email,city))
    else:
        return not_found()
    
@app.route('/')
def all_contacts():
	return(get_contacts())

@app.route('/search')
def search_contact():
    searchterm = request.args.get('term')
    return get_search(searchterm)

@app.route('/contacts/<uid>')
def get_contact(uid):
    return contact(uid)

@app.route('/update/<uid>',methods=['PUT'])
def update_contact(uid):
    _json = request.json
    fname = _json['FirstName']
    lname = _json['LastName']
    phone = _json['PhoneNo']
    email = _json['emailID']
    city  = _json['CityName']

    if fname and lname and email and phone and city and request.method == 'PUT':
        return(put_update(uid,fname,lname,phone,email,city))
    else:
        return not_found()
    
@app.route('/delete/<uid>',methods=['PUT'])
def delete_contact(uid):
    return(del_contact(uid))
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True)
