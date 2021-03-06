# main.py

import os
import uuid
import mimetypes
import falcon
import gevent
from gevent import socket
from controller.users import *
from controller.users_info import *
from controller.image import *
from controller.skills import *
from controller.user_skill import *
from controller.user_interest import *
from controller.users_match import *

# falcon.API instances are callable WSGI apps
app = falcon.API()

# things will handle all requests to the '/things' URL path
app.add_route('/users', Users())
app.add_route('/user', User())
app.add_route('/user/{id}', User())
app.add_route('/user/email/{email}', UserEmail())
app.add_route('/login', Login())
app.add_route('/users/infos', UsersInfo())
app.add_route('/user/info', UserInfo())
app.add_route('/user/info/{id}', UserInfo())
app.add_route('/user/picture', Images())
app.add_route('/user/picture/{id}', Images())
app.add_route('/skill', Skills())
app.add_route('/skill/{id}', Skill())
app.add_route('/skill/autocomplete/{name}', SkillAutoComplete())
app.add_route('/users/skills', UserSkill())
app.add_route('/user/{id}/skills', UserSkill_User())
app.add_route('/skill/{id}/users', UserSkill_Skill())
app.add_route('/users/interests', UserInterest())
app.add_route('/user/{id}/interests', UserInterest_User())
app.add_route('/interest/{id}/users', UserInterest_Interest())
app.add_route('/matches', UserMatch())
app.add_route('/matches/{id}', UserMatches())
