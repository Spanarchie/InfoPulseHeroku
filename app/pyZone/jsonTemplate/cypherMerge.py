from py2neo import cypher
import json

def json2cypher(myJsonObj):
    data  = json.loads(myJsonObj)
    qry = "MERGE (a:Person {"
    for key in data:
        qry = qry+key+': "'+data[key]+'",'
    qry = qry[:-1] +'})'
    return qry

def json2node(type, myJsonObj, lbls = []):
    data  = json.loads(myJsonObj)
    qry = "MERGE (a:"+type
    for lbl in lbls:
        qry= qry+":"+data[lbl]
    qry=qry+" {"
    for key in data:
        qry = qry+key+': "'+data[key]+'",'
    qry = qry[:-1] +'})'
    return qry





with open("Userdata.json") as json_file:
    json_data = json.load(json_file)

session = cypher.Session("http://localhost:7474/")
tx = session.create_transaction()

# send three statements to for execution but leave the transaction open
for Poi in json_data:
    #qry = json2cypher(Poi)
    qry = json2node("User",Poi, ["email","Works_for"])

    print("qry = {}".format(qry))
    tx.append(qry)
tx.commit()
