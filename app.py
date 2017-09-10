from flask import Flask, jsonify, json
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
	r = requests.get('https://backend-challenge-winter-2017.herokuapp.com/customers')
	hard = r.json()
	return jsonify(hard)
