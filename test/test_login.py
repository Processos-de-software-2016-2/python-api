import unittest
import json
import base64

from aux import Aux
from user_aux import UserAux

class LoginTest(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testExistentLogin(self):
        email = "apiteste1@teste.com"

        self.user_aux.createUser(email)

        #pega id do usuario
        url = "/login"
        param = {"email" : email, "password": "123456"}

        response = self.aux.login(self.urlbase, url, param)
        response = json.loads(response)

        self.assertTrue(response['logged'])

        self.user_aux.deleteUser(email)

    def testNonExistentLogin(self):
        email = "apiteste10@teste.com"

        #pega id do usuario
        url = "/login"
        param = {"email" : email, "password": "123456"}

        response = self.aux.login(self.urlbase, url, param)
        response = json.loads(response)

        self.assertFalse(response['logged'])

    def testWrongPasswordLogin(self):
        email = "apiteste1@teste.com"

        self.user_aux.createUser(email)

        #pega id do usuario
        url = "/login"
        param = {"email" : email, "password": "1234567"}

        response = self.aux.login(self.urlbase, url, param)
        response = json.loads(response)

        self.assertFalse(response['logged'])

        self.user_aux.deleteUser(email)

if __name__ == '__main__':
        unittest.main()
