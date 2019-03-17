######################################################
# Title: f_server
# Description: A simple server to test bruteforce attacks.
# Author: Tarllark
#
######################################################

from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/', methods=['POST'])
def brute():
	content = request.get_json()
	if(comparePSW(client_password = content["password"])):
		return '', 200
	else:
		return '', 403

def comparePSW(client_password = ''):
	SERVER_PASSWORD = 'aA'
	res = client_password == SERVER_PASSWORD
	return res
