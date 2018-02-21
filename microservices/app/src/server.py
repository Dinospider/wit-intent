from src import app
from flask import jsonify, request, render_template
from wit import Wit

@app.route("/")
def home():
    return "Hasura Hello World"

@app.route('/wit')
def getWit():
	return render_template('form.html')
	
@app.route('/wit' , methods = ['POST'])
def returnWit():
	if request.method == 'POST':
		accesstoken = "FRGHIG2TZ2VGOBJE6OSARPM465EWGBEH"
		query = request.form['comment']
		client = Wit(accesstoken)
		resp = client.message(query)
		return jsonify(resp['entities'])
