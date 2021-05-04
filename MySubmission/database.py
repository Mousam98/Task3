# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:56:10 2021

@author: Mousam
"""

from app import app
from flask_pymongo import PyMongo
'''for mongodb compass database
db_name = "Audio-API"
db_url = "mongodb+srv://raj:{}@cluster0.swh9e.mongodb.net/{}?retryWrites=true&w=majority".format(password, db_name)'''

db_uri = "mongo://localhost:27017/AudioAPI"
database = PyMongo(app)
