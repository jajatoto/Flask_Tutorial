from app import app
from flask impoart jsonify, request

@app.route('/')
def index():
	return "hello world!"

@app.route('/data')
def data():
	data = {"names":["John","Jacob","Julie","Jennifer"]}
	return jsonify(data)
