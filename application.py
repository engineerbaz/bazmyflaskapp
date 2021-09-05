from flask import Flask, request,jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return 'Hello!!!', 200      # 200 is HTTP the response code to be returned to client

from datetime import datetime
@app.route('/datetime', methods=['GET'])
def print_today():
	return str(datetime.now()), 200 


@app.route('/users/<username>')
def get_user(username):
	return "user: "+str(username),200
    
#http://localhost:5000/add?op1=3&op2=4
@app.route('/add', methods=['GET'])
def add():
    if 'op1' in request.args.keys() and 'op2' in request.args.keys():
        a = int(request.args['op1'])
        b = int(request.args['op2'])
        return jsonify({"operand 1": a, "operand 2": b, "sum":a+b}) #return JSON object
    else:
        return jsonify({'error':'missing parameter(s)'}), 400
    

#request content-type=application/json
#request body format: {"op1":3,"op2":5}
@app.route('/mul', methods=['POST'])
def mul():
	
	data = request.json #get json data from request body
	a = data["op1"]
	b = data["op2"]
	
	return jsonify({'mul':a*b}),200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
