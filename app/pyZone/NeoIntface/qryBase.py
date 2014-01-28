qry001 = "match (x:PoI)-[:HAS_WARRANT]-(z:WRNT{Status:'Open'}), (x:PoI)-[:DRV_LNC]->(h), (x)-[:KNOWN_ACCOMPLICE]-(w) where x.name='Lois L. Black' return x.marker as Markers, h.DriverStatus as DriverStatus, w.name as accomplice, count(z.Status) as OpenWarrants"

def addPoI(aName):
    qry001 = "match (x:PoI)-[:HAS_WARRANT]-(z:WRNT{Status:'Open'}), (x:PoI)-[:DRV_LNC]->(h), (x)-[:KNOWN_ACCOMPLICE]-(w) where x.name='"+aName+"' return x.marker as Markers, h.DriverStatus as DriverStatus, w.name as accomplice, count(z.Status) as OpenWarrants"
    return qry001
