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

        url = "/users/infos"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(0, len(response))

        idd = self.user_aux.getIdByEmail(email)

        self.createInfo(idd)

        url = "/users/infos"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        self.user_aux.deleteUser(email)

    def testGetByEmail(self):
        email = "apiteste2@teste.com"

        self.user_aux.createUser(email)

        idd = self.user_aux.getIdByEmail(email)

        self.createInfo(idd)

        url = "/user/info/%d" % (idd)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(84111111111, response[0]['whatsapp'])

        url = "/user/info"
        param = {"facebook": "http://www.facebook.com/example", "whatsapp": "84222222222", "id_user": idd}
        self.aux.putFunction(self.urlbase, url, param)        

        url = "/user/info/%d" % (idd)
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(84222222222, response[0]['whatsapp'])

        self.user_aux.deleteUser(email)

    def testDelete(self):
        email = "apiteste3@teste.com"

        self.user_aux.createUser(email)

        idd = self.user_aux.getIdByEmail(email)

        self.createInfo(idd)

        url = "/users/infos"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(1, len(response))

        url = "/user/info/"
        self.assertEqual( self.aux.deleteFunction(self.urlbase, url,idd), 200)

        url = "/users/infos"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertEqual(0, len(response))

    def createInfo(self, idd):
        url = "/user/info"
        param = {"facebook": "http://www.facebook.com/example", "whatsapp": "84111111111", "id_user": idd}
        self.aux.postFunction(self.urlbase, url, param)

if __name__ == '__main__':
        unittest.main()
