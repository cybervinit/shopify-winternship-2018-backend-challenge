from flask import Flask, jsonify, json
import requests
import math

app = Flask(__name__)

API_URL = 'https://backend-challenge-winter-2017.herokuapp.com/customers.json'

@app.route('/')
def hello_world():
	cust_obj = get_api_resp(1)
	pagination = cust_obj['pagination']
	page_amount = get_page_amount(pagination)
	
	response_data = {}
	invalid_customer_list = get_invalid_cust_list(cust_obj)
	# TEMP
	return get_invalid_cust_list(cust_obj)

	for i in range (1, page_amount):
		page_number = i+1
		cust_obj = get_api_resp(page_number)
		invalid_customer_list.extend(get_invalid_cust_list(cust_obj))
	
	response_data = {'invalid_customers': invalid_customer_list}
	return str(response_data)

def get_api_resp(page_number):
	page_query = '?page=%s' % page_number
	endpoint = API_URL + page_query
	response = requests.get(endpoint)
	return response.json()


def get_page_amount(pagination):
	amount = pagination['total'] / float(pagination['per_page'])
	return int(math.ceil(amount))



def get_invalid_cust_list(cust_obj):
	validation_arr = cust_obj['validations']
	customer_arr = cust_obj['customers']

	

	invalid_list = []

	for j in range (0, len(customer_arr)):
		# TODO: extract all validations
		current_customer = customer_arr[j]
		issue_list = get_issues(current_customer, validation_arr)
		return issue_list

	return validation_arr[0]

def get_issues(current_customer, validation_arr):
	issue_list = []
	# TODO: validate the whole customer
	for k in range (0, len(validation_arr)):
		key = validation_arr[k].keys()[0]
		validation = validation_arr[k][key]
		if (not check(validation, current_customer[key])):
			issue_list.append(key)
	return issue_list

def check(validation, value):
	# TODO: validation
	return False

def is_length_valid(min, max, value):
	length = len(value)
	if (length >= min and length <= max):
		return True
	return False

def is_required(req_bool, value):
	# make validation for checking if the value is there or not
	if (req_bool):
		if (value == None):
			return False
	return True

def is_type_valid(type_value, value):
	# TODO: validate type
	if (type_value == "boolean"):
		if (type(value) is bool):
			return True
	if (type_value == "number"):
		if ((type(value) is int) or (type(value) is float)):
			return True
	if (type_value == "string"):
		if ((type(value) is str)):
			return True
	return False


@app.route('/full')
def full():
	return jsonify(get_api_resp(1))

@app.route('/checkTypeFunction')
def test_type():
	return str(is_type_valid("number", "2313"))