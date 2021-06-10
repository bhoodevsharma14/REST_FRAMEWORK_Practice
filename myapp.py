import requests
import json


URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'Minakshi Upadhyay',
    'roll':104,
    'city':'Mandsaur'
}
json_data = json.dumps(data)
# r = requests.get(url = URL)
r = requests.post(url = URL,data=json_data)
data = r.json()
print(data)