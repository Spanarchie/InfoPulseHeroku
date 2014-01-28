import py.test

from config import lblList
import json


def json2node(type, myJsonObj):
    data  = json.loads(myJsonObj)
    lbls = lblList[type]
    qry = "MERGE (a:"+type
    for lbl in lbls:
        qry= qry+":"+data[lbl]
    qry=qry+" {"
    for key in data:
        qry = qry+key+': "'+data[key]+'",'
    qry = qry[:-1] +'})'
    return qry

if __name__ == '__main__':
    jsn = '{"userRef":"RefRoger", "username": "Rogger"}'
    actu = json2node("user", jsn)
    expt = 'MERGE (a:user:RefRoger:Rogger {username: "Rogger",userRef: "RefRoger"})'
    assert actu == expt