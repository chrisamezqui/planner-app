from ..repository import Repository
from ..repository.mongo import MongoRepository
from .schema import StickynoteSchema, PosttypeSchema
from ..repository.mongo_constants import *
from .posttype_definitions import *
# from uuid import uuid4

class CollectionService(object):
    def __init__(self, user_id, collection, schema, adapter=MongoRepository):
        self.repo_client = Repository(adapter(collection))
        self.user_id = user_id
        self.schema = schema

        if not user_id:
            raise Exception("user id not provided")

    # def get_random_id():
    #     return uuid4().int & (1<<63)-1

    def dump(self, data):
        return self.schema(exclude=['_id']).dump(data).data

    def prepare_item(self, postdata):
        data = postdata.data
        data['user_id'] = self.user_id
        return data

class PosttypeService(CollectionService):
    def __init__(self, user_id):
        super().__init__(user_id, POSTTYPE_COLLECTION_NAME, PosttypeSchema)

    def find_all_posttypes(self):
        posttypes = self.repo_client.find_all({'$or' : [{'user_id' : self.user_id},{'user_id': PUBLIC_USER_ID}]})
        return [self.dump(posttype) for posttype in posttypes]

    def find_posttype(self, id):
        posttype = self.repo_client.find({'$and' : [{'$or' : [{'user_id' : self.user_id},{'user_id': PUBLIC_USER_ID}]},{'type_id': id}]})
        return self.dump(posttype)

    def create_posttype_for(self, posttype_data):
        self.repo_client.create(self.prepare_item(posttype_data))
        return self.dump(posttype_data.data)

    def update_posttype_with(self, id, posttype_data):
        records_affected = self.repo_client.update({'user_id': self.user_id, 'type_id': id}, self.prepare_item(posttype_data))
        return records_affected > 0

    def delete_posttype_for(self, id):
        records_affected = self.repo_client.delete({'user_id': self.user_id, 'type_id': id})
        return records_affected > 0

class StickynoteService(CollectionService):
    def __init__(self, user_id):
        super().__init__(user_id, STICKYNOTE_COLLECTION_NAME, StickynoteSchema)

    def validate_type(self, stickynote):
        ptservice = PosttypeService(self.user_id)
        type_id = stickynote['type_id']
        posttype = ptservice.find_posttype(type_id)
        if not posttype:
            return False, "type_id not found"
        type_fields = posttype['type_fields']
        for key in stickynote.keys():
            if key not in META_FIELDS and stickynote[key] and key not in type_fields:
                return False, "contains invalid fields"
        return True, "type is valid"

    def find_all_stickynotes(self):
        stickynotes  = self.repo_client.find_all({'user_id': self.user_id})
        return [self.dump(stickynote) for stickynote in stickynotes]

    def find_stickynote(self, id):
        stickynote = self.repo_client.find({'user_id': self.user_id, 'note_id': id})
        return self.dump(stickynote)

    def create_stickynote_for(self, stickynote_data):
        stickynote = self.prepare_item(stickynote_data)
        ok, error = self.validate_type(stickynote)
        if not ok:
            return {}, error
        self.repo_client.create(stickynote)
        return self.dump(stickynote_data.data), ""

    def update_stickynote_with(self, id, stickynote_data):
        records_affected = self.repo_client.update({'user_id': self.user_id, 'note_id': id}, self.prepare_item(stickynote_data))
        return records_affected > 0

    def delete_stickynote_for(self, id):
        records_affected = self.repo_client.delete({'user_id': self.user_id, 'note_id': id})
        return records_affected > 0
