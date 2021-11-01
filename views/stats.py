import json

from flask import Response
from app import app
from models.survivors import *

def get_data(infected):

	result = {"success": False, "percentage":None}
	status = 200
	try:
		many = Survivors.query.filter_by(infected=infected).count()
		size = Survivors.query.count()
		size = 1 if size == 0 else size
		result["percentage"] = many * 100 / size;
	except Exception as e:
		print(e)
		result["success"] = False
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/stats/infected_survivors', methods=['GET'])
def stats_infected_survivors():
	"""
	Show Percentage of infected survivors.
	input: None
	output: array of infected survivors
	"""
	return get_data(True)

@app.route('/stats/non_infected_survivors', methods=['GET'])
def stats_non_infected_survivors():
	"""
	Show Percentage of non-infected survivors.
	input: None
	output: array of non infected survivors
	"""
	return get_data(False)
