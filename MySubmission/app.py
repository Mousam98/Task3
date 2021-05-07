# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 11:30:42 2021

@author: Mousam
"""


from flask import Flask, request, jsonify
from json import dumps
from datetime import datetime
from flask_pymongo import PyMongo
from song import Song
from podcast import Podcast
from audiobook import Audiobook

app = Flask(__name__)
db_uri = "mongodb://localhost:27017/<database_name>"
app.config["MONGO_URI"] = db_uri
database = PyMongo(app)


@app.route("/create/", methods=["POST"])
def createAPI():
    if request.method == "POST":
        req = request.json
        audioFileType = req["audioFileType"]
        metadata = req.get("audioFileMetadata", None)
        if audioFileType == "song":
            obj = Song()
            obj.Add(database, metadata)
            return success()
        
        elif audioFileType == "podcast":
            obj = Podcast()
            if obj.Add(database, metadata):
                return success()
            return notfoundError()
        
        elif audioFileType == "audiobook":
            obj = Audiobook()
            obj.Add(database, metadata)
            return success()

        
        else:
            return notfoundError()
        
    else:
        return notfoundError()
        

@app.route('/<audioFileType>/<audioFileID>/', methods = ["DELETE"])
def deleteAPI(audioFileType, audioFileID):
    if request.method == "DELETE":
        if audioFileType == "song":
            obj = Song()
            if obj.deleteItem(database, audioFileID):
                return success()
            
            else:
                return notfoundError()
                
        
        elif audioFileType == "podcast":
            obj = Podcast()
            if obj.deleteItem(database, audioFileID):
                return success()
            else:
                return notfoundError()
        
        elif audioFileType == "audiobook":
            obj = Audiobook()
            if obj.deleteItem(database, audioFileID):
                return success()
            else:
                return notfoundError()
        
        else:
            return notfoundError()
            
    else:
        return notfoundError()
    
    
    
@app.route('/<audioFileType>/<audioFileID>/', methods = ["PUT"])
def updateAPI(audioFileType, audioFileID):
    if request.method == "PUT":
        res = request.json
        metadata = res.get("audioFileMetadata", None)
        if audioFileType == "song":
            obj = Song()
            if obj.updateItem(database, metadata):
                return success()
            else:
                return notfoundError()
            
        elif audioFileType == "podcast":
            obj = Podcast()
            if obj.updateItem(database, metadata):
                return success()
            else:
                return notfoundError()
        
        elif audioFileType == "audiobook":
            obj = Audiobook()
            if obj.updateItem(database, metadata):
                return success()
            else:
                return notfoundError()
            
        else:
            notfoundError()
            
    else:
        notfoundError()
            
            
            
@app.route('/<audioFileType>/<audioFileID>/', methods = ["GET"])
def getAPI(audioFileType, audioFileID):
    if request.method == "GET":
        if audioFileType == "song":
            res = database.db.song.find_one({"_id" : int(audioFileID)})
            if res:
                return jsonify(res)
            else:
                return notfoundError()
        
        elif audioFileType == "podcast":
            res = database.db.podcast.find_one({"_id" : int(audioFileID)})
            if res:
                return jsonify(res)
            else:
                return notfoundError()
        
        elif audioFileType == "audiobook":
            res = database.db.audiobook.find_one({"_id" : int(audioFileID)})
            if res:
                return jsonify(res)
            else:
                return notfoundError()
            
        else:
            return notfoundError()
            
    else:
        notfoundError()
        
@app.route('/<audioFileType>/', methods = ["GET"])
def getAPI_(audioFileType):
    if request.method == "GET":
        if audioFileType =="song":
            res = database.db.song.find()
            if res:
                return jsonify([i for i in res])
            return notfoundError()
        
        elif audioFileType == "podcast":
            res = database.db.podcast.find()
            if res:
                return jsonify([i for i in res])
            return notfoundError()
        
        elif audioFileType == "audiobook":
            res = database.db.audiobook.find()
            if res:
                return jsonify([i for i in res])
            return notfoundError()
        
        else:
            return notfoundError()
            
    else:
        return notfoundError()


@app.errorhandler(400)
def notfoundError(error = None):
    text = {
        "body" : "the request is invalid : 400 bad request",
        }
    response = jsonify(text)
    return response

@app.errorhandler(500)
def foundError(error = None):
    text = {
        "body" : "Any error: 500 internal server error"
        }
    return jsonify(text)

def success():
    text = {
        "body" : "Action is succesfull",
        "code" : "200, OK"
        }
    return jsonify(text)

if __name__ == "__main__":
    app.run(debug = True, port = 9090)
