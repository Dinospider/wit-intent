from src import app
from flask import jsonify
from wit import Wit

@app.route("/")
def home():
    return "Hasura Hello World"

@app.route('/wit')
def testWit():
	client = Wit("FRGHIG2TZ2VGOBJE6OSARPM465EWGBEH")
	resp = client.message("How far is tokyo from bangalore?")
	return jsonify(resp['entities'])