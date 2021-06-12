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
        'name':'Akansha',
        'roll':112,
        'city':'Dewas'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

def update_data(id=None):
    data = {
        'id':id,
        'name':'Ballu',
        'roll':109,
        'city':'Mandsaur'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

def delete_data(id=None):
    data = {
        'id':id
    }
    json_data =json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

# delete_data(12)
update_data(11)
# post_data()
# get_data()