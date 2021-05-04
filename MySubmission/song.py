# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:16:45 2021

@author: Mousam
"""

from datetime import datetime
from flask import jsonify
class Song:
    def Add(self, database, metadata):
        song_id = metadata["_id"]
        name = metadata["name"]
        duration = metadata["duration"]
        upload_time = datetime.now()
        database.db.song.insert({"_id" : song_id, "name" : name, "duration" : duration, "upload_time" : upload_time})
        
    
    def updateItem(self, database, metadata):
        song_id = metadata["_id"]
        name = metadata["name"]
        duration = metadata["duration"]
        upload_time = datetime.now()
        response = database.db.song.find_one_and_update({"_id": song_id}, {"$set" : {
                                                                  "name" : name,
                                                                  "duration" : duration,
                                                                  "upload_time" : upload_time}})
        if response:
            return True
        return False
        
    def deleteItem(self, database, audioFileID):
        response = database.db.song.find_one_and_delete({"_id" : int(audioFileID)})
        if response:
            return True
        return False
        
        
    

        