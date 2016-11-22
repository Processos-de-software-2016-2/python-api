#user.py

class UserModel(object):
    
    def __init__(self, id, name, email, age, password=""):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.password = password

class UserModelMatch(object):
    
    def __init__(self, id, name, email, age, id_skill, teacher, password=""):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.password = password
        self.id_skill = id_skill
        self.teacher = teacher
