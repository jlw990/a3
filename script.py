import json
import csv
import pprint as p


with open('score_all_years.csv') as f:
    propertyDict = [{k: v for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

codeList = set()

for each in propertyDict:
    codeList.add(each["code"])


final = {}

for i in range(len(propertyDict)):
    final[propertyDict[i]["code"]] = propertyDict[i]

p.pprint(final)


# opening the geojson
with open('worldcopy.geojson', 'r') as f:
    data = json.load(f)

# Python dictionary containing properties to be added to each GeoJSON Feature
properties_dict = {
    {'eighteen': '4.724',
         'fifteen': '4.642',
         'name': 'South Africa',
         'nineteen': '4.722',
         'pop20': '47938663',
         'rank15': '113',
         'rank16': '116',
         'rank17': '101',
         'rank18': '105',
         'rank19': '106',
         'rank20': '101',
         'seventeen': '4.828999996',
         'sixteen': '4.459',
         'twenty': '4.828999996'}
    }

#Loop over GeoJSON features and add the new properties
for feat in data['features']:
    curr_id = feat['id']
    if curr_id in codeList:
        feat["properties"] = final[curr_id]


#Write result to a new file
with open('new.geojson', 'w') as f:
    json.dump(data, f)
