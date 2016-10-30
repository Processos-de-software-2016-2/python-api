# main.py

import os
import uuid
import mimetypes
import falcon
import gevent
from gevent import socket
from controller.users import Users

# falcon.API instances are callable WSGI apps
app = falcon.API()

users = Users()

# things will handle all requests to the '/things' URL path
app.add_route('/users', users)
