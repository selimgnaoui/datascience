import pymongo
class Write_Tweest(object):
    db=""
    def __init__(self):
      
      connection = pymongo.MongoClient('ds237475.mlab.com',37475)
      self.db = connection['XXXX']
      self.db.authenticate('XXXXX', 'XXXXXX')
       
    def savetodb(self,tweets):
       (self.db.us.insert_many(tweets))
    
    def showtweets(self):
       cursor =self.db.us.find({})
       for document in cursor:
          print(document)
        
    def deletetweets(self):
         self.db.us.delete_many({})