import unittest
import json

from aux import Aux
from user_aux import UserAux

class TestUserSkill(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testGetAll(self):
        email = "apiteste1@teste.com"

        self.user_aux.createUser(email)
        idd1 = self.user_aux.getIdByEmail(email)
        self.createSkill(idd1)

        url = "/users/skills"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertTrue(len(response) > 0)

        self.user_aux.deleteUser(email)

    def testGetSkillByUser(self):
        email = "apiteste2@teste.com"

        self.user_aux.createUser(email)
        idd1 = self.user_aux.getIdByEmail(email)
        self.createSkill(idd1)

        url = "/user/%d/skills" % (idd1)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email)

    def testGetUserBySkill(self):
        email = "apiteste3@teste.com"

        self.user_aux.createUser(email)

        idd1 = self.user_aux.getIdByEmail(email)

        self.createSkill(idd1)

        url = "/skill/%d/users" % (10)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email)

    def createSkill(self, idd):
        url = "/users/skills"
        param = {"id_user":idd, "id_skill":"10"}
        self.aux.postFunction(self.urlbase, url, param)

if __name__ == '__main__':
        unittest.main()
