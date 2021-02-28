import pymysql
from authentication import authentication
from flask import jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import datetime

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'myBase'
}
  
connection=None
cursor=None


class User(object):	
	def __init__(self, id, username):
		self.id = id
		self.username = username

	def __str__(self):
		return "User(id='%s')" % self.id

@authentication.route('/rest-auth')
@jwt_required()
def get_response():
	return jsonify('You are an authenticate person to see this message')

def authenticate(username, password):	

	if username and password:
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()

		cursor.execute('SELECT id, username, pwd FROM users WHERE username=%s', (str(username),))
		row = cursor.fetchone()
			
		if row:
			if check_password_hash(row[2], password):
				cursor.close() 
				connection.close() 
				return User(row[0], row[1])

	cursor.close() 
	connection.close()      
	return None


def identity(payload):
	if payload['identity']:
		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()

		cursor.execute('SELECT id, username FROM users WHERE id=%s', payload['identity'])
		row = cursor.fetchone()
		if row:
			cursor.close() 
			connection.close() 
			return (row[0], row[1])

	cursor.close() 
	connection.close() 
	return None
	
jwt = JWT(authentication, authenticate, identity)

if __name__ == '__main__':
    authentication.run("0.0.0.0", 6000)