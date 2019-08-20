from pymongo import MongoClient
from .mongo_constants import *

class MongoRepository(object):
    def __init__(self, collection):
        self.db = MongoClient(MONGO_URL)[INSTANCE_NAME]
        self.collection = collection

    def find_all(self, selector):
        return self.db[self.collection].find(selector)

    def find(self, selector):
        return self.db[self.collection].find_one(selector)

    def create(self, item):
        return self.db[self.collection].insert_one(item)

    def update(self, selector, item):
        return self.db[self.collection].replace_one(selector, item).modified_count

    def delete(self, selector):
        return self.db[self.collection].delete_one(selector).deleted_count
