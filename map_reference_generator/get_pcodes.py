from urllib2 import urlopen
import json

url = "https://s3.amazonaws.com/itos-humanitarian/MLI/MLIAdmin3.json"
attribute = "mli_admbnda_admALL_pnts_admin3Pcode"

pcodes = []
response = urlopen(url)
data = json.loads(response.read())
for obj in data['objects']['geom']['geometries']:
	pcodes.append(obj['properties'][attribute])

print json.dumps(pcodes)