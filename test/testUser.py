import unittest
import requests
import json

class Aux:
    def getFuncition(self, urlbase, url):
        response = requests.get(urlbase+url)
        if response.status_code != 200:
                raise ApiError('GET/{}'.format(resp.status_code))
        return response

    def postFuncition(self, urlbase, url, param):
        response = requests.post(urlbase+url, json=param)
        if response.status_code != 201:
                raise ApiError('POST/{}'.format(resp.status_code))
        return response.status_code

    def deleteFuncition(self, urlbase, url,idd):
        response = requests.get(urlbase+url+idd)
        if response.status_code != 200:
                raise ApiError('DELETE/{}'.format(resp.status_code))
        return response.status_code

    def  putFuncition(self, urlbase, url, param):
        response = requests.get(urlbase+url, json=param)
        if response.status_code != 200:
                raise ApiError('put/{}'.format(resp.status_code))
        return response


class FunTest(unittest.TestCase):
    
    urlbase = "http://localhost:8000"
    aux = Aux()

    def testPost(self):
        url= "/user"
        param = { "name":"Teste","email":"asdsada9djq0aj@90asdjsa0d9asjd9a.c0m","age":"21","password":"123456"}
        self.assertEqual(self.aux.postFuncition(self.urlbase, url, param), 201)
        
        url = "/user/email/asdsada9djq0aj@90asdjsa0d9asjd9a.c0m"
        json = self.aux.getFuncition(self.urlbase, url)
        idd = json['id']

        url = "/user/" 
        deleteFuncition(self.urlbase, url,idd)

    def testGetByEmail(self):
        url= "/user"
        param = { "name":"Teste","email":"asdsada9djq0aj@90asdjsa0d9asjd9a.c0m","age":"21","password":"123456"}
        self.aux.postFuncition(self.urlbase, url, param)
        
        url = "/user/email/asdsada9djq0aj@90asdjsa0d9asjd9a.c0m"
        json = self.aux.getFuncition(self.urlbase, url)
        self.assertEqual(json['email'], "asdsada9djq0aj@90asdjsa0d9asjd9a.c0m")

        idd = json['id']
        url = "/user/" 
        deleteFuncition(self.urlbase, url,idd)

    def testDelete(self):
        url= "/user"
        param = { "name":"Teste","email":"asdsada9djq0aj@90asdjsa0d9asjd9a.c0m","age":"21","password":"123456"}      
        
        url = "/user/email/asdsada9djq0aj@90asdjsa0d9asjd9a.c0m"
        json = self.aux.getFuncition(self.urlbase, url)

        idd = json['id']
        url = "/user/" 
        self.assertEqual(deleteFuncition(urlbase, url,idd), 200)

if __name__ == '__main__':
    unittest.main()

