import unittest
import json

from aux import Aux

class FunTest(unittest.TestCase):

    aux = Aux()
    urlbase = "http://159.203.75.66:8000"

    def testPost(self):
             url= "/user"
             param = { "name":"Teste1","email":"teste1@teste.com","age":"21","password":"123456"}
             self.assertEqual(self.aux.postFunction(self.urlbase, url, param), 201)
             url = "/user/email/teste1@teste.com"
             res = self.aux.getFunction(self.urlbase, url)
             idd = json.loads(res)[0]['id']

             url = "/user/"
             self.aux.deleteFunction(self.urlbase, url,idd)

    def testGetByEmail(self):
             url= "/user"
             param = { "name":"Teste","email":"teste2@teste.com","age":"21","password":"123456"}
             self.aux.postFunction(self.urlbase, url, param)
             url = "/user/email/teste2@teste.com"
             res = self.aux.getFunction(self.urlbase, url)
             self.assertEqual(json.loads(res)[0]['email'], "teste2@teste.com")

             idd = json.loads(res)[0]['id']
             url = "/user/"
             self.aux.deleteFunction(self.urlbase, url,idd)

    def testDelete(self):
                 url= "/user"
                 param = { "name":"Teste3","email":"teste3@teste.com","age":"21","password":"123456"}
                 self.aux.postFunction(self.urlbase, url, param)
                 url = "/user/email/teste3@teste.com"
                 res = self.aux.getFunction(self.urlbase, url)
                 idd = json.loads(res)[0]['id']
                 url = "/user/"
                 self.assertEqual( self.aux.deleteFunction(self.urlbase, url,idd), 200)

if __name__ == '__main__':
        unittest.main()