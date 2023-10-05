import json

#Example json
x= '{"name":"Carlo","age":"22", "city":"San Mateo"}'

#parse json
y = json.loads(x)
print("The output of the json file is", y)
print("Name:", y["name"])
print("Age:", y["age"])
print("City:", y["city"])