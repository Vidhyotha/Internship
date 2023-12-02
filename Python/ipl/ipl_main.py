from flask import Flask, request
from flask_restful import Api, Resource
from iplstats_dao import *

app = Flask(__name__)
api = Api(app)

@app.route("/teamselect")
def get_team_labels():
    team = request.args.get('team')
    role = request.args.get('role')
    if team and not role:
        return single_team_stats(team)
    elif team and role:
        return single_role_stats(team,role)
    else:
        return select_team()

@app.route('/teamdetails')
def get_team_details():
    return team_details()

@app.route('/amount')
def get_amount_spent():
    return team_amount_stats()

@app.route('/highestbids')
def get_highest_bids():
    return bidding_stats()

@app.route('/bids')
def gets_bidding_prices():
    return bidding_players()

if __name__ == '__main__':
    app.run(debug=True)
