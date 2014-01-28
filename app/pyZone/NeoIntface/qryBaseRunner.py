from py2neo import neo4j, cypher
import json
import qryBase


lister=[]
# print ("QRY001 = "+ qryBase.qry001)
qry = qryBase.addPoI("Hilda W. Burgess")
# print ("QRY = "+ qry)
graph_db = neo4j.GraphDatabaseService()
query = neo4j.CypherQuery(graph_db, qry)
# print(query)
data = query.execute()
for item in data:
	# print(len(item.columns))
	for x in range(len(item.columns)):
		col = item.columns[x]
		val = item.values[x]
		# print("PNC_REF is {} ".format(val))
		ans = col+":"+str(val)
		lister.append(ans)
print("Listing : {}".format(lister))