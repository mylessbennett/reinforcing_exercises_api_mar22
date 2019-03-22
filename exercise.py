import requests
import json

response = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')                                   
body = json.loads(response.content) 

djibouti = body[55]

djibouti_leg = djibouti['legislatures'][0]['popolo_url'] 

politicians = requests.get(djibouti_leg)                                     
politicians_json = json.loads(politicians.content)  
politician_name = politicians_json['persons'][0]['name']
print(politician_name)