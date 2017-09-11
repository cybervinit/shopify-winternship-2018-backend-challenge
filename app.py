from flask import Flask, jsonify, json
import requests
import math

app = Flask(__name__)

API_URL = 'https://backend-challenge-winter-2017.herokuapp.com/customers.json'

@app.route('/')
def hello_world():
	cust_obj = get_api_resp(1)
	pagination = cust_obj['pagination']
	get_page_amount(pagination)
	
	response_data = {}
	invalid_customer_list = get_invalid_cust_list(cust_obj)
	for i in range (1, page_amount):
		page_number = i+1
		invalid_customer_list.extend(get_invalid_cust_list(cust_obj))
		return jsonify(cust_obj)
		
	return str(page_amount)

def get_api_resp(page_number):
	page_query = '?page=%s' % page_number
	endpoint = API_URL + page_query
	response = requests.get(endpoint)
	return response.json()


def get_page_amount(pagination):
	amount = pagination['total'] / float(pagination['per_page'])
	return int(math.ceil(amount))



def get_invalid_cust_list(cust_obj):
	return []


@app.route('/full')
def full():
	return jsonify(get_api_resp(1))