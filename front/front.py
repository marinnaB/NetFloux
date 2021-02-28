from typing import List, Dict
from flask import Flask, jsonify, redirect, flash, request, render_template, session, send_from_directory
import json
import requests 
from functools import wraps
import os
import sys

front = Flask(__name__)
front.config['SECRET_KEY'] = 'secret-key'

def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        # Check to see if it's in their session
        if 'api_session_token' not in session:
            # If it isn't then redirect to login page
            return redirect("/login")

        # Otherwise just send them where they wanted to go
        return func(*args, **kwargs)

    return check_token

@front.route("/")
def index():
    return render_template("index.html")

@front.route('/catalog')
@require_api_token
def catalog():
    return render_template("catalog.html")

@front.route('/login')
def login():
    if 'api_session_token' not in session:
        # If it isn't then redirect to login page
        return render_template("login.html")
    else:
        return redirect("/catalog")

@front.route('/loginVerify', methods=['POST'])
def loginVerify():
    username = request.form.get("username")
    password = request.form.get("password")

    url = 'http://authentication:6000/auth'
    data = {'username': username,'password':password}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    if (r.status_code is 200):
        response = r.json()
        token = response['access_token']

        # Put the token and the username in the session
        session['api_session_token'] = token
        session['username'] = username

        # allow user into protected view
        return redirect("/catalog")
    else:
        flash("incorrect username or password.")
    
    return redirect("/login")

@front.route("/logout")
def logout():
    #logout_user()
    return redirect("/")

@front.route("/mylist")
@require_api_token
def myList():
    return render_template("myList.html")

@front.route('/getAllMovies', methods=['GET'])
def getMoviesFRomCatalog():
    url = 'http://catalog:7000/getAllMovies'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url,headers=headers)
    print("reponse json: " + str(r.content), file=sys.stderr)
    return r.content

@front.route('/getMyList', methods=['GET'])
def getMyList():
    url = 'http://mylist:8000/getMyList'
    data = {'username': session['username']}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.get(url, data=json.dumps(data), headers=headers)
    print("my list of movies: " + str(r.content), file=sys.stderr)
    return r.content

if __name__ == '__main__':
    front.run(host='0.0.0.0')

