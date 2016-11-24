import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user_match import UserMatchModel
from model.skill import SkillModel
from model.user import UserModelMatch


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class UserMatch(object):
    def on_get(self, req, resp):
        #"""GET ALL PAIR USER-SKILL"""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware",charset="utf8", use_unicode = True)
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        #Executa a query
        cursor.execute("SELECT  id , id_user_not, id_user_has, id_skill  FROM user_match")
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
            user_skill = UserMatchModel(q[0], q[1], q[2], q[3])
            queryObjects.append(user_skill.__dict__)
        resp.body = json.dumps(queryObjects)
        db.close()

    def on_post(self, req, resp):
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware",charset="utf8", use_unicode = True)
        cursor = db.cursor()
        body = req.stream.read()
        newusersql = self.mountUserSkill(body)
        equery = "INSERT INTO user_match (id_user_not, id_user_has, id_skill) VALUES (%s, %s, %s)"

        try:
            cursor.execute(equery, (newusersql['id_user_not'], newusersql['id_user_has'], newusersql['id_skill'],))
            cursor.execute("SELECT LAST_INSERT_ID() FROM user_match");
            result = {'id': int(cursor.fetchone()[0])}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_201
            db.commit()
        except:
            db.rollback()
            print "Insert ERROR: ", sys.exc_info()
            resp.status = falcon.HTTP_500
            resp.body = "Erro ao inserir match"
        db.close()

    def mountUserSkill(self, uData):
        return json.loads(uData)

class UserMatches(object):
    def on_get(self, req, resp, id):
        #"""GET ALL USERS  WHO HAVE A SKILL ""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware",charset="utf8", use_unicode = True)
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT id , id_user_not, id_user_has, id_skill FROM user_match WHERE id_user_not = %s OR id_user_has = %s" % (id, id)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
            if id == q[1]:
                id_search = int(q[2])
                teacher = False
            else:
                id_search = int(q[1])
                teacher = True
            #Executa a query
            sql = "SELECT id, nome, email, idade FROM users WHERE id = %d" % (id_search)
            cursor.execute(sql)
            #Recebe todos os resultados
            query = cursor.fetchall()
            #Converte
            user = UserModelMatch(query[0][0], query[0][1], query[0][2], query[0][3], q[3], teacher)
            queryObjects.append(user.__dict__)

        resp.body = json.dumps(queryObjects)
        db.close()
