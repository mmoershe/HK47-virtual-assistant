import json
import random 

json_file = open("data.json", "r")
json_data = json.load(json_file)

for i in range(10):
    print(json_data["status"][random.randint(0, len(json_data["status"])-1)])
