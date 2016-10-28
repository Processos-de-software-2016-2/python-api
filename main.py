# main.py

import os
import uuid
import mimetypes
import users
import falcon
import gevent
from gevent import socket

# falcon.API instances are callable WSGI apps
app = falcon.API()

# things will handle all requests to the '/things' URL path
app.add_route('/user', users.AllUsers())
app.add_route('/user/new', users.NewUser())
