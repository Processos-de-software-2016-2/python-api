import unittest
import json
import base64

from aux import Aux

class SkillTest(unittest.TestCase):

    aux = Aux()
    urlbase = "http://127.0.0.1:8000"

    def testGetSkills(self):
        url = "/skill"
        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        self.assertTrue(response != "[]")

    def testGetSkillByID(self):
        url = "/skill/2"

        response = self.aux.getFunction(self.urlbase,url)
        response = json.loads(response)

        #TO DO
        ##colocar nome da skill com ID 10
        self.assertTrue(response[0]['name'] == "Programar em Java")

    def testGetSkillAutoComplete(self):
        name = "jav"
        #pega id do usuario
        url = "/skill/autocomplete/"+name

        response = self.aux.getFunction(self.urlbase, url)
        response = json.loads(response)

        #TO DO
        ## Ver esse retorno
        self.assertTrue(response != "[]")

if __name__ == '__main__':
        unittest.main()
