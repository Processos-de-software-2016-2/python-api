import unittest
import json

from aux import Aux
from user_aux import UserAux

class UserTest(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testGetAll(self):
        email = "apiteste1@teste.com"

        self.user_aux.createUser(email)

        url = "/users/interests"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(0, len(response))

        idd = self.user_aux.getIdByEmail(email)

        self.createInterest(idd)

        url = "/users/interests"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email)

    def testGetInterestByUser(self):
        email = "apiteste1@teste.com"
        email2 = "apiteste2@teste.com"

        self.user_aux.createUser(email)
        self.user_aux.createUser(email2)

        idd1 = self.user_aux.getIdByEmail(email)
        idd2 = self.user_aux.getIdByEmail(email2)

        self.createInterest(idd1)
        self.createInterest(idd2)

        url = "/user/%d/interests" % (idd1)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        url = "/user/%d/interests" % (idd2)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email) 
        self.user_aux.deleteUser(email2) 

    def testGetUserByInterest(self):
        email = "apiteste1@teste.com"
        email2 = "apiteste2@teste.com"

        self.user_aux.createUser(email)
        self.user_aux.createUser(email2)

        idd1 = self.user_aux.getIdByEmail(email)
        idd2 = self.user_aux.getIdByEmail(email2)

        self.createInterest(idd1)
        self.createInterest(idd2)

        url = "/interest/%d/users" % (1)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(2, len(response))

        url = "/users/interests"
        param = {"id_user":idd1, "id_skill":"2"}
        self.aux.postFunction(self.urlbase, url, param)

        url = "/users/interests"
        param = {"id_user":idd2, "id_skill":"3"}
        self.aux.postFunction(self.urlbase, url, param)

        url = "/interest/%d/users" % (2)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        url = "/interest/%d/users" % (3)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email) 
        self.user_aux.deleteUser(email2) 

    def createInterest(self, idd):
        url = "/users/interests"
        param = {"id_user":idd, "id_skill":"1"}
        self.aux.postFunction(self.urlbase, url, param)

if __name__ == '__main__':
        unittest.main()
