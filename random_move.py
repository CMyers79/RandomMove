from re import A
from flask import Flask, request, jsonify
import random


generator = Flask(__name__)

@generator.route('/getmove', methods = ['POST', 'GET'])
def get_move():
    req_data = request.get_json()
    array = req_data['array']
    our_number = random.choice(array)
    if request.method == "GET":
        if our_number in array:
            array.remove(our_number)
            new_array = array
            req_data['array'] = new_array
            req_data['move'] = our_number
            return jsonify(req_data)
    else:
        print(req_data)

if __name__ == '__main__':
    generator.run(debug=True)
