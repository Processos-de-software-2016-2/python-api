import os
import uuid
import mimetypes
import MySQLdb
import json
import collections

import falcon


class User(object):
	def __init__(self, uData):
		self.__dict__ = json.loads(uData)


class AllUsers(object):
	def on_get(self, req, resp):
		"""GET"""
		db = MySQLdb.connect (host = "localhost",
							  user = "victor",
							  passwd = "123",
							  db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		cursor.execute("SELECT id, nome, email, idade FROM users")
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
			q2j = collections.OrderedDict()
			q2j['id'] = q[0]
			q2j['nome'] = q[1]
			q2j['email'] = q[2]
			q2j['idade'] = q[3]
			queryObjects.append(q2j)
		resp.body = json.dumps(queryObjects)
		db.close()

class NewUser(object):
	def on_post(self, req, resp):
		#Ainda não funciona.
		resp.status = falcon.HTTP_201 
		body = req.stream.read()
		newusersql = User(body)
		equery = "INSERT INTO users (nome, email, idade, senha) VALUES (%s %s %s %s)"
		cursor.execute(equery, (newusersql.nome, newusersql.email, newusersql.idade, newusersql.senha,))
		resp.body = body


