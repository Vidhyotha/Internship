from pymongo import MongoClient
import pprint

connection_string = "mongodb+srv://vidhyotha:1sjl12qa43qJfR3x@cluster0.tsc3uwi.mongodb.net/"
client = MongoClient(connection_string)
db = client.get_database("ipl2020")
collection = db.get_collection("teams")

#getting team labels
def select_team():
    cursor = collection.aggregate([{'$project':{'_id':0,'label':1}}])
    return [ doc['label'] for doc in cursor]

#getting stats of a team
def single_team_stats(team):
    cursor = collection.aggregate([{'$unwind':'$players'},{'$match':{'label':team}},{'$project':{'_id':0,'info':{'name':'$players.player','role':'$players.role','label':'$label','price':'$players.price'}}}])
    return [ doc['info'] for doc in cursor ]

#getting stats of a team's role
def single_role_stats(team, role):
    cursor = collection.aggregate([{'$unwind':'$players'},{'$match':{'players.role':role,'label':team}},{'$project':{'_id':0,'info':{'name':'$players.player','team':'$label','role':'$players.role','price':'$players.price'}}}])
    return [ doc['info'] for doc in cursor ]

#getting details of team
def team_details():
    cursor = collection.aggregate([{'$project':{'_id':0,'players':0}}])
    return [ doc for doc in cursor ]

#getting amount spent by all teams
def team_amount_stats():
    cursor = collection.aggregate([{'$unwind':'$players'},{'$group':{'_id':'$label','amount':{'$sum':'$players.price'}}}])
    return [ doc for doc in cursor ]

#getting highest bid players
def bidding_stats():
    cursor = collection.aggregate([{"$unwind":"$players"},{ "$group":{ "_id": "$players.role","maxPrice": { "$max": "$players.price" },"docs": { "$push": {"name": "$players.player","price": "$players.price"}}}},{ "$project": {"maxPrice": 1,"docs": {"$setDifference": [{ "$map": {"input": "$docs","as": "doc","in": {"$cond": [{ "$eq": [ "$maxPrice", "$$doc.price" ] },"$$doc.name",'false']}}},['false']]}}}])
    return [ doc for doc in cursor ]

#getting all players from most paid to least paid
def bidding_players():
    cursor = collection.aggregate([{'$unwind':'$players'},{'$sort':{'players.price':-1}},{'$project':{'_id':0,'info':{'name':'$players.player','role':'$players.role','label':'$label','price':'$players.price'}}}])
    return [ doc['info'] for doc in cursor ]                                  

pprint.pprint(bidding_stats())