import requests
import json

baseUrl="http://localhost:5279/api/"

def httpRequestForJsonWord(data):
    url = baseUrl+"Word/ListCreate"
    bearerToken = login()
    headers = {"Authorization": "Bearer " + bearerToken,
               "Content-Type": "application/json; charset=utf-8",
               "accept": "text/plain"
               }
    print(data)
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def login():
    url = baseUrl+"Authentication/Login"
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
        "userName": "engineerFM",
        "password": "123456",
    }
    response = requests.post(url, headers=headers, json=data)
    json_obj = json.loads(response.text)
    return json_obj['payload']['token']
