from py2neo import cypher
import json

with open("Userdata.json") as json_file:
    json_data = json.load(json_file)
    #print(json_data)


session = cypher.Session("http://localhost:7474/")
tx = session.create_transaction()

# send three statements to for execution but leave the transaction open
for Poi in json_data:
    qry = "MERGE (a:Person {})".format(Poi)
    print(qry)
    tx.append(qry)
tx.commit()
