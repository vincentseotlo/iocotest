import json
from app import db
from models.survivors import *

def update_survivor(data):
	"""
	A survivor must have the ability to update their last location.
	input: {id:id, lat:lat, lon:lon}
	returns: {success:True|False}
	"""
	result = {"success": False}
	status = 200
	try:
		user = Survivors.query.get(data["id"])
		if user != None:
			user.lat = data["lat"]
			user.lon = data["lon"]
			db.session.commit()
			result["success"] = True;
		else:
			status = 404
	except Exception as e:
		print(e)
		result["success"] = False;
	
	return (result, status)

def flag_survivor(data):
	"""
	Flag the survivor as infected.
	A survivor is marked as infected when at least three other survivors report their cntamination.
	input: {id:id, infected:id1}
	returns: {success:True|False}
	"""
	result = {"success": False}
	status = 200
	try:
		user = Survivors.query.get(data["infected"])
		if user != None:
			count = Infected.query.filter_by(reporter=data["id"]).count()
			if count == 0:
				flag = Infected(survivor=user.id, reporter=data["id"])
				db.session.add(flag)
				#db.session.commit()
				count = Infected.query.filter_by(survivor=user.id).count()
				user.infected = True if count >= 3 else False
				db.session.commit()
				result["success"] = True;
		else:
			status = 404
	except Exception as e:
		print(e)
		result["success"] = False;
	
	return (result, status)

def add_survivor(data):
	"""
	Add survivors to the database A survivor must have a name, age, gender, ID and last location (latitude, longitude).
	A survivor also has an inventory of resources (which you need to declare upon the registration of the survivor). This can include Water, Food, Medication and Ammunition.
	input: {id:id, lat:lat, lon:lon, name:name, age:age, gender:gender, inventory:[inv1, ...]}
	returns: {success:True|False}
	"""
	result = {"success": True}
	status = 200
	try:
		user = Survivors(	id=data["id"], 
							name=data["name"], 
							flags='{}',
							gender=data["gender"],
							lat=data["lat"], 
							lon=data["lon"],
							infected=False)
		db.session.add(user)
		db.session.commit()
		for inp in data["inventory"]:
			inv = Inventory(survivor=user.id, name=inp)
			db.session.add(inv)
		db.session.commit()
	except Exception as e:
		print(e)
		result["success"] = False;
	
	return (result, status)

def remove_survivor(data):
	"""
	Remove a member, for some reason
	input: {id:id}
	returns: {success:True|False}
	"""
	result = {"success": False}
	status = 200
	try:
		user = Survivors.query.get(data["id"])
		if user != None:
			print(user.to_json())
			inventory = Inventory.query.filter_by(survivor=user.id).all()
			for inv in inventory:
				db.session.delete(inv)
			db.session.delete(user)
			db.session.commit()
			result["success"] = True
		else:
			status = 404
	except Exception as e:
		print(e)
		result["success"] = False;
	
	return (result, status)

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
	return (result, status)

def get_stats(infected):

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
	return (result, status)