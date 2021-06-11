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
        'name':'Balram',
        'roll':111,
        'city':'Barujna'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

def update_data(id=None):
    data = {
        'id':4,
        'city':'Bagli'
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

# delete_data(9)
# update_data(4)
post_data()
# get_data()