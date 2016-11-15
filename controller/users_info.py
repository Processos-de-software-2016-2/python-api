#users.py

import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user_info import UserInfoModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class UsersInfo(object):
	def on_get(self, req, resp):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		#Executa a query
		cursor.execute("SELECT id, facebook, whatsapp, id_user FROM users_info")
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserInfoModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

class UserInfo(object):
	def on_get(self, req, resp, id):
		#"""GET"""
		db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
		cursor = db.cursor()
		resp.status = falcon.HTTP_200  # Ok!
		id = int(id)
		#Executa a query
		sql = "SELECT id, facebook, whatsapp, id_user FROM users_info WHERE id_user = %d" % (id)
		cursor.execute(sql)
		#Recebe todos os resultados
		query = cursor.fetchall()
		#Cria uma lista guardar os dados convertidos
		queryObjects = []
		#Converte
		for q in query:
				user = UserInfoModel(q[0], q[1], q[2], q[3])
				queryObjects.append(user.__dict__)
		resp.body = json.dumps(queryObjects)
		db.close()

