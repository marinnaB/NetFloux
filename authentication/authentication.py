from typing import List, Dict
from flask import Flask
from flask import render_template
from flask import request, jsonify
#import mysql.connector
import json
from flaskext.mysql import MySQL
#from flask.ext.mysql import MySQL

authentication = Flask(__name__)
authentication.config['SECRET_KEY'] = 'secret-key'




@authentication.route('/verify', methods=['POST'])
def verify():
    username = request.form.get("username")
    password = request.form.get("password")

    url = 'http://authentication:6000/auth'
    data = {'username': username,'password':password}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    response = r.json()

    if (r.status_code is 200):
        token = response['access_token']

        # Move the import to the top of your file!
        from flask import session

        # Put it in the session
        session['api_session_token'] = token

        # allow user into protected view

    return render_template("../front/templates/catalog.html")

