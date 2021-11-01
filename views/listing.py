import json
import requests
import operator
from flask import request
from flask import Response
from app import app


def get_data(infected, orderBy=None):
	result = {"success": False, "data":[]}
	status = 200
	assert(orderBy in ['id', 'name', 'gender', 'location', None])
	try:
		data = []
		users = Survivors.query.filter_by(infected=infected).all().order_by(orderBy)
		for user in users:
			data.append(user.to_json())
		result["data"] = data
	except Exception as e:
		print(e)
		result["success"] = False;
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/listing/robot_locations', methods=['GET'])
def robot_locations():
	"""
	Show robots and their locations
	input: orderBy=[category | model | serialNumber | manufacturedDate| None] 
	output: list of robots details 
	"""
	orderBy = request.args.get('orderBy')
	assert(orderBy in ['category', 'model', 'serialNumber', 'manufacturedDate', None])
	response = requests.get(app.config.get("ROBOTS_URL"))
	status = response.status_code
	result = {"success": False, "data":[]}

	if(status == 200):
		resp = response.json()
		if orderBy != None:
			resp.sort(key=operator.itemgetter(orderBy))
		result["data"] = resp

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
