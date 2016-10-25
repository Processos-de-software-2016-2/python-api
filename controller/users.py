#users.py

import falcon
import json
from model.user import User

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class Users(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        user = User(1, 'João', 'example@example.com', 20, '123456')
        resp.body = (json.dumps(user.__dict__))
