import pymysql
from flask import Flask, jsonify, redirect, request, after_this_request
import mysql.connector
import json
import sys
#from flask_cors import CORS

mylist = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db-Catalog',
    'port': '3306',
    'database': 'baseCatalog'
}
  
connection = None
cursor = None


class MyList(object):	
	def __init__(self, id, idUser, idMovie, title,imageMovie, username):
		self.id = id
		self.idUser = idUser
		self.idMovie = idMovie
		self.title=title
		self.imageMovie=imageMovie
		self.username=username

	def __str__(self):
		return "Movie(id='%s')" % self.id
	
	def dump(self):
		return { 'id' : self.id ,'idUser': self.idUser,'idMovie': self.idMovie, 'title': self.title ,'imageMovie': self.imageMovie,'username': self.username}

def getListUser(username):	
	listMovies=[]
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute('SELECT ml.id, ml.idUser, ml.idMovie, m.title,  m.imageMovie, ml.username FROM myList ml inner join movies m on ml.idMovie = m.id WHERE ml.username=%s', (username,))
	movies = cursor.fetchall()
	if movies: 
		for movie in movies: 
			listMovies.append(MyList(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
	else :
		print("error, no data found", file=sys.stderr)

	cursor.close() 
	connection.close() 
	return listMovies


@mylist.route('/getMyList', methods=['GET'])
def getMyList():
	
	data=json.loads(request.data)
	idUser=data['username']

	movies=getListUser(idUser)
	json_movies = json.dumps([movie.dump() for movie in movies])
	print("User list: " + str(json_movies), file=sys.stderr)

	return json_movies

if __name__ == '__main__':
    mylist.run("0.0.0.0", 8000)