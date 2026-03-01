from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. 
        # Connection Variables
        USER = 'aacuser'
        PASS = 'SNHU2134'  # Using your specific password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'aac'  # Changed from 'animals' to 'aac' so it looks at the imported data
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d/%s' % (USER,PASS,HOST,PORT,DB))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # 1. CREATE METHOD
    def create(self, data):
        if data is not None:
            try:
                insert_result = self.collection.insert_one(data) 
                return insert_result.acknowledged
            except Exception as e:
                print(f"An error occurred during create: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # 2. READ METHOD
    def read(self, search_data):
        if search_data is not None:
            try:
                # Returns a list as required by the rubric
                cursor = self.collection.find(search_data, {"_id": False})
                return list(cursor)
            except Exception as e:
                print(f"An error occurred during read: {e}")
                return []
        else:
            try:
                # If empty, return all documents in a list
                cursor = self.collection.find({}, {"_id": False})
                return list(cursor)
            except Exception as e:
                return []

    # 3. UPDATE METHOD
    def update(self, search_query, update_data):
        if search_query is not None and update_data is not None:
            try:
                # update_many handles single or multiple document updates
                result = self.collection.update_many(search_query, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            raise Exception("Search query or update data is empty")

    # 4. DELETE METHOD
    def delete(self, search_query):
        if search_query is not None:
            try:
                # delete_many handles single or multiple document deletions
                result = self.collection.delete_many(search_query)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during delete: {e}")
                return 0
        else:
            raise Exception("Nothing to delete, because search_query parameter is empty")