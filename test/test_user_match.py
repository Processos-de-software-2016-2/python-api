import unittest
import json

from aux import Aux
from user_aux import UserAux

class TestMatch(unittest.TestCase):

    aux = Aux()
    user_aux = UserAux()
    urlbase = "http://127.0.0.1:8000"

    def testGetAll(self):
        url = "/matches"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        email = "apiteste1@teste.com"
        email2 = "apiteste2@teste.com"

        self.user_aux.createUser(email)
        self.user_aux.createUser(email2)

        idd1 = self.user_aux.getIdByEmail(email)
        idd2 = self.user_aux.getIdByEmail(email2)

        param = { "id_user_not": idd1, "id_user_has": idd2,  "id_skill": "2" }
        self.aux.postFunction(self.urlbase, url, param)
        response1 = self.aux.getFunction(self.urlbase, url)
        response1 = json.loads(response)

        self.assertEqual(len(response) < len(response1))

        ##TEM CASCADE? AO DELETAR UM USER - REFLETE NAS OUTRAS TABELAS?
        self.user_aux.deleteUser(email)
        self.user_aux.deleteUser(email2)

if __name__ == '__main__':
        unittest.main()
