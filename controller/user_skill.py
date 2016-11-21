import os
import uuid
import mimetypes
import MySQLdb
import json
import collections
import falcon
import sys

from model.user_skill import UserSkillModel

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

class UserSkill(object):
    def on_get(self, req, resp):
        #"""GET ALL PAIR USER-SKILL"""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        #Executa a query
        cursor.execute("SELECT  id , id_user, id_skill  FROM user_skills")
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                user_skill = UserSkillModel(q[0], q[1], q[2])
                queryObjects.append(user_skill.__dict__)
        resp.body = json.dumps(queryObjects)
        db.close()

    def on_post(self, req, resp):
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        body = req.stream.read()
        newusersql = self.mountUser(body)
        equery = "INSERT INTO user_skills (id_user, id_skill) VALUES (%s, %s)"

        try:
            cursor.execute(equery, (newusersql['id_user'], newusersql['id_skill'],))
            cursor.execute("SELECT LAST_INSERT_ID() FROM user_skills");
            result = {'id': int(cursor.fetchone()[0])}
            resp.body = json.dumps(result)
            resp.status = falcon.HTTP_201
            db.commit()
        except:
            db.rollback()
            print "Insert ERROR: ", sys.exc_info()[0]
            resp.status = falcon.HTTP_500
            resp.body = "Erro ao inserir -----"
        db.close()


class UserSkillSkill(object):
    def on_get(self, req, resp, skillID):
        #"""GET ALL USERS  WHO HAVE A SKILL ""
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT id_user FROM user_skills WHERE skillID = %d" % (id_skill)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                #BUSCAR OS DADOS DO USUÁRIO COM O ID =q[0]
        resp.body = json.dumps(queryObjects)
        db.close()

class UserSkillUser(object):
    def on_get(self, req, resp, userID):
        #"""GET ALL SKILLS  OF A  USER"
        db = MySQLdb.connect (host = "localhost",user = "pds",passwd = "123456",db = "processodesoftware")
        cursor = db.cursor()
        resp.status = falcon.HTTP_200  # Ok!
        id = int(id)
        #Executa a query
        sql = "SELECT id_skill FROM user_skills WHERE userID = %d" % (id_user)
        cursor.execute(sql)
        #Recebe todos os resultados
        query = cursor.fetchall()
        #Cria uma lista guardar os dados convertidos
        queryObjects = []
        #Converte
        for q in query:
                #BUSCAR OS DADOS DAS HABILIDADES COM O ID =q[0]
        resp.body = json.dumps(queryObjects)
        db.close()







