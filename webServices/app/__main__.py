from __future__ import absolute_import, print_function
from app.repository.mongo_constants import *
from pymongo import MongoClient
from app.http.api.endpoints import app
from app.stickynote.posttype_definitions import *
from app.stickynote.schema import PosttypeSchema

db = MongoClient(MONGO_URL)[INSTANCE_NAME]
for collection in COLLECTIONS:
    db[collection].drop()

for definition in POSTTYPE_DEFINITIONS:
    posttype = PosttypeSchema().load(definition)
    data = posttype.data
    data['user_id'] = PUBLIC_USER_ID
    db[POSTTYPE_COLLECTION_NAME].insert_one(data)

print([ x for x in db[POSTTYPE_COLLECTION_NAME].find()])

app.run(debug=True)
