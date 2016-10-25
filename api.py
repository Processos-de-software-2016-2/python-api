# api.py

# Let's get this party started!
import falcon
from users import Users

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
users = Users()

# things will handle all requests to the '/things' URL path
app.add_route('/users', users)
