from functools import wraps
from flask import Flask, request, Response, abort, jsonify
#from datetime import datetime, timedelta
#from dateutil.parser import parse
#import os

#import json
#import pytz
#from simple_salesforce import Salesforce
#import iso8601
#import logging
#from collections import OrderedDict

app = Flask(__name__)

hardarchive = [
  {
    'rien': u'du tout'
  }
]

def authenticate():
  """Sends a 401 response that enables basic auth"""
  return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def little_func(f):
  @wraps(f)
  def print_warning(*args, **kwargs):
    print("You are in a wrapper\n")
    return f(*args, **kwargs)

  return print_warning

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth:
      return authenticate()
    return f(*args, **kwargs)

  return decorated


@app.route('/api/a', methods=['GET'])
@little_func
def get_hardarchive():
    return jsonify({'hardarchive': hardarchive})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
