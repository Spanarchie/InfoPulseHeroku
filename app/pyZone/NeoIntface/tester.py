
import json

def add_employee(jsonSalaries, name, salary):
    # Add your code here
    jsonSalaries = json.loads(jsonSalaries)
    jsonSalaries[name] = str(salary)
    jsonSalaries = json.dumps(jsonSalaries)
    return jsonSalaries



with open("5090.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

response = []
y = json_data["cols"]
print(len(y))
print ("COLS : {}".format(y))
x = json_data["data"]
print(len(x))
#jsonData = '{}'
for b in x:
    jsonData = '{}'
    for itm in range(len(b)):
        jsonData = add_employee(jsonData, y[itm], b[itm])

    response.append(jsonData)

#print json.dumps(response)
with open('5090data.json', 'w') as outfile:
    json.dump(response, outfile)