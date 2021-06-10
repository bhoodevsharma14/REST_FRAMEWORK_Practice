import requests
import json


URL = 'http://127.0.0.1:8000/stucrud/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    r = requests.get(url=URL,data=json_data)

    data = r.json()
    print(data)

def post_data():
    data = {
        'name':'Priyank Joshi',
        'roll':106,
        'city':'Indore'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json
    print(data)

post_data()
# get_data()