# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:26:51 2021

@author: Mousam
"""

from json import dumps
from datetime import datetime
class Podcast:
    def Add(self, database, metadata):
        podcast_id, name = metadata["_id"], metadata["name"]
        upload_time = datetime.now()
        duration, host, participants = metadata["duration"], metadata["host"], metadata["participants"]
        if len(participants) > 10 or any(i for i in participants if len(i) > 100) or len(participants) == 0:
            return False
        else:
            response = database.db.podcast.insert({
                                        "_id": podcast_id,
                                        "name" : name,
                                        "duration" : duration,
                                        "upload_time" : upload_time,
                                        "host" : host,
                                        "participants" : participants
                                        })
            if response:
                return True
            return False
                
        
    def updateItem(self, database, metadata):
        podcast_id, upload_time = metadata["_id"], datetime.now()
        duration, name = metadata["duration"], metadata["name"]
        host, participants = metadata["host"], metadata["participants"]
        if len(participants) == 0 or len(participants) > 10 or any(i for i in participants if len(i) > 100):
            return False
        response = database.db.podcast.find_one_and_update({"_id": int(podcast_id)}, {"$set" : {
                                                                            "name" : name,
                                                                            "duration" : duration,
                                                                            "upload_time" : upload_time,
                                                                            "host" : host,
                                                                            "participants" : participants}})
        if response:
            return True
        return False

        
    def deleteItem(self, database, audioFileID):
        response = database.db.podcast.find_one_and_delete({"_id" : int(audioFileID)})
        if response:
            return True
        return False