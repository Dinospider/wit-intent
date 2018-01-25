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
		query = request.form['comment']
		client = Wit("FRGHIG2TZ2VGOBJE6OSARPM465EWGBEH")
		resp = client.message(query)
		return jsonify(resp['entities'])
