import json
import glob
from pprint import pprint
result = []

for f in glob.glob("*.json"):
	#print(f, end = ' ')
	data = json.load(open(f))
	#print(len(data))
	for i in range(len(data)):
		result.append(data[i])

with open("merged_file.json", "w+") as outfile:
     json.dump(result, outfile)

#data = json.load(open('merged_file.json'))
#print(len(data))