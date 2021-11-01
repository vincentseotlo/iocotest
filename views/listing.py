import json
from flask import request
from flask import Response
from app import app
from controllers import survivorctl
from controllers import robotworld


def get_data(infected, orderBy=None):
	result, status = survivorctl.get_data(infected, orderBy)
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/listing/robot_locations', methods=['GET'])
def robot_locations():
	"""
	Show robots and their locations
	input: orderBy=[category | model | serialNumber | manufacturedDate| None] 
	output: list of robots details 
	"""
	orderBy = request.args.get('orderBy')
	result, status = robotworld.robot_locations(orderBy)

	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/listing/infected_survivors', methods=['GET'])
def listing_infected_survivors():
	"""
	List of infected survivors
	input: orderBy=[id|name|gender|location|None] 
	output: list of infected users 
	"""
	orderBy = request.args.get('orderBy')
	return get_data(True, orderBy)

@app.route('/listing/non_infected_survivors', methods=['GET'])
def listing_non_infected_survivors():
	"""
	List of non infected survivors
	input: orderBy=[id|name|gender|location|None] 
	output: list of infected users 
	"""
	orderBy = request.args.get('orderBy')
	return get_data(False, orderBy)
