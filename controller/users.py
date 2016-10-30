#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user import UserModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class Users(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
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
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class User(object):
	def on_get(self, req, resp, id):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		id = int(id)
		#Executa a query
		sql = "SELECT id, nome, email, idade FROM users WHERE id = %d" % (id)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()
	def on_post(self, req, resp):
		#Ainda nao funciona.
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()

		resp.status = falcon.HTTP_201 
		body = req.stream.read()
		newusersql = self.mountUser(body)
		equery = "INSERT INTO users (nome, email, idade, senha) VALUES (%s, %s, %s, %s)"

		try:
			cursor.execute(equery, (newusersql['name'], newusersql['email'], newusersql['age'], newusersql['password'],))
			db.commit()
		except:
		 	db.rollback()
		 	print "Insert ERROR: ", sys.exc_info()[0]
		 	resp.status = falcon.HTTP_500

		resp.body = body
		db.close()
	def mountUser(self, uData):
		return json.loads(uData)

class UserEmail(object):
	def on_get(self, req, resp, email):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		sql = "SELECT id, nome, email, idade FROM users WHERE email LIKE '%s'" % (email)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()		
