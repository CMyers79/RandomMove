import requests
import json


array_json = {'array': [2,3,4,5,6,7,8,9]}

random_move_response = requests.get('http://127.0.0.1:5000/getmove', json=array_json)
print(random_move_response)

random_move_json = random_move_response.json()
random_move = random_move_json['move']

print(random_move)
