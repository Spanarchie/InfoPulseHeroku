import json

def jsonBuilder(jsonObj, key, val):
	# Add your code here
    jsonInst = json.loads(jsonObj)
    jsonInst [key] = str(val)
    jsonResp = json.dumps(jsonInst )
    return jsonResp

with open("wFlow.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

response = []
y = json_data["title"]
print(len(y))
print ("COLS : {}".format(y))
x = json_data["data"]
print(len(x))
#jsonData = '{}'
for b in x:
    jsonData = '{}'
    for itm in range(len(b)):
        jsonData = jsonBuilder(jsonData, y[itm], b[itm])
    print("Date of Birth is {}").format(jsonData["DoB"])
    response.append(jsonData)

#print json.dumps(response)
with open('wFlowdata.json', 'w') as outfile:
    json.dump(response, outfile)