import pymysql
from flask import Flask, jsonify, redirect, request, after_this_request
import mysql.connector
import json
import sys
#from flask_cors import CORS

catalog = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db-Catalog',
    'port': '3306',
    'database': 'baseCatalog'
}
  
connection = None
cursor = None


class Movie(object):	
	def __init__(self, id, title, description, durationMin, image, idType):
		self.id = id
		self.title = title
		self.description = description
		self.durationMin = durationMin
		self.image = image
		self.idType = idType


	def __str__(self):
		return "Movie(id='%s')" % self.id
	
	def dump(self):
		return { 'id' : self.id ,'title': self.title,'description': self.description,'durationMin': self.durationMin,'image': self.image, 'idType':self.idType,}

def getAllMovies():	
	listMovies=[]
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM movies')
	movies = cursor.fetchall()
	if movies: 
		for movie in movies: 
			listMovies.append(Movie(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
	else :
		print("error, no data found", file=sys.stderr)

	cursor.close() 
	connection.close() 
	return listMovies

def getPopularMovies():	
	listMovies=[]
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute('SELECT * FROM movies where idType = 1')
	movies = cursor.fetchall()
	if movies: 
		for movie in movies: 
			listMovies.append(Movie(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
	else :
		print("error, no data found", file=sys.stderr)

	cursor.close() 
	connection.close() 
	return listMovies	


def getActionMovies():	
	listMovies=[]
	cursor.execute('SELECT * FROM movies where idType = 2')
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	movies = cursor.fetchall()
	if movies: 
		for movie in movies: 
			listMovies.append(Movie(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
	else :
		print("error, no data found", file=sys.stderr)

	cursor.close() 
	connection.close() 
	return listMovies	

def getTVShowsMovies():	
	listMovies=[]
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM movies where idType = 3')
	movies = cursor.fetchall()
	if movies: 
		for movie in movies: 
			listMovies.append(Movie(movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
	else :
		print("error, no data found", file=sys.stderr)

	cursor.close() 
	connection.close() 
	return listMovies


@catalog.route('/getAllMovies', methods=['GET'])
def getMovies():

	movies=getAllMovies()
	json_movies = json.dumps([movie.dump() for movie in movies])
	#print("json_Movies" + str(json_movies), file=sys.stderr)
	return json_movies

if __name__ == '__main__':
    catalog.run("0.0.0.0", 7000)