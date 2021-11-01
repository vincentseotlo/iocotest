import json
import operator
import requests
from app import app

def robot_locations(orderBy):
	"""
	Show robots and their locations
	input: orderBy=[category | model | serialNumber | manufacturedDate| None] 
	output: list of robots details 
	"""
	assert(orderBy in ['category', 'model', 'serialNumber', 'manufacturedDate', None])
	response = requests.get(app.config.get("ROBOTS_URL"))
	status = response.status_code
	result = {"success": False, "data":[]}

	if(status == 200):
		resp = response.json()
		if orderBy != None:
			resp.sort(key=operator.itemgetter(orderBy))
		result["data"] = resp

	return (result, status)