import pymongo


class Post:
    def __init__(self, database, collection):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[database]
        self.collection = db[collection]

    def insert(self, data):
        newData = self.collection.insert_one(data)
        return newData.inserted_id

    def createIndex(self, field):
        self.collection.create_index([(field, 1)], unique=True)

    def list(self):
        allData = self.collection.find()
        output = []
        for i in allData:
            output.append(i)
        return output
