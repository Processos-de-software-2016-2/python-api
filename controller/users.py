#users.py

import falcon
import json
from model.user import User

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class Users(object):

    def __init__(self):
        self.users = []

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        user = User(1, 'João', 'example@example.com', 20, '123456')
        resp.body = (json.dumps(user.__dict__))


    def on_post(self, req, resp):
	"""Handles POST requests"""
	try:
	    raw_json = req.stream.read()
	except Exception as ex:
	    raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)
 	try:
	    result_json = json.loads(raw_json, encoding='utf-8')
	except ValueError:
	    raise falcon.HTTPError(falcon.HTTP_400,
	        'Malformed JSON',
	        'Could not decode the request body. The '
	        'JSON was incorrect.')


        #Cria o usuário passando as infos do JSON
	user = User(result_json['id'],result_json['name'],result_json['email'],result_json['age'],result_json['password'])
        #add user na lista
        users.append(user)
        
	resp.status = falcon.HTTP_202
	resp.body = json.dumps(result_json, encoding='utf-8')
