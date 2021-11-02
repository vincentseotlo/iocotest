import json

from flask import Response
from app import app
from controllers import survivorctl

def get_stats(infected):
	result, status = survivorctl.get_stats(infected)
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/stats/infected_survivors', methods=['GET'])
def stats_infected_survivors():
	"""
	Show Percentage of infected survivors.
	input: None
	output: array of infected survivors
	"""
	return get_stats(True)

@app.route('/stats/non_infected_survivors', methods=['GET'])
def stats_non_infected_survivors():
	"""
	Show Percentage of non-infected survivors.
	input: None
	output: array of non infected survivors
	"""
	return get_stats(False)

@app.route('/stats/get_list_of_reporters', methods=['GET'])
def stats_non_infected_survivors():
	"""
	Show Percentage of non-infected survivors.
	input: None
	output: array of non infected survivors
	"""
	result, status = survivorctl.get_reporters()
	return Response(json.dumps(result), status=status, mimetype='application/json')

