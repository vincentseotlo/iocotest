#!/bin/sh
json='{"id":1, "lat":20.1, "lon":10.1, "name":"name", "age":12, "gender":"Male", "inventory":["inv1","inv2","inv3"]}'
curl -d "${json}" -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/add_survivor

json='{"id":2, "lat":20.1, "lon":10.1, "name":"name", "age":12, "gender":"Male", "inventory":["inv1","inv2","inv3"]}'
curl -d "${json}" -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/add_survivor

json='{"id":3, "lat":20.1, "lon":10.1, "name":"name", "age":12, "gender":"Male", "inventory":["inv1","inv2","inv3"]}'
curl -d "${json}" -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/add_survivor

json='{"id":4, "lat":20.1, "lon":10.1, "name":"name", "age":12, "gender":"Male", "inventory":["inv1","inv2","inv3"]}'
curl -d "${json}" -H 'Content-Type: application/json' -X POST http://127.0.0.1:5000/add_survivor


json='{"id":1, "infected":1}'
curl -d "${json}" -H 'Content-Type: application/json' -X PUT http://127.0.0.1:5000/flag_survivor

json='{"id":2, "infected":1}'
curl -d "${json}" -H 'Content-Type: application/json' -X PUT http://127.0.0.1:5000/flag_survivor

json='{"id":3, "infected":1}'
curl -d "${json}" -H 'Content-Type: application/json' -X PUT http://127.0.0.1:5000/flag_survivor

json='{"id":4, "infected":1}'
curl -d "${json}" -H 'Content-Type: application/json' -X PUT http://127.0.0.1:5000/flag_survivor



json='{"id":1,"lat":11, "lon":11}'
curl -d "${json}" -H 'Content-Type: application/json' -X PUT http://127.0.0.1:5000/update_survivor



json='{"id":1}'
curl -d "${json}" -H 'Content-Type: application/json' -X DELETE http://127.0.0.1:5000/remove_survivor



curl -X GET http://127.0.0.1:5000/stats/infected_survivors
curl -X GET http://127.0.0.1:5000/stats/non_infected_survivors

curl -X GET 'http://127.0.0.1:5000/listing/robot_locations?orderBy=model'
curl -X GET 'http://127.0.0.1:5000/listing/infected_survivors?orderBy=name'
curl -X GET 'http://127.0.0.1:5000/listing/non_infected_survivors?orderBy=name'
