from flask import Flask, render_template,redirect, url_for, request, session
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="dz67"
)
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/rasporedCasova')
def rasporedCasova():
	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	raspored = mc.fetchall()
	predavac = []
	for element in raspored:
		if element[3] not in predavac:
			predavac.append(element[3])
	ucionice = []
	for element in raspored:
		if element[7] not in ucionice:
			ucionice.append(element[7])
	return render_template("rasporedCasova.html",raspored = raspored, predavac = predavac, ucionice = ucionice)

if __name__ == '__main__':
	app.run(debug=True)