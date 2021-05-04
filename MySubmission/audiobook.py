# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:29:47 2021

@author: Mousam
"""


from datetime import datetime
class Audiobook:
    def Add(self, database, metadata):
        audio_id = metadata["_id"]
        title, author = metadata["title"], metadata["author"]
        duration, narrator = metadata["duration"], metadata["narrator"]
        upload_time = datetime.now()
        database.db.audiobook.insert({
                                    "_id" : audio_id,
                                    "title" : title,
                                    "author" : author,
                                    "narrator": narrator,
                                    "duration" : duration,
                                    "upload_time" : upload_time})
        
        
    
        
    def updateItem(self, database, metadata):
        audio_id = int(metadata["_id"])
        narrator = metadata["narrator"]
        title, author = metadata["title"], metadata["author"]
        duration, upload_time = metadata["duration"], datetime.now()
        response = database.db.audiobook.find_one_and_update({"_id" : audio_id}, {"$set" : {
                                                                                    "author" : author,
                                                                                    "narrator" : narrator,
                                                                                    "duration" : duration,
                                                                                    "upload_time" : upload_time,
                                                                                    "title" : title}})
        if response:
            return True
        return False
        
        
    def deleteItem(self, database, audioFileID):
        response = database.db.audiobook.find_one_and_delete({"_id" : int(audioFileID)})
        if response:
            return True
        return False
        
        
        