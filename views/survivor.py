import json
from flask import request
from flask import Response
from app import app
from app import db
from controllers import survivorctl

@app.route('/update_survivor', methods=['PUT'])
def update_survivor():
	"""
	A survivor must have the ability to update their last location.
	input: {id:id, lat:lat, lon:lon}
	returns: {success:True|False}
	"""
	result, status = survivorctl.update_survivor(json.loads(request.data))
	
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/flag_survivor', methods=['PUT'])
def flag_survivor():
	"""
	Flag the survivor as infected.
	A survivor is marked as infected when at least three other survivors report their cntamination.
	input: {id:id, infected:id1}
	returns: {success:True|False}
	"""
	result, status  = survivorctl.flag_survivor(json.loads(request.data))
	
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/add_survivor', methods=['POST'])
def add_survivor():
	"""
	Add survivors to the database A survivor must have a name, age, gender, ID and last location (latitude, longitude).
	A survivor also has an inventory of resources (which you need to declare upon the registration of the survivor). This can include Water, Food, Medication and Ammunition.
	input: {id:id, lat:lat, lon:lon, name:name, age:age, gender:gender, inventory:[inv1, ...]}
	returns: {success:True|False}
	"""
	result, status  = survivorctl.add_survivor(json.loads(request.data))
	
	return Response(json.dumps(result), status=status, mimetype='application/json')

@app.route('/remove_survivor', methods=['DELETE'])
def remove_survivor():
	"""
	Remove a member, for some reason
	input: {id:id}
	returns: {success:True|False}
	"""
	result, status  = survivorctl.remove_survivor(json.loads(request.data))
	
	return Response(json.dumps(result), status=status, mimetype='application/json')
